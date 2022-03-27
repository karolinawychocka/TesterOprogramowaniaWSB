*** Settings ***
Documentation       Buttons testing
Library             SeleniumLibrary

*** Variables ***
${BROWSER}          Chrome
${URL}              https://abstracta.us/industries/ecommerce

*** Test Cases ***
Buttons testing
    Open Browser    ${URL}      ${BROWSER}
    Maximize Browser Window
    Input Text         xpath://input[@id="fullname"]       TesterOprogramowania
#   Select Checkbox    //label[@id='label_field_34']
    Click link         //body/section[@id='featured-insights']/div[2]/div[1]/a[1]
    Click button       //button[contains(text(),'Send me news')]


*** Keywords ***

