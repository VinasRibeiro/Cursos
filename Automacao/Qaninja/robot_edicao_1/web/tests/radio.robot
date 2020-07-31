*** Settings ***

Resource    base.robot

Test Setup          Nova sessão
Test Teardown       Encerra sessão

*** Test Cases ***
Selecionando por ID

    Go TO                               ${url}/radios
    Select Radio Button                 movies      cap
    Radio Button Should Be Set TO       movies      cap

Selecionando por Value

    Go TO                               ${url}/radios
    Select Radio Button                 movies      guardians
    Radio Button Should Be Set TO       movies      guardians


*** comment ***

O select Radion Button usa o grupo 
do radio button para encontrar o elemento
ele funciona com id e values