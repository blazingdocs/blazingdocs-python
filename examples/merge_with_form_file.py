from blazingdocs import BlazingClient, MergeParameters, FormFile


def merge():
    client = BlazingClient('YOUR-API-KEY')
    parameters = MergeParameters()

    with open('templates/PO-Template.json', 'r', encoding='utf-8') as f:
        data = f.read()

    with open('templates/PO-Template.docx', 'rb') as f:
        file = FormFile('PO-Template.docx')
        file.content = f.read()

    operation = client.merge_with_form_file(
        data=data,
        filename='output.pdf',
        parameters=parameters,
        template=file
    )


if __name__ == '__main__':
    merge()

