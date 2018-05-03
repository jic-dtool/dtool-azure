from dtoolcore import  DataSet

def test_httpenable():

    uri = "azure://jicinformatics/04c4e3a4-f072-4fc1-881a-602d589b089a"

    dataset = DataSet.from_uri(uri)

    http_manifest = dataset._storage_broker.generate_http_manifest()

    assert "admin_metadata" in http_manifest
    assert "item_urls" in http_manifest
    assert "overlays" in http_manifest
    assert "readme_url" in http_manifest
    assert "manifest_url" in http_manifest

    # Check item urls

    assert set(http_manifest["item_urls"].keys()) == set(dataset.identifiers)

    dataset._storage_broker.write_http_manifest(http_manifest)
