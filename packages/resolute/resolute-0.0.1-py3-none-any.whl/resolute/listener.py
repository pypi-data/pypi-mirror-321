from multiprocessing import Queue, Process
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from resolute.handler import _handle

def accept(host: str, port: int, queue: Queue):
	with socket(family=AF_INET, type=SOCK_STREAM) as sock:
		sock.bind((host, port))
		sock.listen(4096)
		while True:
			queue.put(sock.accept()[0], block=True, timeout=None)

def listen(host: str = "127.0.0.1", port: int = 8000):
	connQueue = Queue()
	Process(target=accept, args=(host, port, connQueue), daemon=True).start()
	while True:
		conn = connQueue.get(block=True, timeout=None)
		Thread(target=_handle, args=(conn,), daemon=True).start()
