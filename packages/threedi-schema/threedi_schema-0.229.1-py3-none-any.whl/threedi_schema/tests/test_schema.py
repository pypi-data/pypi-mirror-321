from unittest import mock

import pytest
from sqlalchemy import Column, Integer, MetaData, String, Table, text

from threedi_schema import ModelSchema
from threedi_schema.application import errors
from threedi_schema.application.schema import get_schema_version
from threedi_schema.domain import constants
from threedi_schema.infrastructure.spatialite_versions import get_spatialite_version


@pytest.fixture
def south_migration_table(in_memory_sqlite):
    south_migrationhistory = Table(
        "south_migrationhistory", MetaData(), Column("id", Integer)
    )
    engine = in_memory_sqlite.engine
    south_migrationhistory.create(engine)
    return south_migrationhistory


@pytest.fixture
def alembic_version_table(in_memory_sqlite):
    alembic_version = Table(
        constants.VERSION_TABLE_NAME,
        MetaData(),
        Column("version_num", String(32), nullable=False),
    )
    engine = in_memory_sqlite.engine
    alembic_version.create(engine)
    return alembic_version


def test_get_schema_version():
    """The current version in the library. We start counting at 200."""
    # this will catch future mistakes of setting non-integer revisions
    assert get_schema_version() >= 200


def test_get_version_no_tables(in_memory_sqlite):
    """Get the version of a sqlite with no version tables"""
    schema_checker = ModelSchema(in_memory_sqlite)
    migration_id = schema_checker.get_version()
    assert migration_id is None


def test_get_version_empty_south(in_memory_sqlite, south_migration_table):
    """Get the version of a sqlite with an empty South version table"""
    schema_checker = ModelSchema(in_memory_sqlite)
    migration_id = schema_checker.get_version()
    assert migration_id is None


def test_get_version_south(in_memory_sqlite, south_migration_table):
    """Get the version of a sqlite with a South version table"""
    with in_memory_sqlite.engine.connect() as connection:
        with connection.begin():
            for v in (42, 43):
                connection.execute(south_migration_table.insert().values(id=v))

    schema_checker = ModelSchema(in_memory_sqlite)
    migration_id = schema_checker.get_version()
    assert migration_id == 43


def test_get_version_empty_alembic(in_memory_sqlite, alembic_version_table):
    """Get the version of a sqlite with an empty alembic version table"""
    schema_checker = ModelSchema(in_memory_sqlite)
    migration_id = schema_checker.get_version()
    assert migration_id is None


def test_get_version_alembic(in_memory_sqlite, alembic_version_table):
    """Get the version of a sqlite with an alembic version table"""
    with in_memory_sqlite.engine.connect() as connection:
        with connection.begin():
            connection.execute(
                alembic_version_table.insert().values(version_num="0201")
            )

    schema_checker = ModelSchema(in_memory_sqlite)
    migration_id = schema_checker.get_version()
    assert migration_id == 201


def test_validate_schema(sqlite_latest):
    """Validate a correct schema version"""
    schema = sqlite_latest.schema
    with mock.patch.object(schema, "get_version", return_value=get_schema_version()):
        assert schema.validate_schema()


@pytest.mark.parametrize("version", [-1, 205, None])
def test_validate_schema_missing_migration(sqlite_latest, version):
    """Validate a too low schema version"""
    schema = ModelSchema(sqlite_latest)
    with mock.patch.object(schema, "get_version", return_value=version):
        with pytest.raises(errors.MigrationMissingError):
            schema.validate_schema()


@pytest.mark.parametrize("version", [9999])
def test_validate_schema_too_high_migration(sqlite_latest, version):
    """Validate a too high schema version"""
    schema = ModelSchema(sqlite_latest)
    with mock.patch.object(schema, "get_version", return_value=version):
        with pytest.warns(UserWarning):
            schema.validate_schema()


def test_full_upgrade_empty(in_memory_sqlite):
    """Upgrade an empty database to the latest version"""
    schema = ModelSchema(in_memory_sqlite)
    schema.upgrade(backup=False, upgrade_spatialite_version=False)
    assert schema.get_version() == get_schema_version()
    assert in_memory_sqlite.has_table("connection_node")


