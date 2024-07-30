from flask import Flask, request, render_template_string
import whois

app = Flask(__name__)

# HTML template com CSS e conteúdo em português
HTML_TEMPLATE = '''
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Whois-lookup.com</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #0056b3;
        }
        form {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            background-color: #0056b3;
            color: #fff;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #004494;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #0056b3;
            color: #fff;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Consulta Whois</h1>
        <form method="post">
            <input type="text" id="domain" name="domain" placeholder="Digite o domínio" required>
            <input type="submit" value="Consultar">
        </form>
        {% if result %}
        <table>
            <tr><th>Campo</th><th>Valor</th></tr>
            {% for key, value in result.items() %}
            <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
            {% endfor %}
        </table>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        domain_name = request.form['domain']
        try:
            domain = whois.whois(domain_name)
            result = {
                "Nome do Domínio": domain.domain_name or "N/A",
                "Registrador": domain.registrar or "N/A",
                "Data de Criação": domain.creation_date or "N/A",
                "Data de Expiração": domain.expiration_date or "N/A",
                "Servidores DNS": ", ".join(domain.name_servers) if domain.name_servers else "N/A"
            }
        except Exception as e:
            result = {"Erro": str(e)}
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    