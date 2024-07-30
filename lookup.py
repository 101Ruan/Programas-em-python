import whois

# pergunta o dominio alvo e consulta o whois
dominio = input("digite seu alvo: ")
whois_lookup = whois.whois(dominio)

# imprime as informacões no console
print(whois_lookup)
