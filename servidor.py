import socket

html = """

"""

def start_server():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 8089))
    servidor.listen()

    print("Servidor iniciado em http://127.0.0.1:8089")

    while True:
        conexao, endereco = servidor.accept()
        conexao.send(b"HTTP/1.1 200 OK\r\n")
        conexao.send(b"Content-Type: text/html\r\n\r\n")
        conexao.sendall(html.encode())
        print(f"conexão estabelecida: {endereco}")

        
        dados = conexao.recv(1024).decode()
       
        if "username=" in dados and "password=" in dados:
            username = dados.split("username=")[1].split("&")[0]
            password = dados.split("password=")[1].split("&")[0]
            print(f"Usuário: {username}, Senha: {password}")

        conexao.close()

start_server()
