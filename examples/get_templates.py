from blazingdocs import BlazingClient


def get_templates():
    client = BlazingClient('API-KEY')
    templates = client.get_templates()


if __name__ == '__main__':
    get_templates()

