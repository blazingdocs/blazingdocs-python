from blazingdocs import BlazingClient, MergeParameters


def merge():
    client = BlazingClient('YOUR-API-KEY')
    parameters = MergeParameters()

    with open('templates/PO-Template.json', 'r', encoding='utf-8') as f:
        data = f.read()

    operation = client.merge_with_relative_path(
        data=data,
        filename='output.pdf',
        parameters=parameters,
        template='RELATIVE-PATH'  # e.g. 'folder/nested_folder/Template.docx'
    )


if __name__ == '__main__':
    merge()

