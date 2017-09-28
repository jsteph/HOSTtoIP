import socket
import os
import time
def Main():
	os.system('clear')
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("\033[1;31mHOSTtoIP\033[0m\n")
	host = input("\033[31m> \033[0m")
	ip = socket.gethostbyname(host)
	print("\n"+"the ip of \033[1;31m"+host+"\033[0m is \033[1;31m"+ip+"\033[0m\n")
	time.sleep(1)
	print("\033[1;32myes\033[0m / \033[1;31mno\033[0m")
	option = input("find another ip? > ")
	if option == "yes":
		Main()
	if option == "no":
		exit()
	else:
		time.sleep(1)
		print("\033[1;31mERROR. NOW CLOSING\033[0m")
		exit()
if __name__ == '__main__':
	Main()
