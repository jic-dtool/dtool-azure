"""Test the S3StorageBroker self description metadata."""

from . import tmp_uuid_and_uri  # NOQA
from . import (
    _key_exists_in_storage_broker,
    _get_data_structure_from_key,
    _get_unicode_from_key,
    CONFIG_PATH,
)


def test_writing_of_dtool_structure_file(tmp_uuid_and_uri):  # NOQA
    from dtoolcore import ProtoDataSet, generate_admin_metadata

    # Create a proto dataset.
    uuid, dest_uri = tmp_uuid_and_uri
    name = "test_dtool_structure_file"
    admin_metadata = generate_admin_metadata(name)
    admin_metadata["uuid"] = uuid
    proto_dataset = ProtoDataSet(
        uri=dest_uri,
        admin_metadata=admin_metadata,
        config_path=CONFIG_PATH
    )
    proto_dataset.create()

    # Check that the ".dtool/structure.json" file exists.
    expected_azure_key = 'structure.json'
    assert _key_exists_in_storage_broker(
        proto_dataset._storage_broker,
        expected_azure_key
    )

    from dtool_azure.storagebroker import _STRUCTURE_PARAMETERS as expected_content  # NOQA

    actual_content = _get_data_structure_from_key(
        proto_dataset._storage_broker,
        expected_azure_key
    )
    assert expected_content == actual_content


def test_writing_of_dtool_readme_file(tmp_uuid_and_uri):  # NOQA
    from dtoolcore import ProtoDataSet, generate_admin_metadata

    # Create a proto dataset.
    uuid, dest_uri = tmp_uuid_and_uri
    name = "test_dtool_readme_file"
    admin_metadata = generate_admin_metadata(name)
    admin_metadata["uuid"] = uuid
    proto_dataset = ProtoDataSet(
        uri=dest_uri,
        admin_metadata=admin_metadata,
        config_path=CONFIG_PATH
    )
    proto_dataset.create()

    # Check that the ".dtool/README.txt" file exists.
    expected_azure_key = 'README.txt'
    assert _key_exists_in_storage_broker(
        proto_dataset._storage_broker,
        expected_azure_key
    )

    actual_content = _get_unicode_from_key(
        proto_dataset._storage_broker,
        expected_azure_key
    )
    assert actual_content.startswith("README")
