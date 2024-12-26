import socket
import time
from colorama import init, Fore, Style

host = '192.168.1.1'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(Fore.BLUE + "enviando mensagem em 2s..." + Style.RESET_ALL)
time.sleep(2)

for i in range(1, 10000):
		try:
			mensagem = "ola".encode()
			s.sendto(mensagem, (host, port))	
			print(Fore.RED + "mensagem enviada" + Style.RESET_ALL)
			time.sleep(0.02)
		except Exception as e:
				print(f"erro {e}")
				break
	
