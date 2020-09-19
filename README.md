# Documentação
Essa documentação tem como objetivo orientar e demonstrar como a API funciona
<h2>Ambiente virtual</h2>

Partindo do pressuposto de que você ja tem o Python3.7+ instalado na sua maquina (caso não tenha click no link: https://www.python.org/downloads/) e o repositorio clonado,
entre na pasta e inicie o ambiente virtual que ja vem inatalado com o Python:

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

Se tudo correu de forma correta a aplicação estara rodando:

>Running on http://127.0.0.1:5000/

<h2>API</h2>
Para testar os métodos POST e PUT, use o POSTMAN (link para download: https://www.postman.com/downloads/).

__A API aceita e retorna apenas o formato JSON__
<h3>Listagem de usuarios<h3>



