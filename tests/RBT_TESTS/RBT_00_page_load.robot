*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    http://137.152.100.34:8551/cally/main-py
${BROWSER}     Chrome

*** Test Cases ***
Test Page Load
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://div[@id='loading'][not(@style='display: block;')]
    [Teardown]    Close Browser
