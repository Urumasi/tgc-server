from src.server import Server


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 17013

    server = Server(host, port)
    server.run()
