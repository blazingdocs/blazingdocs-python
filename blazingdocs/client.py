import uuid
import requests
from builtins import isinstance
from typing import List, Union
from .exceptions import BlazingException
from .models import Operation, Account, Usage, Template
from .parameters import MergeParameters
from .utils import FormFile


# BlazingClient API client.
class BlazingClient:
    __headers = None
    __api_key: str = None
    __base_url: str = 'https://api.blazingdocs.com'

    # Creates new instance of client.
    def __init__(self, api_key: str):
        self.__api_key = api_key
        self.__headers = {'X-API-Key': self.__api_key}

    # Executes merge operation with union template.
    def __merge(self, data: str, filename: str, parameters: MergeParameters, template: Union[str, uuid.UUID, FormFile]) -> Operation:
        url = self.__base_url + '/operation/merge'

        if not (data and data.strip()):
            raise ValueError('Data is not provided')

        if not (filename and filename.strip()):
            raise ValueError('Output filename is not provided')

        if not parameters:
            raise ValueError('Merge parameters are not provided')

        payload = dict(
            Data=(None, data),
            OutputName=(None, filename),
            MergeParameters=(None, parameters.to_json())
        )

        if isinstance(template, uuid.UUID):
            payload['Template'] = (None, str(template))
        elif isinstance(template, str):
            payload['Template'] = (None, template.replace('\\', '/'))
        elif isinstance(template, FormFile):
            payload['Template'] = (template.name, template.content)
        else:
            raise ValueError('Template is not provided')

        response = requests.post(url=url, headers=self.__headers, files=payload, timeout=10)
        return Operation(self.__handle_response(response))

    # Gets account info.
    def get_account(self) -> Account:
        url = self.__base_url + '/account'
        response = requests.get(url, headers=self.__headers, timeout=10)
        return Account(self.__handle_response(response))

    # Gets usage info.
    def get_usage(self) -> Usage:
        url = self.__base_url + '/usage'
        response = requests.get(url, headers=self.__headers, timeout=10)
        return Usage(self.__handle_response(response))

    # Gets templates list.
    def get_templates(self, path: str = None) -> List[Template]:
        url = self.__base_url + '/templates'

        if path is not None:
            url += path

        response = requests.get(url, headers=self.__headers, timeout=10)
        decoded = self.__handle_response(response)
        return list(map(Template, decoded))

    # Executes merge operation with template id.
    def merge_with_id(self, data: str, filename: str, parameters: MergeParameters, template: uuid.UUID) -> Operation:
        return self.__merge(data, filename, parameters, template)

    # Executes merge operation with template path.
    def merge_with_relative_path(self, data: str, filename: str, parameters: MergeParameters, template: str) -> Operation:
        return self.__merge(data, filename, parameters, template)

    # Executes merge operation with template form file.
    def merge_with_form_file(self, data: str, filename: str, parameters: MergeParameters, template: FormFile) -> Operation:
        return self.__merge(data, filename, parameters, template)

    # Handle response.
    def __handle_response(self, response: requests.Response):
        try:
            if not response.status_code == requests.codes.ok:
                message = response.json().get('message', '[Message not found]')
                raise BlazingException(response.status_code, message)
        except ValueError as ex:
            raise ex

        return response.json()
