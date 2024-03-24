*** Settings ***
Library           SeleniumLibrary
Library           Dialogs

*** Variables ***
${BASE_URL}       http://137.152.100.34:8551/cally/main-py
${BROWSER}        Chrome

*** Test Cases ***
Test Create Course Calculation
    Open Browser    ${BASE_URL}/create    ${BROWSER}
    Maximize Browser Window

    # Manually input scores for each hole
    Input Scores Manually

    # Calculate the adjusted score
    Calculate Adjusted Score

    # Verify total score and callaway score
    Verify Total Score    89
    Verify Callaway Score    78

*** Keywords ***
Input Scores Manually
    [Documentation]    Manually input scores for each hole
    [Tags]    manual
    [Timeout]    10 seconds
    Wait Until Element Is Visible    id:score_label
    ${input_scores} =    Get Value From User    Enter scores for each hole (comma-separated):
    @{scores}    Create List    ${input_scores}
    FOR    ${score}    IN    @{scores}
        Input Text    id:score_label    ${score}
    END

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
