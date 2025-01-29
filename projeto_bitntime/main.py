from flask import Flask, render_template
from app.api_handler import checar_btc

app = Flask(__name__)

@app.route('/')
def home():
    preco_btc = checar_btc()  # Chama a função para obter o preço
    if preco_btc:
        return render_template('index.html', preco_btc=preco_btc)
    else:
        return "Erro ao obter o preço do Bitcoin", 500

if __name__ == '__main__':
    app.run(debug=True)
