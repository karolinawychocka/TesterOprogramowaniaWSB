*** Settings ***
Documentation       Open And Close Browser
Library             SeleniumLibrary

*** Variables ***
${BROWSER}          Chrome
${URL}              https://robotframework.org/

*** Test Cases ***
TestCase_001 Open And Close Browser
    Open Browser    ${URL}      ${BROWSER}
    Close Browser

*** Keywords ***



