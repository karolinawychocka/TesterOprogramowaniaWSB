*** Settings ***
Documentation    Add product to shopping cart
Library          SeleniumLibrary

*** Variables ***
${BROWSER}              chrome
${URL}                  https://www.housebrand.com/pl/pl/

*** Test Cases ***
Adding product to shopping cart
    Open Shop Website
    Check Shopping Cart
    Add Product To Shopping Cart
    Close Browser


*** Keywords ***
Open Shop Website
    Set Selenium Speed          0.5
    Open Browser                ${URL}      ${BROWSER}
    Maximize Browser Window
Check Shopping Cart
    Click Element               //button[@id='cookiebotDialogOkButton']
    Click Element               //page-header/div[2]/div[1]/div[2]/mini-cart[1]/button[1]
    Element Text Should Be      //h1[contains(text(),'Twój koszyk jest pusty')]  Twój koszyk jest pusty
Add Product To Shopping Cart
    Click Element                       //span[contains(text(),'Ona')]
    Click Element                       //page-header/div[2]/div[1]/tree-menu[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]
    click element                       //body/div[@id='bottom_page']/section[@id='category']/main[@id='app']/div[1]/div[2]/div[1]/section[1]/article[3]/figure[1]/div[1]/h3[1]/a[1]