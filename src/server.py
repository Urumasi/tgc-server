import socket

from src.connection import handle_connection


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.max_games = 1000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

    def __del__(self):
        self.socket.close()

    def run(self):
        print(f"Starting server on {self.host}, port {self.port}")
        try:
            while True:
                self.socket.listen()
                conn, addr = self.socket.accept()
                handle_connection(conn, addr)
        except KeyboardInterrupt:
            print("Interrupted, exiting...")
