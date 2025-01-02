import phonenumbers
from phonenumbers import geocoder
from colorama import init, Fore, Style
import pyfiglet
import os
import time

init()

# apagar tudo no comeco e amostrar a logo num-Tracker
os.system("clear")
logo = "num-Tracker"
resultado = pyfiglet.figlet_format(logo)
print(resultado)

# digitar um numero de telefone e se não tiver nada, imprime uma mensagem
numero = input(Fore.CYAN + "digite um numero de telefone: " + Style.RESET_ALL)
if not numero:
	print(Fore.YELLOW + "nenhum número digitado" + Style.RESET_ALL)
	exit()

# parsear o numero
num = phonenumbers.parse(numero)
time.sleep(3)

# imprime: localizaçao e diz a localização do numero
print(Fore.RED+ "\nlocalização:" + Style.RESET_ALL)
print(geocoder.description_for_number(num, 'pt'))
