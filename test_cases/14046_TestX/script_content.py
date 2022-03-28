def test_on_loadero(driver: TestUIDriver):
    print(tdlpage(driver))
def tdlpage(driver: TestUIDriver) -> str:
    url="https://www.testdevlab.com/"

    # Selectors
    accept_btn="#root > div > div.cookies-message > button.cta-btn.no-select"
    solutions_menu="#root > div > div:nth-child(1) > nav > div.menu > div.sections > div:nth-child(2)"
    qa_consultancy="#root > div > div:nth-child(1) > nav > div.menu > div.sections > div:nth-child(2) > div.menu-block > div > div.links > div.link-col.left > div:nth-child(1) > a > div.link-name.cut-text.no-select"
    contact_us_btn="#root > div > div:nth-child(1) > nav > div.menu > div.right-side > a"
    first_name = '#firstName'
    last_name = '#lastName'
    email = '#email'
    company = '#company'
    message = '#message'

    # Inputs
    fn="Teodora"
    ln="Jovcheska"
    em="jovcheskateodora@gmail.com"
    comp="TDL"
    mess="Hello"

    driver.navigate_to(url)

    driver.e("css", accept_btn).wait_until_visible().click()

    driver.e("css", solutions_menu).wait_until_visible().click()

    driver.e("css", qa_consultancy).wait_until_visible().click()

    driver.e("css", contact_us_btn).wait_until_visible().click()

    driver.e("css", first_name).wait_until_visible().send_keys(fn)

    driver.e("css", last_name).wait_until_visible().send_keys(ln)

    driver.e("css", email).wait_until_visible().send_keys(em)

    driver.e("css", company).wait_until_visible().send_keys(comp)

    driver.e("css", message).wait_until_visible().send_keys(mess)

    driver.save_screenshot("contact_us_page.png")