from .enums import DataSourceType
from .utils import Object


class MergeParameters(Object):
    def __init__(self):
        self.dataSourceName: str = 'data'
        self.dataSourceType: DataSourceType = DataSourceType.JSON
        self.sequence: bool = False
        self.parseColumns: bool = False
        self.strict: bool = True
