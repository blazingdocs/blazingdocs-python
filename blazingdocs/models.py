import requests
from io import BytesIO
from datetime import datetime
from decimal import Decimal
from uuid import UUID


class Plan:

    def __init__(self, response):
        self.response = response

    @property
    def id(self) -> UUID:
        return self.response['id']

    @property
    def name(self) -> str:
        return self.response['name']

    @property
    def price(self) -> Decimal:
        return self.response['price']

    @property
    def price_per_unit(self) -> Decimal:
        return self.response['pricePerUnit']

    @property
    def quota(self) -> int:
        return self.response['quota']


class Account:

    def __init__(self, response):
        self.response = response

    @property
    def id(self) -> UUID:
        return self.response['id']

    @property
    def name(self) -> str:
        return self.response['name']

    @property
    def plan(self) -> Plan:
        return Plan(self.response['plan'])

    @property
    def api_key(self) -> str:
        return self.response['apiKey']

    @property
    def obsolete_api_key(self) -> str:
        return self.response['obsoleteApiKey']

    @property
    def created_at(self) -> datetime:
        return self.response['createdAt']

    @property
    def last_synced_at(self) -> datetime:
        return self.response['lastSyncedAt']

    @property
    def updated_at(self) -> datetime:
        return self.response['updatedAt']


class OperationType:

    def __init__(self, response):
        self.response = response

    @property
    def name(self) -> str:
        return self.response['name']


class Operation:

    def __init__(self, response):
        self.response = response

    @property
    def id(self) -> UUID:
        return self.response['id']

    @property
    def operation_type(self) -> OperationType:
        return OperationType(self.response['type'])

    @property
    def page_count(self) -> int:
        return self.response['pageCount']

    @property
    def elapsed_milliseconds(self) -> int:
        return self.response['elapsedMilliseconds']

    @property
    def remote_ip_address(self) -> str:
        return self.response['remoteIpAddress']

    @property
    def files(self) -> []:
        return list(map(File, self.response['files']))

    @property
    def io(self) -> BytesIO:
        if not self.files:
            raise ValueError('File not found')

        response = requests.get(self.files[0].download_url, timeout=1800)
        return BytesIO(response.content)


class File:

    def __init__(self, response):
        self.response = response

    @property
    def id(self) -> UUID:
        return self.response['id']

    @property
    def name(self) -> str:
        return self.response['name']

    @property
    def content_type(self) -> str:
        return self.response['contentType']

    @property
    def download_url(self) -> str:
        return self.response['downloadUrl']

    @property
    def created_at(self) -> datetime:
        return self.response['createdAt']

    @property
    def last_modified_at(self) -> datetime:
        return self.response['lastModifiedAt']

    @property
    def last_accessed_at(self) -> datetime:
        return self.response['lastAccessedAt']

    @property
    def length(self) -> int:
        return self.response['length']

    @property
    def io(self) -> BytesIO:
        response = requests.get(self.download_url, timeout=1800)
        return BytesIO(response.content)


class Template(File):
    pass


class Usage:

    def __init__(self, response):
        self.response = response

    @property
    def quota(self) -> int:
        return self.response['quota']

    @property
    def page_count(self) -> int:
        return self.response['pageCount']

    @property
    def usage(self) -> int:
        return self.response['usage']
