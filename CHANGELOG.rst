CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added support for tags.

Added
^^^^^

- Added ``dtool_azure.storagebroker.AzureStorageBroker.delete_key()`` method
- Added ``dtool_azure.storagebroker.AzureStorageBroker.get_tag_key()`` method
- Added ``dtool_azure.storagebroker.AzureStorageBroker.list_tags()`` method


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^

- Made
  ``dtool_azure.storagebroker.AzureStorageBroker.list_dataset_uris``
  more robust in cases where there is a container without metadata

Security
^^^^^^^^


[0.6.0] - 2019-10-31
--------------------

Added
^^^^^

- Added support for dataset annotations


[0.5.0] - 2019-07-12
--------------------

Added
^^^^^

- Added optimisation to improve speed when copying data from Azure storage


[0.4.0] - 2019-04-25
--------------------

Changed
^^^^^^^

- Cache environment variable changed from DTOOL_AZURE_CACHE_DIRECTORY to DTOOL_CACHE_DIRECTORY
- Default cache directory changed from ``~/.cache/dtool/azure`` to ``~/.cache/dtool``


[0.3.1] - 2018-09-07
--------------------

Fixed
^^^^^

- Generation of md5 checksums for large files, previously set to "None"


[0.3.0] - 2018-07-24
--------------------

Added
^^^^^

- Added ``storage_broker_version`` to structure parameters
- Added inheritance from ``dtoolcore.storagebroker.BaseStorageClass``
- Overrode ``get_text`` method on ``BaseStorageBroker`` class
- Overrode ``put_text`` method on ``BaseStorageBroker`` class
- Overrode ``get_admin_metadata_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_readme_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_manifest_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_overlay_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_structure_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_dtool_readme_key`` method on ``BaseStorageBroker`` class
- Overrode ``get_size_in_bytes`` method on ``BaseStorageBroker`` class
- Overrode ``get_utc_timestamp`` method on ``BaseStorageBroker`` class
- Overrode ``get_hash`` method on ``BaseStorageBroker`` class


[0.2.1] - 2018-07-05
--------------------

Fixed
^^^^^

- Made download to DTOOL_AZURE_CACHE_DIRECTORY more robust


[0.2.0] - 2018-07-05
--------------------

Added
^^^^^

- Added ability to configure multiple Azure storage accounts
- Added ``http_enable`` method to the ``S3StorageBroker`` class,  to allow publishing of datasets


[0.1.0] - 2018-03-12
--------------------

Initial release.