def test_full_upgrade_with_preexisting_version(south_latest_sqlite):
    """Upgrade an empty database to the latest version"""
    schema = ModelSchema(south_latest_sqlite)
    schema.upgrade(backup=False, upgrade_spatialite_version=False)
    assert schema.get_version() == get_schema_version()
    assert south_latest_sqlite.has_table("connection_node")
    # https://github.com/nens/threedi-schema/issues/10:
    assert not south_latest_sqlite.has_table("v2_levee")


def test_full_upgrade_oldest(oldest_sqlite):
    """Upgrade a legacy database to the latest version"""
    schema = ModelSchema(oldest_sqlite)
    schema.upgrade(backup=False, upgrade_spatialite_version=False)
    assert schema.get_version() == get_schema_version()
    assert oldest_sqlite.has_table("connection_node")
    # https://github.com/nens/threedi-schema/issues/10:
    assert not oldest_sqlite.has_table("v2_levee")


def test_upgrade_south_not_latest_errors(in_memory_sqlite):
    """Upgrading a database that is not at the latest south migration will error"""
    schema = ModelSchema(in_memory_sqlite)
    with mock.patch.object(
        schema, "get_version", return_value=constants.LATEST_SOUTH_MIGRATION_ID - 1
    ):
        with pytest.raises(errors.MigrationMissingError):
            schema.upgrade(backup=False, upgrade_spatialite_version=False)


def test_upgrade_with_backup(south_latest_sqlite):
    """Upgrading with backup=True will proceed on a copy of the database"""
    schema = ModelSchema(south_latest_sqlite)
    with mock.patch(
        "threedi_schema.application.schema._upgrade_database", side_effect=RuntimeError
    ) as upgrade, mock.patch.object(schema, "get_version", return_value=199):
        with pytest.raises(RuntimeError):
            schema.upgrade(backup=True, upgrade_spatialite_version=False)

    (db,), kwargs = upgrade.call_args
    assert db is not south_latest_sqlite


def test_upgrade_without_backup(south_latest_sqlite):
    """Upgrading with backup=True will proceed on the database itself"""
    schema = ModelSchema(south_latest_sqlite)
    with mock.patch(
        "threedi_schema.application.schema._upgrade_database", side_effect=RuntimeError
    ) as upgrade, mock.patch.object(schema, "get_version", return_value=199):
        with pytest.raises(RuntimeError):
            schema.upgrade(backup=False, upgrade_spatialite_version=False)

    (db,), kwargs = upgrade.call_args
    assert db is south_latest_sqlite


def test_convert_to_geopackage_raise(oldest_sqlite):
    if get_schema_version() >= 300:
        pytest.skip("Warning not expected beyond schema 300")
    schema = ModelSchema(oldest_sqlite)
    with pytest.raises(errors.UpgradeFailedError):
        schema.upgrade(
            backup=False, upgrade_spatialite_version=False, convert_to_geopackage=True
        )


def test_upgrade_revision_exception(oldest_sqlite):
    schema = ModelSchema(oldest_sqlite)
    with pytest.raises(ValueError):
        schema.upgrade(revision="foo")


def test_upgrade_spatialite_3(oldest_sqlite):
    lib_version, file_version_before = get_spatialite_version(oldest_sqlite)
    if lib_version == file_version_before:
        pytest.skip("Nothing to test: spatialite library version equals file version")

    schema = ModelSchema(oldest_sqlite)
    schema.upgrade(backup=False, upgrade_spatialite_version=True)

    _, file_version_after = get_spatialite_version(oldest_sqlite)
    assert file_version_after == 4

    # the spatial indexes are there
    with oldest_sqlite.engine.connect() as connection:
        check_result = connection.execute(
            text("SELECT CheckSpatialIndex('connection_node', 'geom')")
        ).scalar()
    assert check_result == 1


def test_set_spatial_indexes(in_memory_sqlite):
    engine = in_memory_sqlite.engine

    schema = ModelSchema(in_memory_sqlite)
    schema.upgrade(backup=False)

    with engine.connect() as connection:
        with connection.begin():
            connection.execute(
                text("SELECT DisableSpatialIndex('connection_node', 'geom')")
            ).scalar()
            connection.execute(text("DROP TABLE idx_connection_node_geom"))

    schema.set_spatial_indexes()

    with engine.connect() as connection:
        check_result = connection.execute(
            text("SELECT CheckSpatialIndex('connection_node', 'geom')")
        ).scalar()

    assert check_result == 1
