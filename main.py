
from server import Server


def run():
    print('running')
    server = Server()
    server.spawn()


if __name__ == '__main__':
    run()