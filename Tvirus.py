from colorama import init, Fore, Style
import os

init()

virus_achados = input(Fore.RED + "- Nome do arquivo: " + Style.RESET_ALL)

try:
    with open(virus_achados, "r") as file:
        conteudo = file.read()
        malwares_nomes = ["worm", "trojan", "ramsomware", "spyware"]
        achados = [nome for nome in malwares_nomes if nome in conteudo.lower()]
        
        if achados:
            print(Fore.YELLOW + f"- Malwares detectados no arquivo {virus_achados}:" + Style.RESET_ALL)
            for malwares in achados:
                print(Fore.BLUE + f"- {malwares}" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"- Nenhum malware detectado no arquivo {virus_achados}." + Style.RESET_ALL)
except FileNotFoundError:
    print(Fore.RED + f"- Arquivo '{virus_achados}' não encontrado." + Style.RESET_ALL)
except PermissionError:
    print(Fore.RED + f"- Acesso negado ao arquivo '{virus_achados}'." + Style.RESET_ALL)
except Exception as e:
    print(Fore.RED + f"- Erro: {str(e)}" + Style.RESET_ALL)
    
