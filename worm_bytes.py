import os

def corromper_arquivo():
    try:
        tamanho_inicial = os.path.getsize("arquivo")
        with open("arquivo", 'a') as arquivo:
            arquivo.write('\0' * 10000)
        tamanho_final = os.path.getsize("arquivo")
        print(f"Arquivo corrompido com sucesso! Tamanho inicial: {tamanho_inicial} bytes. Tamanho final: {tamanho_final} bytes.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

corromper_arquivo()
