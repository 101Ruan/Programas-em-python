import time
from colorama import Fore, Style, init

# iniciar o colorama
init()

# pede pra aguardar 5s e inicia o atack ddos falso
def ddos(target_ip, target_port):
    print(Fore.CYAN + f"aguarde 5s para iniciar o atack" + Style.RESET_ALL)
    time.sleep(5)
    print(Fore.GREEN + "atack iniciado com sucesso" + Style.RESET_ALL)
    
# loop infinito while que fala pacote enviado para o ip e a porta
    while True:
        print(Fore.RED + f"pacote enviado para {target_ip}:{target_port}" + Style.RESET_ALL)
        time.sleep(0.3)
     
# pergunta o ip e a porta   
target_ip = input(Fore.BLUE + "digite o ip do destino: " + Style.RESET_ALL)
target_port = input(Fore.BLUE +"digite a porta do destino: " + Style.RESET_ALL)

# iniciar o ddos corretamente e o fin
ddos(target_ip, target_port)
