*** Settings ***
Library           SeleniumLibrary
Library           Dialogs

*** Variables ***
${BASE_URL}       http://137.152.100.34:8551/cally/main-py
${BROWSER}        Chrome

*** Test Cases ***
Test Create Course Calculation
    Open Browser    ${BASE_URL}/create_course    ${BROWSER}
    Maximize Browser Window

    # Test Play Golf Button
    Input Scores Manually

    Calculate Adjusted Score
    Verify Total Score    89
    Verify Callaway Score    78

*** Keywords ***
Test Play Golf Button
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    id:play_golf_button    timeout=30s
    Click Element    id:play_golf_button

Input Scores Manually
    [Documentation]    Manually input scores for each hole
    [Tags]    manual
    [Timeout]    5 minutes
    # You can use the "Input Text" keyword to input scores manually for each hole
    # For example:
    # Input Text    xpath://input[contains(@class, 'score_label')]    5
    # Input Text    xpath://input[contains(@class, 'score_label')]    4
    # Add more "Input Text" steps for each hole
    ${input_scores} =    Get Value From User     
    @{scores}    Split String    ${input_scores}    ,
    :FOR    ${score}    IN    @{scores}
    \    Input Text    xpath://input[contains(@class, 'score_label')]    ${score}

Calculate Adjusted Score
    Wait Until Element Is Clickable    xpath://button[text()='Calculate Adjusted Score']
    Click Element    xpath://button[text()='Calculate Adjusted Score']

Verify Total Score
    [Arguments]    ${expected_score}
    Wait Until Element Is Visible    xpath://span[contains(@class, 'total_score_label')]
    ${actual_score}    Get Text    xpath://span[contains(@class, 'total_score_label')]
    Should Be Equal As Numbers    ${actual_score}    ${expected_score}

Verify Callaway Score
    [Arguments]    ${expected_score}
    Wait Until Element Is Visible    xpath://span[contains(@class, 'callaway_score_label')]
    ${actual_score}    Get Text    xpath://span[contains(@class, 'callaway_score_label')]
    Should Be Equal As Numbers    ${actual_score}    ${expected_score}
