*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${BASE_URL}    http://137.152.100.34:8551/cally/main-py
${BROWSER}     Chrome
${EXPECTED_URL}    http://137.152.100.34:8551/cally/main-py/create

*** Test Cases ***
Test Navigation to Create Page
    Open Browser    ${BASE_URL}    ${BROWSER}
    [Documentation]    Manually press the "Play Golf" button and then run the test.
    [Tags]    manual
    Press Play Golf Button
    Wait Until Expected URL

*** Keywords ***
Press Play Golf Button
    [Documentation]    Wait for the user to manually press the "Play Golf" button.
    [Tags]    manual
    [Timeout]    5 minutes
    [RETURN]    Press any key to continue...
    [Teardown]    Log    Press any key to continue...

Wait Until Expected URL
    Press any key to continue...
    ${CURR_URL}=    Get Location
    Should Be Equal    ${EXPECTED_URL}    ${CURR_URL}
