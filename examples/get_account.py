from blazingdocs import BlazingClient


def get_account():
    client = BlazingClient('API-KEY')
    account = client.get_account()


if __name__ == '__main__':
    get_account()

