"""Dtool Azure helper functions."""

import base64
import binascii

from dtoolcore.utils import get_config_value


def get_azure_account_key(account_name, config_path):
    """Return the Azure account key associated with the account name."""

    account_key = get_config_value(
        "DTOOL_AZURE_ACCOUNT_KEY_" + account_name,
        config_path=config_path
    )
    return account_key


def base64_to_hex(input_string):
    """Return the hex encoded version of the base64 encoded input string."""

    return binascii.hexlify(base64.b64decode(input_string)).decode()
