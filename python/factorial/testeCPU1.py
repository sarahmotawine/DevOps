from flask import Flask, jsonify
import os
import math
import multiprocessing
import threading

app = Flask(__name__)

# Função para cálculos intensivos em CPU
def calculate_factorial():
    try:
        number_to_factorial = 1000000
        while True:
            result = math.factorial(number_to_factorial)
    except Exception as e:
        print(f"Erro nos cálculos: {e}")

# Rota de teste
@app.route('/test', methods=['GET'])
def health_check():
    try:
        # Calcula o fatorial de 1000
        factorial = math.factorial(1000)

        # Inicia uma thread para cálculos intensivos em CPU
        thread = threading.Thread(target=calculate_factorial)
        thread.start()

        # Retorna o resultado como uma resposta JSON
        return jsonify({'result': 'Hello, World!', 'factorial': factorial}), 200
    except Exception as e:
        # Se ocorrer uma exceção, imprima-a para diagnóstico
        print(f"Erro: {e}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)
