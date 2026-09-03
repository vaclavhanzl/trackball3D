
# test rotating Avogadro camera via RPC
# see: https://avogadro.cc/develop/rpc.html

import json
import socket
import struct
import tempfile

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(tempfile.gettempdir() + "/avogadro")

x_rot, y_rot, z_rot = 10.0, 20.0, 30.0

request = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "rotateScene",
    "params": {"x": float(x_rot), "y": float(y_rot), "z": float(z_rot)},
}).encode("utf-8")
sock.sendall(struct.pack(">I", len(request)) + request)

size = struct.unpack(">I", sock.recv(4))[0]
print(json.loads(sock.recv(size).decode("utf-8")))
