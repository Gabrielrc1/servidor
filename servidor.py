from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'login' not in data or 'senha' not in data:
        return jsonify({"error": "Requisição inválida. Envie um JSON com 'login' e 'senha'."}), 400
    
    return jsonify({"login": data['login'], "senha": data['senha']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
