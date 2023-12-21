from flask import Flask, jsonify
import os
import math

app = Flask(__name__)

# Rota de teste
@app.route('/test', methods=['GET'])
def health_check():
    try:
        # Calcula o fatorial de 1000
        factorial = math.factorial(1000)

        # Retorna o resultado como uma resposta JSON
        return jsonify({'result': 'Hello, World!', 'factorial': factorial}), 200
    except Exception as e:
        # Se ocorrer uma exceção, imprima-a para diagnóstico
        print(f"Erro: {e}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)
