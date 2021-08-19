# BlazingDocs Python client
High-performance document generation API. Generate documents and reports from СSV, JSON, XML with 99,9% uptime and 24/7 monitoring.

## Installation

Run this line from Terminal:

```
pip install blazingdocs
```

## Integration basics

### Setup

You can get your API Key at https://app.blazingdocs.com

```python
client = BlazingClient('API-KEY')
```

### Getting account info

```python
account = client.get_account()
```

### Getting merge templates list

```python
templates = client.get_templates()
```

### Getting usage info

```python
usage = client.get_usage()
```

### Executing merge with template id

```python
client = BlazingClient('API-KEY')
parameters = MergeParameters()

with open('templates/PO-Template.json', 'r', encoding='utf-8') as f:
    data = f.read()

operation = client.merge_with_id(
    data=data,
    filename='output.pdf',
    parameters=parameters,
    template=uuid.UUID('TEMPLATE-ID')
)
```

### Executing merge with relative path

```python
client = BlazingClient('API-KEY')
parameters = MergeParameters()

with open('templates/PO-Template.json', 'r', encoding='utf-8') as f:
    data = f.read()

operation = client.merge_with_relative_path(
    data=data,
    filename='output.pdf',
    parameters=parameters,
    template='RELATIVE-PATH'  # e.g. 'folder/nested_folder/Template.docx'
)
```

### Executing merge with form file

```python
client = BlazingClient('API-KEY')
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
```

### Executing merge with array

```python
client = BlazingClient('API-KEY')
parameters = MergeParameters()
parameters.sequence = True # data is array

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
```

## Documentation

See more details here https://docs.blazingdocs.com