*** Settings ***

Resource    base.robot

Test Setup          Nova sessão
Test Teardown       Encerra sessão

*** Test Cases ***
Verifica o valor ao informar o numero da linha
    Go TO                           ${url}/tables
    Table Row Should Contain        id:actors   1   @robertdowneyjr

Descobre a linha pelo texto chave e valida os demais valores
    Go TO              ${url}/tables
    ${target}=         Get WebElement          xpath:.//tr[contains(.,'@chadwickboseman')]
    Log                ${target.text}
    Log To Console     ${target.text}
    Should Contain     ${target.text}          $ 700.000
    Should Contain     ${target.text}          Pantera Negra




*** comment ***
A função Table Row Should Contain valida de acordo com a linha especificada
No exemplo acima ele verifica se na linha 1 da tabela actors instagram corresponde

Get WebElement em conjunto com xpath retorna a linha inteira da tabela que o 
xpath localizou, no caso o a linha que contem o texto @chadwickboseman

A linha é armazenada na variável target, assim mais de um valor pode ser validado 
sem fazer outra busca na pagina.