from contextlib import contextmanager

from dbt.adapters.base import Credentials
from dbt.adapters.sql import SQLConnectionManager


MSSQL_CREDENTIALS_CONTRACT = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'database': {
            'type': 'string',
        },
        'schema': {
            'type': 'string',
        },
    },
    'required': ['database', 'schema'],
}


class MSSQLCredentials(Credentials):
    SCHEMA = MSSQL_CREDENTIALS_CONTRACT

    @property
    def type(self):
        return 'mssql'

    def _connection_keys(self):
        # return an iterator of keys to pretty-print in 'dbt debug'
        raise NotImplementedError


class MSSQLConnectionManager(SQLConnectionManager):
    TYPE = 'mssql'
