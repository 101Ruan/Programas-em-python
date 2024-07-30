import socket

tcp_socket = None

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket TCP IPv4
    
    host = '127.0.0.1'  # Escuta em todas as interfaces de rede
    port = 9999

    tcp_socket.bind((host, port))  # Associa o socket ao endereço e porta especificados
    tcp_socket.listen(5)  # Habilita o socket para aceitar conexões, com um backlog de até 5 conexões pendentes

    print(f"Servidor escutando em {host}:{port}")

    while True:
        c, addr = tcp_socket.accept()  # Aguarda conexões de clientes
        print(f"Conexão de {addr[0]}:{addr[1]}")

        # Resposta HTTP com conteúdo HTML e CSS
        response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
                      <!DOCTYPE html>
                      <html>
                      <head>
                          <meta charset="UTF-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1.0">
                          <title>servidor socket</title>
                          <style>
                              body {
                                  font-family: Arial, sans-serif;
                                  background-color: #f0f0f0;
                                  margin: 20px;
                                  padding: 20px;
                                  text-align: center;
                              }
                              h1 {
                                  color: #333;
                                  text-shadow: 2px 2px #ddd;
                              }
                              p {
                                  color: #666;
                                  font-size: 18px;
                              }
                              .container {
                                  background-color: #fff;
                                  border-radius: 10px;
                                  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                  padding: 20px;
                                  max-width: 600px;
                                  margin: 0 auto;
                              }
                          </style>
                      </head>
                      <body>
                          <div class="container">
                              <h1>Bem-vindo ao Nosso Site!</h1>
                              <p>Este é um site de teste de hacking.</p>
                              <p>isso é um teste de um servidor socket em python para hackers </p>
                          </div>
                      </body>
                      </html>\r\n"""

        c.sendall(response.encode())  # Envia a resposta ao cliente
        c.close()  # Fecha a conexão com o cliente após a comunicação

except socket.error as e:
    print(f"Erro de socket: {e}")
finally:
    if tcp_socket:
        tcp_socket.close()  # Fecha o socket do servidor ao sair do loop
