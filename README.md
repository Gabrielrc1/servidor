Gabriel Reis Costa - 2111508
Vanessa

OBS: Esse servidor foi criado em um ambiente virtual em python. Para fazer ele rodar siga as instruções abaixo:
1. Ative a virtualenv com o comando venv/Scripts/activate.
2. (CASO NECESSÁRIO) - baixe as dependências com o comando: pip install flask
3. Rode o comando no terminal para iniciar o servidor: python servidor.py

TESTANDO
1. No insomnia ou Postman configure uma requisição POST para http://127.0.0.1:5000/login.
2. No corpo da requisição (Body), escolha JSON e envie:
        {
            "login": "nome_usuario",
            "senha": "senha_usuário"
        }
        
