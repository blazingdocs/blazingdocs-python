from blazingdocs import BlazingClient, MergeParameters, FormFile


def merge():
    client = BlazingClient('YOUR-API-KEY')
    parameters = MergeParameters()
    parameters.sequence = True

    with open('templates/PO-Template-Array.json', 'r', encoding='utf-8') as f:
        data = f.read()

    with open('templates/PO-Template-Array.docx', 'rb') as f:
        file = FormFile('PO-Template-Array.docx')
        file.content = f.read()

    operation = client.merge_with_form_file(
        data=data,
        filename='output.pdf',
        parameters=parameters,
        template=file
    )


if __name__ == '__main__':
    merge()
