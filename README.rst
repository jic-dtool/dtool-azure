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

Then you need to run:

.. code-block:: bash

    az storage account show-connection-string --name jicinformatics --resource-group jic_informatics_resources_ukwest
