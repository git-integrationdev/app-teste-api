# API REST com Flask

Este é um projeto template de uma API REST usando Flask que demonstra como criar endpoints para processar dados JSON e retornar respostas formatadas.

## Estrutura do Projeto

- `app.py`: Aplicação principal Flask com o endpoint de exemplo
- `Dockerfile`: Configuração para containerização da aplicação

## Endpoint de Exemplo

### POST /api/welcome

Recebe um JSON com nome e email e retorna uma mensagem de boas-vindas.

**Requisição:**
```json
{
    "nome": "Exemplo",
    "email": "exemplo@email.com"
}
```

**Resposta:**
```json
{
    "response": "Olá Exemplo, confirma seu e-mail exemplo@email.com?"
}
```

## Como Executar

### Localmente

1. Instale as dependências:
   ```
   pip install flask
   ```

2. Execute a aplicação:
   ```
   python app.py
   ```

### Com Docker

1. Construa a imagem:
   ```
   docker build -t flask-api .
   ```

2. Execute o container:
   ```
   docker run -p 5000:5000 flask-api
   ```

## Como Adaptar para Novos Endpoints

1. No arquivo `app.py`, use o endpoint existente como template
2. Crie uma nova rota usando o decorador `@app.route`
3. Defina o método HTTP desejado
4. Adapte a lógica de processamento conforme necessário

Exemplo de novo endpoint:

```python
@app.route('/api/novo-endpoint', methods=['POST'])
def novo_endpoint():
    data = request.get_json()
    # Processe os dados conforme necessário
    return jsonify({'response': 'Nova resposta'})
```

## Testando a API

Você pode testar a API usando curl:

```bash
curl -X POST http://localhost:5000/api/welcome \
     -H "Content-Type: application/json" \
     -d '{"nome":"Teste","email":"teste@email.com"}'
```