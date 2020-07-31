*** Settings ***
Resource            base.robot

Test Setup          Nova sessão
Test Teardown       Encerra sessão

*** Test Cases ***
Selecionar por tesxto e validar pelo valor
    Go TO                           ${url}/dropdown
    Select From List By Label       class:avenger-list          Scott Lang
    ${selected}=                    Get Selected List Value     class:avenger-list
    Should Be Equal                 ${selected}                 7

Selecionar pelo valor e validar pelo texto
    GO TO                           ${url}/dropdown
    Select From List By Value       id:dropdown                 6
    ${selected}=                    Get Selected List Label     id:dropdown
    Should Be Equal                 ${selected}                 Loki


*** comment ***
O simbolo ${} cria uma variavel 