import socket
import re
import sys

if __name__ == '__main__':
	print("""Availible commands:
		open {port}
		close {port}
		exit

		Example:
		open 1234
		""")
	ports = dict()
	while True:
		command = input("hope, you know what to do:\n")
		if re.fullmatch("open \d+", command):
			try:
				port = command[5:]
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.bind((socket.gethostname(), int(port)))
				s.listen(1)
				ports[port] = s
			except OSError:
				print("Address already in use by other program, use another")
		elif re.fullmatch("close \d+", command):
			try:
				port = command[6:]
				ports[port].close()
				del ports[port]
			except KeyError:
				print("you haven't open socket on this port")
		elif command == "exit":
      print("bye")
			sys.exit()
		else:
			print("omg, r u serious?")

