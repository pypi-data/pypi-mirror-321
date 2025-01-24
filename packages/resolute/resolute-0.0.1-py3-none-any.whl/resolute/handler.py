from socket import socket

def _handle(sock: socket) -> None:
    try:
        sock.settimeout(1)

        sock.recv(4096)
        sock.sendall(b"HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: 11\r\n\r\nHello world")
    except:
        pass
    finally:
        sock.close()
