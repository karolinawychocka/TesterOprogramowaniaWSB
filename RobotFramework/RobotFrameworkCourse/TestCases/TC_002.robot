*** Settings ***
Documentation       Open And Close Browser
Library             SeleniumLibrary

*** Variables ***
${BROWSER}          Chrome
${URL}              https://www.thetestingworld.com/index.php?option=com_users&view=registration

*** Test Cases ***
Input text
    Open Browser    ${URL}      ${BROWSER}
    Maximize Browser Window
#   Input Text              name:jform[name]                        TesterOprogramowania
    Input Text              xpath://input[@name='jform[name]']      TesterOprogramowania
    Input Text              xpath://input[@id="jform_username"]     TestowyLogin
    Clear Element Text      name:jform[name]
    Close Browser

*** Keywords ***
