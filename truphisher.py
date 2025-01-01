from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username}\n Password: {password}")
        return 'login efetuado com sucesso!'
    else:
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                input { display: block; margin: 10px auto; width: 200px; }
                h1 { display: block; margin: 10px auto; width: 100px; color: blue; }
                button { display: block; margin: 10px auto; width: 200px; color: #03a509; background-color: #323ff2; }
            </style>
            <meta charset="UTF-8">
            <title>Olá</title>
        </head>
        <body>
            <h1>Login</h1>
            <form method="POST">
                <input type="text" name="username" placeholder="username">
                <input type="password" name="password" placeholder="password">
                <button>Login</button>
            </form>
        </body>
        </html>
        """
        return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=True)
    