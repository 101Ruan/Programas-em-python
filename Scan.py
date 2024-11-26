from colorama import init, Fore, Style


ip = input(Fore.RED + "digite um ip: " + Style.RESET_ALL) # pede para você digitar um ip
if ip == '192.168.1.1': # se o ip for 192.168.1.1 ele entra
	print(Fore.BLUE + "você entrou no roteador :) " + Style.RESET_ALL) # imprime uma mensagem dizendo que você entrou no roteador
else:
	while True: # cria um loop imprimindo a mensagem você foi hackeado! :(
		print(Fore.GREEN + "você foi hackeado! :( " + Style.RESET_ALL)	
