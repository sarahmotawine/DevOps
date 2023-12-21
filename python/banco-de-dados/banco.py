#Banco de dados com ID, USERNAME, EMAIL, NUMBER E CPF. Código com o método GET e POST.

from flask import Flask, jsonify, request
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
    return 'Version 1.0', 200

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
        cursor.execute('SELECT * FROM users ORDER BY id;')
        users = cursor.fetchall()

        # Formatar os resultados como um dicionário
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'number': user[3],  # Adicione a coluna 'number'
                'cpf': user[4],     # Adicione a coluna 'CPF'

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

# Rota para cadastrar um novo usuário
@app.route('/register', methods=['POST'])
def create_user():
    connection = None
    cursor = None

    try:
        # Conectar ao banco de dados
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # Obter dados do JSON da requisição
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        number = data.get('number')  # Novo campo 'number'
        cpf = data.get('cpf')        # Novo campo 'CPF'

        # Inserir novo usuário na tabela 'users'
        cursor.execute('INSERT INTO users (username, email, number, cpf) VALUES (%s, %s, %s, %s) RETURNING id;',
                       (username, email, number, cpf))
        new_user_id = cursor.fetchone()[0]

        # Commit da transação
        connection.commit()

        return jsonify({'id': new_user_id}), 201  

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return f'Erro interno do servidor: {e}', 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
