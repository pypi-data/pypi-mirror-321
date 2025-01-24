import socket

from pyrcon4squad.exceptions import IllegalArgumentException
from pyrcon4squad.rcon_packet import send_auth, RconPacket, send, listen

request_id = 0

class Rcon:

    sock = None

    def __init__(self, host: str, port: int, password: str):
        """

        :param host: host of game server
        :param port: rcon port of game server
        :param password: rcon password
        """
        self.host = host
        self.port = port
        self.password = password

    def _connect(self):
        global request_id
        if self.host is None or self.host == "":
            raise IllegalArgumentException("host cannot be None")
        if self.port is None:
            raise IllegalArgumentException("port cannot be None")
        if self.port < 1 or self.port > 65535:
            raise IllegalArgumentException("port must be between 1 and 65535")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(1)

    def __enter__(self):
        self._connect()
        self.send_authentication()
        return self

    def __exit__(self, exit_type, value, traceback):
        self.sock.close()

    def command(self, payload: str) -> str:
        if payload is None or payload == "":
            raise IllegalArgumentException("payload cannot be None")
        response = self.send(2, payload.encode('utf-8'))
        return response.decode('utf-8')

    def listen_chat(self) -> str:
        return listen(self.sock).payload.decode('utf-8')

    def send_authentication(self):
        global request_id
        request_id += 1
        return send_auth(self.sock, RconPacket(
            request_id=self.get_request_id(),
            type_id=3,
            payload=self.password.encode("utf-8")
        ))

    def send(self, type_id: int, payload: bytes) -> bytes:
        return send(self.sock,
                    RconPacket(
                        request_id=self.get_request_id(),
                        type_id=type_id,
                        payload=payload
                    )
                )

    @staticmethod
    def get_request_id():
        global request_id
        request_id += 1
        return request_id