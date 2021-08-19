from enum import Enum


class DataSourceType(str, Enum):
    CSV: str = 'CSV'
    JSON: str = 'JSON'
    XML: str = 'XML'
