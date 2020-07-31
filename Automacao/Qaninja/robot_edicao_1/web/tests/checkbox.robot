*** Settings ***
Resource            base.robot

Test Setup          Nova sessão
Test Teardown       Encerra sessão

*** Variables ***
${check_thor}       id:thor      
${check_iron}       css:input[value='iron-man']
${check_panter}     Xpath://*[@id='checkboxes']/input[7]

*** Test Cases ***
Marcando opções com ID
    Go TO                               ${url}/checkboxes
    Select CheckBox                     ${check_thor}
    CheckBox Should Be Selected         ${check_thor}     

Marcando opção com CSS Selector
    Go TO                               ${url}/checkboxes
    Select CheckBox                     ${check_iron}
    CheckBox Should Be Selected         ${check_iron}

Marcando opção com Xpath
    [tags]      ironman
    Go TO                               ${url}/checkboxes
    Select CheckBox                     ${check_panter}
    CheckBox Should Be Selected         ${check_panter}

