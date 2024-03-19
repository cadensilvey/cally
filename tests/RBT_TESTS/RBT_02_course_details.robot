*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${BASE_URL}       http://137.152.100.34:8551/cally/main-py
${BROWSER}        Chrome
${DELAY}          1s

*** Test Cases ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}

Test Full Eighteen Page
    [Documentation]    Tests the full_eighteen page functionality
    Go To             /18

    # Test entering par values for each hole
    : FOR    ${par}    IN    3    4    2    5    3    4    3    5    4    3    4    3    4    3    4    3    5
    \   Input Text    id:parTextField    ${par}
    \   Click Button    Next Hole
    \   Sleep    ${DELAY}
    \   ${current_hole}    Get Text    xpath://span[contains(text(), 'Enter Par for Hole')]/following-sibling::input
    \   Should Be Equal As Numbers    ${current_hole}    ${par}
    \   ${total_par}    Get Text    xpath://span[contains(text(), 'Total Par')]
    \   Should Be Equal As Numbers    ${total_par}    ${par}

    # Test submitting the form
    Click Button    Submit Form
    Sleep    ${DELAY}
    ${submitted_pars}    Get Text    xpath://span[contains(text(), 'Submitted Pars')]
    Should Be Equal    ${submitted_pars}    [3, 4, 2, 5, 3, 4, 3, 5, 4, 3, 4, 3, 4, 3, 4, 3, 5]

*** Keywords ***
Go To
    [Arguments]    ${url}
    Go To    ${url}
    Sleep    ${DELAY}
