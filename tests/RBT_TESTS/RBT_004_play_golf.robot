*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${BASE_URL}       http://137.152.100.34:8551/cally/main-py
${BROWSER}        Chrome

*** Test Cases ***
Test Play Golf Button
    
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    class:play-golf-button-class



    # Wait Until Page Contains    Enter Score for Hole 1
