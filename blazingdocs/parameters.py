from .enums import DataSourceType
from .utils import Object


class MergeParameters(Object):
    def __init__(self):
        self.dataSourceName: str = 'data'
        self.dataSourceType: DataSourceType = DataSourceType.JSON  # data in json format
        self.sequence: bool = False  # data is object
        self.parseColumns: bool = False
        self.strict: bool = True  # keep json types
