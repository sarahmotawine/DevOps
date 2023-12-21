from flask import Flask, jsonify
import os
import math
import multiprocessing

app = Flask(__name__)

# ... (configuração do banco de dados e outras configurações)

@app.route('/consume_cpu', methods=['GET'])
def consume_cpu():
    try:
        # Número para calcular o fatorial (pode ajustar conforme necessário)
        number_to_factorial = 10000

        # Número de processos paralelos para aumentar a carga de trabalho
        num_processes = multiprocessing.cpu_count()

        # Executa cálculos intensivos em CPU em paralelo
        with multiprocessing.Pool(num_processes) as pool:
            result = pool.map(math.factorial, [number_to_factorial] * num_processes)

        return jsonify({'result': 'CPU consumption in progress!'}), 200

    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)