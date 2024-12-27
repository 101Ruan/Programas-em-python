import socket
import time
from colorama import init, Fore, Style

host = "192.168.1.39"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input(Fore.BLUE + "digite a mensagem: " + Style.RESET_ALL).encode()

print(Fore.CYAN + "enviando mensagem em 5s..." + Style.RESET_ALL)
time.sleep(5)

print(Fore.GREEN + "mensagem enviada com sucessso!" + Style.RESET_ALL)
time.sleep(3)
for i in range(1,10000):
    try:
       s.sendto(mensagem, (host, port))

       print(Fore.RED + f'mensagem enviada {mensagem.decode()}' + Style.RESET_ALL)
       time.sleep(0.01)
    except Exception as e:
        print(f"erro {e}")
        break
        
