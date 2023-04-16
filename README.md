<h1 align="center">
 <img src="https://github.com/ipedromotta/VueJS-Flask/blob/main/frontend/src/assets/logo-python.png" width="50"><br>Sistema para gerenciamento de atividades e avaliações
</h1>

## :page_facing_up: Sobre #
Neste sistema, o professor pode cadastrar atividades e registrar avaliações que serão ou foram aplicadas presencialmente na universidade. Assim, o reitor terá mais dados para melhorar os indices da universidade

## :wrench: Configuração do projeto #
Para a inicialização do sistema é necessário ativar o ambiente virtual Pipenv ( Caso não possua basta usar o comando ```pip install pipenv``` )<br>
Dentro do diretório raiz do projeto utilize o comando a seguir para ativar o ambiente virtual:
```
pipenv shell
```
Após ativar o ambiente virtual, instale as dependencias com o seguinte comando:
```
pipenv install --dev
```
Agora você está com o ambiente virtual ativado e configurado, agora é preciso configurar o projeto django.<br>
Utilize o seguinte comando para criar novas migrações para alterar ou criar a estrutura do banco de dados:
```
python manage.py makemigrations
```
Em seguida, utilize o seguinte comando para criar as tabelas:
```
python manage.py migrate
```
Agora já está tudo configurado, para subir o servidor basta executar o seguinte comando:
```
python manage.py runserver
```
Agora a aplicação já está rodando na porta <a href="http://localhost:8000/">http://localhost:8000/</a><br>

- Pacotes <strong>Django</strong> utilizados: <br>
```django-crispy-forms``` Para criar layouts reutilizáveis programáticos a partir de componentes <br>
```django-braces``` Facilitador para gerenciamento de acesso as views <br>
```django-cleanup``` Atualiza/exclui automaticamente arquivos FileField, ImageField e suas subclasses <br>

- Pacotes <strong>JavaScript</strong> utilizados: <br>
```JQuery``` Facilitador JS que simplifica a manipulação do DOM e o gerenciamento de eventos em páginas web<br>
```JQueryMask``` Para fazer máscaras em campos de formulário <br>
```DataTables``` Uma biblioteca JQuery que adiciona recursos avançados em tabelas <br>

## 🛠️ Tecnologias utilizadas #

Para o desenvolvimento desse projeto foram utilizadas as seguintes tecnologias:

* Django;
* Bootstrap;
* JavaScript.
