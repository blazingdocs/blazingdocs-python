import json
from io import BytesIO


class Object:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class FormFile:

    def __init__(self, name: str):
        self.name: str = name
        self.contentType: str
        self.content: BytesIO
