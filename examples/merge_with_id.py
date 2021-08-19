import uuid
from blazingdocs import BlazingClient, MergeParameters


def merge():
    client = BlazingClient('YOUR-API-KEY')
    parameters = MergeParameters()

    with open('templates/PO-Template.json', 'r', encoding='utf-8') as f:
        data = f.read()

    operation = client.merge_with_id(
        data=data,
        filename='output.pdf',
        parameters=parameters,
        template=uuid.UUID('YOUR-TEMPLATE-ID')
    )


if __name__ == '__main__':
    merge()
