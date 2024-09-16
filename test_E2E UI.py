from selene import browser, be, have

def test():
    browser.open('https://saucedemo.com')
    browser.element('[name="user-name"]').should(be.blank).type('standard_user')
    browser.element('[name="password"]').should(be.blank).type('secret_sauce').press_enter()
    browser.element('[class="inventory_item_name "]').click()
    browser.element('[class="btn btn_primary btn_small btn_inventory"]').click()
    browser.element('[class="shopping_cart_link"]').click()

    browser.element('[class="inventory_item_name"]').should(have.text('Sauce Labs Backpack'))

    browser.element('[class="btn btn_action btn_medium checkout_button "]').click()

    browser.element('[name="firstName"]').should(be.blank).type('something')
    browser.element('[name="lastName"]').should(be.blank).type('something to')
    browser.element('[name="postalCode"]').should(be.blank).type('1234')

    browser.element('[class="submit-button btn btn_primary cart_button btn_action"]').click()
    browser.element('[class="btn btn_action btn_medium cart_button"]').click()

    browser.element('[class="complete-header"]').should(have.text('Thank you for your order!'))
