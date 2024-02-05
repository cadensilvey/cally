*** Settings ***
Library    Process
Library    OperatingSystem

*** Variables ***
${python3 Executable}    python3    
${Script Path}    /Users/cadensilvey/Developer/GitHub/Courses/Cally/callyScore.py

*** Test Cases ***
Test Golf Scoring
    [Documentation]    Calculate Callaway Score Based on hard coded data. 
    [Tags]    golf

    # Run callyScore to determine the callaway score calcualtion

    ${result}    Run Process    ${python3 Executable}    ${Script Path}    DressForLess
    Log    ${result.stdout}    # Log the script's output

    ${result}    Run Process    ${python3 Executable}    ${Script Path}    DriveNThriive
    Log    ${result.stdout}

    ${result}    Run Process    ${python3 Executable}    ${Script Path}    Osama
    Log    ${result.stdout}

    ${result}    Run Process    ${python3 Executable}    ${Script Path}    GG
    Log    ${result.stdout}

    ${result}    Run Process    ${python3 Executable}    ${Script Path}    DaddysMoney
    Log    ${result.stdout}
