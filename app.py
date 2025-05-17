from flask import Flask, request, render_template_string

valores_letras = {
    "a": 2.85, "b": 3.35, "c": 2.20, "d": 3.70,
    "e": 2.70, "f": 2.50, "g": 3.50, "h": 3.35,
    "i": 1.35, "j": 2, "k": 3, "l": 1.85, "m": 4.35,
    "n": 3.70, "o": 3.35, "p": 3, "q": 3.50, "r": 3.20,
    "s": 2.85, "t": 2, "u": 3, "v": 2.50, "w": 4.35,
    "x": 3, "y": 2.20, "z": 3.20
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    valor_total = None
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"].lower()
        valor_total = sum(valores_letras.get(letra, 0) for letra in nome)

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Valor do Nome</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #74ebd5, #acb6e5);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px 40px;
                border-radius: 10px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
                text-align: center;
                max-width: 400px;
                width: 90%;
            }
            h2 {
                color: #333;
                margin-bottom: 20px;
            }
            input[type="text"] {
                padding: 10px;
                width: 80%;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                margin-top: 15px;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #4CAF50;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            .resultado {
                margin-top: 20px;
                font-size: 18px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Calculadora de Valor do Nome</h2>
            <form method="post">
                <input type="text" name="nome" placeholder="Digite o nome" required>
                <br>
                <button type="submit">Calcular</button>
            </form>
            {% if valor_total is not none %}
                <div class="resultado">
                    O valor do nome "<strong>{{ nome }}</strong>" é <strong>R$ {{ "%.2f"|format(valor_total) }}</strong>.
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    """, valor_total=valor_total, nome=nome)
