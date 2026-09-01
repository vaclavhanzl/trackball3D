
# This is just a dirty quick AI-made test to verify that Avogadro has rotate RPC,
# NOT an example how to do things. For a proper way, see:
# https://github.com/OpenChemistry/avogadrolibs/blob/master/python/avogadro/connect.py

import json
import os
import socket
import struct
import sys
import tempfile

# Match path resolution logic found in connect.py
SOCKET_PATH = os.path.join(tempfile.gettempdir(), "avogadro")


def rotate_with_framing(x_rot, y_rot, z_rot):
    if not os.path.exists(SOCKET_PATH):
        print(f"Error: Socket path '{SOCKET_PATH}' does not exist.")
        return False

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rotateScene",
        "params": {"x": float(x_rot), "y": float(y_rot), "z": float(z_rot)},
    }

    # Encode payload to bytes
    json_bytes = json.dumps(payload).encode("ascii")

    # 1. Generate the mandatory 4-byte big-endian length prefix header
    size = len(json_bytes)
    header = struct.pack(">I", size)

    # 2. Stitch the binary package together
    packet = header + json_bytes

    print(f"Connecting to Unix socket: {SOCKET_PATH}")
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.settimeout(2.0)
            client.connect(SOCKET_PATH)

            print(f"Sending framed rotation -> X:{x_rot}, Y:{y_rot}, Z:{z_rot}")
            client.sendall(packet)

            # Receive the response packet
            raw_response = client.recv(4096)
            if len(raw_response) >= 4:
                # Discard the first 4 bytes of server length header to parse JSON response cleanly
                response_json = json.loads(raw_response[4:].decode("ascii"))
                print("Server Response:", response_json)
            else:
                print("No parsable response returned from server.")
            return True

    except Exception as e:
        print(f"Communication failure: {e}")
        return False


if __name__ == "__main__":
    # Test values (multiplied internally by 0.005 speed coefficient)
    X_DELTA = 150.0
    Y_DELTA = 50.0
    Z_DELTA = 0.0

    success = rotate_with_framing(X_DELTA, Y_DELTA, Z_DELTA)
    sys.exit(0 if success else 1)
