
import os

import pytest

from dtoolcore import generate_admin_metadata

from dtool_azure.storagebroker import (
    AzureStorageBroker,
)

_HERE = os.path.dirname(__file__)
TEST_SAMPLE_DATA = os.path.join(_HERE, "data")

def _remove_dataset(uri):

    storage_broker = AzureStorageBroker(uri)

    storage_broker._blobservice.delete_container(storage_broker.uuid)


@pytest.fixture
def tmp_uuid_and_uri(request):
    admin_metadata = generate_admin_metadata("test_dataset")
    uuid = admin_metadata["uuid"]

    uri = AzureStorageBroker.generate_uri(
        "test_dataset",
        uuid,
        "azure://test-dtool-azure-collection"
    )

    @request.addfinalizer
    def teardown():
        _remove_dataset(uri)

    return (uuid, uri)
