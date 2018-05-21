from dtoolcore import  DataSet

def test_http_manifest():

    uri = "azure://jicinformatics/04c4e3a4-f072-4fc1-881a-602d589b089a"

    dataset = DataSet.from_uri(uri)

    http_manifest = dataset._storage_broker.generate_http_manifest()

    assert "admin_metadata" in http_manifest
    assert http_manifest["admin_metadata"] == dataset._admin_metadata


    assert "overlays" in http_manifest
    assert "readme_url" in http_manifest
    assert "manifest_url" in http_manifest

    # Check item urls
    assert "item_urls" in http_manifest
    assert set(http_manifest["item_urls"].keys()) == set(dataset.identifiers)

    dataset._storage_broker.write_http_manifest(http_manifest)

def test_http_enable():

    uri = "azure://jicinformatics/8e65e5ee-a5c7-4a0e-bc2d-a47f8c3a6809"

    dataset = DataSet.from_uri(uri)

    access_url = dataset._storage_broker.http_enable()

    assert access_url.startswith("https://")
