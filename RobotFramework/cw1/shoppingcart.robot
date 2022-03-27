*** Settings ***
Documentation    Add product to shopping cart
Library          SeleniumLibrary

*** Variables ***
${BROWSER}              chrome
${URL}                  https://www.mediaexpert.pl/

*** Test Cases ***
Adding product to shopping cart
    Open Shop Website
    Check Shopping Cart
    Add Product To Shopping Cart
    Check If Shoping Cart Contain Product
    Close Browser


*** Keywords ***
Open Shop Website
#    Set Selenium Speed          0.5
    Open Browser                ${URL}      ${BROWSER}
    Maximize Browser Window
Check Shopping Cart
    Click Element               //span[contains(text(),'Koszyk')]
    Element Text Should Be      //div[contains(text(),'Twój koszyk jest pusty')]  Twój koszyk jest pusty
Add Product To Shopping Cart
    Click Element                       //body/div[@id='spark']/div[3]/div[1]/div[1]/button[1]
    Click Element                       //header/div[@id='section_menu-bar']/div[@id='section_menu-categories']/div[@id='section_menu-list']/div[1]/ul[1]/li[1]/a[1]/span[1]
    Wait Until Page Contains Element    //body/div[@id='spark']/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/div[1]/img[1]
    click element                       //body/div[@id='spark']/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/div[1]/img[1]
    Wait Until Element Is Visible       //body/div[@id='spark']/div[3]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/span[1]/div[1]/div[2]/div[1]/div[4]/button[1]/span[1]
    Wait Until Page Contains            Do koszyka      2
    click element                       //body/div[@id='spark']/div[3]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/span[1]/div[1]/div[2]/div[1]/div[4]/button[1]/span[1]

Check If Shoping Cart Contain Product
    Reload Page
    Click Element                       //span[contains(text(),'Koszyk')]
    Wait Until Page Contains            KOD PRODUKTU    2
    Wait Until Page Contains Element    //span[contains(text(),'Kod produktu: 384264')]
    Element Text Should Be              //span[contains(text(),'Kod produktu: 384264')]  KOD PRODUKTU: 384264

