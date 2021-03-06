*** Settings***
Documentation   Suite dos testes de cadsatro

Resource        ../resources/base.robot

Test Setup      Open Session
Test Teardown   Close Session

***Test Cases***
Cadastro simples
    Dado que acesso a página principal
    Quando submeto o meu email "joao@gmail.com"
    Então devo ser autenticado


Email Incorreto
    Dado que acesso a página principal
    Quando submeto o meu email "joão&yahoo.com"
    Então devo ver a mensagem "Oops. Informe um email válido!"


Email não informado
    Dado que acesso a página principal
    Quando submeto o meu email "${EMPTY}"
    Então devo ver a mensagem "Oops. Informe um email válido!"