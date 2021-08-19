from json import JSONEncoder
from .parameters import MergeParameters


# JSONEncoder that encodes MergeParameters objects as JSON
class MergeParametersEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, MergeParameters):
            return object.__dict__
        else:
            # Call base class implementation which takes care of
            # raising exceptions for unsupported types
            return JSONEncoder.default(self, object)
