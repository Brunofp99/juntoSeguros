# Documentação
Essa documentação tem como objetivo orientar e demonstrar como a API funciona
<h2>Ambiente virtual</h2>

Partindo do pressuposto de que você ja tem o Python3.7+ instalado na sua maquina (caso não tenha click no link: https://www.python.org/downloads/) e o repositorio clonado,
entre na pasta pelo seu editor de texto ou IDE e inicie o ambiente virtual que ja vem inatalado com o Python:

>$ python -m venv ambvir

Em seguida ative o seu ambinete virtual:

>$ ./bin/Scripts/Activate.bat

Caso esteja usando p PowerShell use:

>$ ./bin/Scripts/Activate.ps1

Caso seu PowerShell esteja com os scripts desabilitados, consulte a documentação para saber como proceder

<h2>Baixando dependências</h2>

Na raiz do projeto (com o ambiente virtual ativo) abra o terminal e digite o comando para atualizar o "pip":

>$ python -m pip install --upgrade pip

Em seguida instale todas as dependências do projeto que se encontram na pasta requirements.txt:

>$ pip install -r requirements.txt

Logo após o download das dependências use o comando:

>$ python app.py

Se tudo correu de forma correta a aplicação estará rodando:

>Running on http://127.0.0.1:5000/

<h2>API</h2>
Para testar os métodos POST e PUT, use o POSTMAN (link para download: https://www.postman.com/downloads/).

__A API aceita e retorna apenas o formato JSON__


<h3>Adicionar usuários</h3>

>POST http://127.0.0.1:5000/users/register

__Enviar JSON__:

````
{
    "login": "tesla@hotmail.com",
    "password": "eletromagnetismo",
    "city": "São paulo"
}
````

__Sucesso__:

````
{
    "message": "User cread successfully"
}
````

__Usuario já existe__:

````
{
    "massage": "The login tesla@hotmail.com alredy exists."
}
````

<h3>Geração de token</h3>

>POST http://127.0.0.1:5000/users/token

__Enviar JSON__
````
{
    "login": "tesla@hotmail.com",
    "password": "eletromagnetismo"
}
````

__Sucesso__:

````
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDA1NDE2MDEsIm5iZiI6MTYwMDU0MTYwMSwianRpIjoiY2IzNGJmNjQtNmM5ZS00MTg4LWJlMjUtYzgwNjhjNmI5NTlmIiwiZXhwIjoxNjAwNTQyNTAxLCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.g5lNkaKN5KQ_4-hPZRb9peWlENUygZt3Z-rKLyWF94g"
}
````

__Erro__:

````
{
    "message": "The user name or password is incorrect"
}
````

<h3>Listagem de usuarios</h3>

>GET http://127.0.0.1:5000/users

Retorna um JSON com todos os registros de usuarios

```
{
    "users": [
        {
            "id": 1,
            "login": "einstein@hotmail.com",
            "city": "Curitiba"
        },
        {
            "id": 2,
            "login": "newton@gmail.com",
            "city": "Curitiba"
        },
        {
            "id": 3
            "login": "tesla@hotmail.com",
            "city": "São paulo"
        }
     ]
}

```

<h4>Parâmetro(opcionais)</h4>

Filtragem por cidade:

>GET http://127.0.0.1:5000/users?city=curitiba

Filtragem por Quantidade:

>GET http://127.0.0.1:5000/users?limit=100&offset=0

Filtragem por cidade e quantidade:

>GET http://127.0.0.1:5000/users?city=curitiba&limit=100&offset=0

Retorna um JSON com todos os usuários filtrados pelos parâmetros

<h3>Pesquisar por "id" usuário</h3>

Para executar esse método precisaremos da token que foi gerada, após copiar a token entre na aba do POSTMAN "Headers" na coluna de "KEY" adicione a palavra
"Authorization" e na coluna "VALUE" adicione "Bearer" seguido pela token

__Exemplo__:

|     KEY        |          VALUE             |
|----------------|----------------------------|
|  Authorization | Bearer eyJ0eXAiOiJKV1Qi... |



>GET http://127.0.0.1:5000/users/{:id}


Retorna um JSON com "id", "login" e "city":

````
{
    "id": 3,
    "login": "tesla@hotmail.com",
    "city": "São paulo"
}
````


<h3>Alterar dados</h3>

Para executar esse método precisaremos da token que foi gerada, após copiar a token entre na aba do POSTMAN "Headers" na coluna de "KEY" adicione a palavra
"Authorization" e na coluna "VALUE" adicione "Bearer" seguido pela token

__Exemplo__:

|     KEY        |          VALUE             |
|----------------|----------------------------|
|  Authorization | Bearer eyJ0eXAiOiJKV1Qi... |


Os dados que podem ser alterados são: "login", "password", "city"

>PUT http://127.0.0.1:5000/users/alter/{:id}


__Enviar JSON (Todos os index são opcionais)__:

````
{
    "login": "nikolatesla@hotmail.com",
    "password": "correntealternada"
}
````

Retorna um JSON com as novas informações:

__Sucesso__:

````
{
    "id": 3
    "login": "nikolatesla@hotmail.com",
    "city": "São paulo"
}
````

__Erro__:

````
{
    "message": "this user id :id dont have a register"
}
````

<h3>Deletar Usuário</h3>

Para executar esse método precisaremos da token que foi gerada, após copiar a token entre na aba do POSTMAN "Headers" na coluna de "KEY" adicione a palavra
"Authorization" e na coluna "VALUE" adicione "Bearer" seguido pela token

__Exemplo__:

|     KEY        |          VALUE             |
|----------------|----------------------------|
|  Authorization | Bearer eyJ0eXAiOiJKV1Qi... |


>DELETE http://127.0.0.1:5000/users/{id}

Retorna um JSON com uma menssagem:

__Sucesso__:

````
{
    "message": "user deleted"
}
````

__Erro id não existe__:

````
{
    "message": "The user :id does not exist"
}
````

__Erro desconhecido__:

````
{
    "message": "An internal error ocurred trying to delete user"
}
````

<h3>Seguranças</h3>

* Usuários registrados tem obrigatoriamente que gerar token para executar ação de POST, PUT, DELETE.
* As senhas são salvas criptografadas no bancos, ou seja, apenas o usuário tem acesso a sua versão original.

