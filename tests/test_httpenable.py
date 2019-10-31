from dtoolcore import DataSet

from . import CONFIG_PATH


def test_http_manifest():

    uri = "azure://dtooltesting/c58038a4-3a54-425e-9087-144d0733387f"

    dataset = DataSet.from_uri(uri, CONFIG_PATH)

    http_manifest = dataset._storage_broker._generate_http_manifest()

    assert "admin_metadata" in http_manifest
    assert http_manifest["admin_metadata"] == dataset._admin_metadata

    assert "overlays" in http_manifest
    assert "readme_url" in http_manifest
    assert "manifest_url" in http_manifest

    # Check item urls
    assert "item_urls" in http_manifest
    assert set(http_manifest["item_urls"].keys()) == set(dataset.identifiers)

    dataset._storage_broker._write_http_manifest(http_manifest)


def test_http_enable():

    uri = "azure://dtooltesting/c58038a4-3a54-425e-9087-144d0733387f"

    dataset = DataSet.from_uri(uri, CONFIG_PATH)

    access_url = dataset._storage_broker.http_enable()

    assert access_url.startswith("https://")
