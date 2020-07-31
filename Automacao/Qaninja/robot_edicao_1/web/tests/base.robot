*** Settings ***
Library     SeleniumLibrary



*** Variables ***
${url}              https://training-wheels-protocol.herokuapp.com



*** KeyWord ***
Nova sessão
    Open Browser                        ${url}      chrome

Encerra sessão
    Capture Page Screenshot
    Close Browser