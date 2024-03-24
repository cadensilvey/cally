*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BASE_URL}       http://137.152.100.34:8551/cally/main-py
${BROWSER}        Chrome

*** Test Cases ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}

Test Full Eighteen Page
    [Documentation]    Tests the full_eighteen page functionality
    Go To             /create

    # Test entering par values for each hole
    : FOR    ${par}    IN    3    4    2    5    3    4    3    5    4    3    4    3    4    3    4    3    5
    \   Input Text    id:parTextField    $  {par}
    \   Click Button    Next Hole
    \   ${current_hole}    Get Text    xpath://span[contains(text(), 'Enter Par for Hole')]/following-sibling::input
    \   Should Be Equal As Numbers    ${current_hole}    ${par}

    # Test submitting the form
    Click Button    Submit Form
    ${submitted_pars}    Get Text    xpath://span[contains(text(), 'Submitted Pars')]/following-sibling::span
    Should Be Equal As Strings    ${submitted_pars}    ${par_list}

*** Keywords ***
Go To
    [Arguments]    ${url}
    Go To    ${url}
    Wait Until Page Contains Element    id:parTextField    timeout=10s
