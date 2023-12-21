#Banco de dados com ID, USERNAME e EMAIL. Código com método GET.

from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configuração do banco de dados a partir de variáveis de ambiente
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '5432'),
    'user': os.environ.get('DB_USER', 'sarah'),
    'password': os.environ.get('DB_PASSWORD', 'sarah'),
    'database': os.environ.get('DB_DATABASE', 'sarah')
}

# Rota de teste
@app.route('/test', methods=['GET'])
def test():
    return 'Hello, World!', 200

# Rota para obter todos os usuários do banco de dados
@app.route('/users', methods=['GET'])
def get_users():
    connection = None
    cursor = None

    try:
        # Conectar ao banco de dados
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # Consultar a tabela 'users'
        cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()

        # Formatar os resultados como um dicionário
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'email': user[2],

                # Adicione mais campos conforme necessário
            }
            user_list.append(user_dict)

        return jsonify(user_list), 200

    except Exception as e:
        print(f"Erro ao obter usuários: {e}")
        return 'Erro interno do servidor', 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)