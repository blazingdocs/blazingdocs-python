from blazingdocs import BlazingClient


def get_usage():
    client = BlazingClient('API-KEY')
    usage = client.get_usage()


if __name__ == '__main__':
    get_usage()
