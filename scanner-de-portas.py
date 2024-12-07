# importa a biblioteca socket e colorama
import socket
from colorama import init, Fore, Style

# ip do alvo
alvo = "192.168.1.2"
		
# varre das portas 1 até 1025
for porta in range(1, 1025):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um socket para conexão tcp
	
	# define o tempo de conexão
	sock.settimeout(1)
	
	# verifica as portas abertas
	if sock.connect_ex((alvo, porta)) == 0:
		print(Fore.GREEN + f"portas abertas: {porta}" + Style.RESET_ALL) # imprime as portas abertas
			
	sock.close() # fecha o socket
