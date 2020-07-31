***Settings***

Documentation       Cadastro de produtos/pratos
...                 Sendo um cozinheiro amador
...                 Quero cadsatrar meus melhores pratos
...                 Para que e possa cozinha-los para outras pessoas


Resource        ../resources/base.robot

Test Setup      Login Session  papito@yahoo.com
Test Teardown   Close Session

***Variables***
&{nhoque}=      img=nhoque.jpg      nome=Nnhoque molho páprica      tipo=Massas     preco=20.00



***Test Cases***
Novo prato
    Dado que "${nhoque}" é um dos meus pratos
    Quando faço o cadastro desse item
    Então devo ver este prato no meu dashboard


*** comment ***
    O simbolo &{} representa um dicionário no robot frame work
    Com chave valor
    O simbolo ${} representa uma variável para o robot


