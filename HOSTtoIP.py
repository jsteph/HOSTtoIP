
import socket
import os
import time
def Main():
	os.system('cls')
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("HOSTtoIP")
	host = input("> ")
	ip = socket.gethostbyname(host)
	print("\n"+"the ip of "+host+" is "+ip+"\n")
	time.sleep(1)
	print("yes / no")
	option = input("find another ip? > ")
	if option == "yes":
		Main()
	if option == "no":
		exit()
	else:
		time.sleep(1)
		print("ERROR. NOW CLOSING")
		exit()
if __name__ == '__main__':
	Main()