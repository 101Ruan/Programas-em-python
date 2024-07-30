import requests
from colorama import Fore, Style  # Biblioteca para colorir a saída no terminal
import re

def print_header(title):
    length = len(title) + 4
    print(f"{Fore.YELLOW}{'=' * length}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}= {title} ={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * length}{Style.RESET_ALL}")

def check_headers(url):
    if not re.match(r'^https?://', url):
        url = 'http://' + url  # Adiciona http:// se não estiver presente
    try:
        response = requests.get(url)
        print_header(f"Headers para {url}")
        for header, value in response.headers.items():
            print(f"{Fore.CYAN}{header}:{Style.RESET_ALL} {value}")

        extract_personal_info(response.text)  # Chamando função para extrair informações pessoais
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Erro ao acessar {url}:{Style.RESET_ALL} {e}")

def extract_personal_info(html_content):
    # Aqui você pode definir padrões de expressões regulares para extrair informações pessoais
    # Exemplo simples: buscando por endereços de e-mail
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, html_content)
    
    if emails:
        print_header("Informações Pessoais Encontradas")
        for email in emails:
            print(f"{Fore.GREEN}Email encontrado:{Style.RESET_ALL} {email}")

if __name__ == "__main__":
    print(f"{Fore.GREEN}Bem-vindo ao verificador de headers HTTP!{Style.RESET_ALL}")
    url = input(f"{Fore.WHITE}Digite a URL para verificar os headers HTTP: {Style.RESET_ALL}")
    check_headers(url)
