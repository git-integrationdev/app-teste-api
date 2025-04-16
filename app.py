from flask import Flask, request, jsonify

# Criação da aplicação Flask
app = Flask(__name__)

# Endpoint POST para processar nome e email
# Este endpoint pode ser usado como template para criar outros endpoints similares
@app.route('/api/welcome', methods=['POST'])
def welcome():
    # Recebe o JSON da requisição
    data = request.get_json()
    
    # Extrai os campos nome e email
    # Você pode adaptar esta parte para extrair outros campos conforme necessário
    nome = data.get('nome')
    email = data.get('email')
    
    # Valida se os campos obrigatórios estão presentes
    if not nome or not email:
        return jsonify({'error': 'Nome e email são obrigatórios'}), 400
    
    # Monta a mensagem de resposta
    # Modifique esta lógica conforme necessário para outros endpoints
    mensagem = f'Olá {nome}, confirma seu e-mail {email}?'
    
    # Retorna a resposta no formato especificado
    return jsonify({'response': mensagem})

# Configuração para executar a aplicação
if __name__ == '__main__':
    # Host '0.0.0.0' permite acesso externo ao container
    # Debug True ativa o modo de desenvolvimento
    app.run(host='0.0.0.0', port=5003, debug=False, threaded=True, use_reloader=True)
