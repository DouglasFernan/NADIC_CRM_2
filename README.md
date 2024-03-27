# Instalação do NADIC CRM parte 2

Este guia contém instruções para configurar e executar o NADIC CRM em seu ambiente local.

## Requisitos:

Python instalado  

Git instalado

## Passo 1: Clonar o Repositório

Abra o Visual Studio Code ou outra IDE de sua preferência e navegue até a pasta em seu computador onde deseja instalar o projeto. Em seguida, execute o seguinte comando no terminal:  

`git clone https://github.com/DouglasFernan/NADIC_CRM_2`


## Passo 2: Instalar Dependências

Após clonar o repositório, entre na pasta recém-clonada que contém o arquivo `requirements.txt`. No terminal, digite o seguinte comando:  

`pip install -r requirements.txt`


## Passo 3: Executar o Servidor Local

Agora, entre na pasta `nadic_crm`, onde está localizado o arquivo `manage.py`. No terminal da sua IDE, execute o seguinte comando:

`python manage.py runserver`


Pronto! O servidor local deve estar em execução, e o terminal do Visual Studio Code ou da sua IDE mostrará o caminho para acessá-lo.

## Passo 4: Usuários e login  

Eu criei um super user com as seguintes credenciais:   
user: dougfernan    
password: ifrn.123   
Se desejar pode criar seu próprio superuser para testar as funcionalidades exigidas do projeto (como o endpoint faturamento ser disponível apenas para o usuário "Fundador" ):   

Criando superuser:  
`python manage.py createsuperuser`    


Com esse usuário você poderá fazer login em:   
`http://127.0.0.1:8000/admin`   
OBS: O servidor django tem que estar ativo  
  
  
Por padrão o superuser e usuários comuns não vem com o grupo "Fundador" então não terá acesso a rota faturamento/, mas como o superuser tem acesso ao admin você poderá conceder esse grupo a qualquer usuário:  
### Fazer login em admin/  
### Ir na página de "users"  
### Adicionar o grupo "Fundador" ao seu superuser  
### Salve as alterações  
E pronto, agora logado como superuser e que possui a credencial de "Fundador", entre na rota faturamento pelo link ou navegando pela navbar do site para testar se está funcionando corretamente. Teste também criando outro usuário comum para confirmar que ele não tem acesso ao endpoint faturamento, crie esse usuário comum nos templates normalmente.  
