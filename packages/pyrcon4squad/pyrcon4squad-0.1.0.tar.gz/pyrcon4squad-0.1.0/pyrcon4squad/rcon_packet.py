import socket
import struct

from pyrcon4squad.exceptions import MalformedPacketException


class RconPacket:
    def __init__(self, request_id: int, type_id: int, payload: bytes):
        self.request_id = request_id
        self.type_id = type_id
        self.payload = payload

def send(sock: socket.socket, packet: RconPacket) -> bytes:
    try:
        write(sock, packet.request_id, packet.type_id, packet.payload)
        write(sock, packet.request_id, 0, b"")
    except Exception as e:
        raise e

    last: bytes = b""
    output: bytes = read(sock).payload
    while len(output) != 0 and output is not None:
        last = last + output
        output = read(sock).payload
    return last


def send_auth(sock: socket.socket, packet: RconPacket):
    try:
        write(sock, packet.request_id, packet.type_id, packet.payload)
    except Exception as e:
        raise e

    read(sock)
    return read(sock)

def listen(sock: socket.socket) -> RconPacket:
    return read(sock)

def write(sock: socket.socket, request_id: int, type_id: int, payload: bytes):
    try:
        # Calculate lengths
        body_length = 10 + len(payload)  # request_id + packet_type + payload + padding

        # Pack the data
        buffer = struct.pack('<iii', body_length, request_id, type_id) + payload + b'\x00\x00'

        # Send the packet
        sock.sendall(buffer)
    except Exception as e:
        raise IOError("Failed to write RCON packet") from e

def read(sock: socket.socket) -> RconPacket:
    try:
        # Read the 12-byte header
        try:
            header = sock.recv(12)
        except Exception as e:
            return RconPacket(-1, -1, b'')
        if len(header) < 12:
            raise MalformedPacketException("Cannot read the whole packet header")

        # Unpack the header (LE: Little Endian)
        length, request_id, packet_type = struct.unpack('<iii', header)

        # Calculate payload length
        payload_length = length - 4 - 4 - 2
        if payload_length < 0:
            raise MalformedPacketException("Invalid packet length")

        # Read the payload
        payload = b''
        while len(payload) < payload_length:
            chunk = sock.recv(payload_length - len(payload))
            if not chunk:
                raise MalformedPacketException("Cannot read the whole payload")
            payload += chunk

        # Read the 2-byte padding
        padding = sock.recv(2)
        if len(padding) < 2:
            raise MalformedPacketException("Cannot read the 2-byte padding")

        return RconPacket(request_id, packet_type, payload)
    except (EOFError, struct.error) as e:
        raise MalformedPacketException("Cannot read the whole packet") from e
