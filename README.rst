README
======

Add Azure dataset support to dtool

To install the dtool-azure package.

.. code-block:: bash

    cd dtool-azure
    python setup.py install

Configuration
-------------

Install the Azure command line client via:

.. code-block:: bash

    pip install azure-cli

(you may wish to install this in a virtual environment)

Then:

.. code-block:: bash

    az login

To log into Azure.

Then you need to run (changing the resource name/group as appropriate):

.. code-block:: bash

    az storage account show-connection-string --name jicinformatics --resource-group jic_informatics_resources_ukwest

Then create the file ``.config/dtoolazure/config.json`` as follows:

.. code-block:: json

    {
        "DTOOL_AZURE_ACCOUNT_NAME": "jicinformatics",
        "DTOOL_AZURE_ACCOUNT_KEY": "<KEY HERE>"
    }

Changing the account name and key as appropriate.
