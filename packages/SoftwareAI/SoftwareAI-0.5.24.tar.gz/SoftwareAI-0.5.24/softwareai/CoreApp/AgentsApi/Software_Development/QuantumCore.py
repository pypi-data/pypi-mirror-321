from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à aplicação Flask!"

@app.route('/hello/<nome>')
def hello(nome):
    return f"Olá, {nome}!"

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    resultado = dados['a'] + dados['b']
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)






