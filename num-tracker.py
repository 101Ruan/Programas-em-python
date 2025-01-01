import phonenumbers
from phonenumbers import geocoder
import os
from colorama import init, Fore, Style
import pyfiglet
import time

os.system("clear")
logo = 'num-tracker'
res = pyfiglet.figlet_format(logo)
print(res)

num = input(Fore.CYAN + "digite um numero de telefone: " + Style.RESET_ALL)
numero = phonenumbers.parse(num)
print(Fore.BLUE + "procurando localizacão..." + Style.RESET_ALL)
time.sleep(3)
print(Fore.RED + "localizacão do numero de telefone: " + Style.RESET_ALL)
print(geocoder.description_for_number(numero, "pt-br"))
