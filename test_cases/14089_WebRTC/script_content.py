{"id": 117258, "created": "2022-03-14T11:26:54Z", "updated": "2022-03-25T10:13:27Z", "project_id": 10571, "file_type": "test_script", "content": "def test_on_loadero(driver: TestUIDriver):\n    print(tdlpage(driver))\ndef tdlpage(driver: TestUIDriver) -> str:\n    url=\"https://www.testdevlab.com/\"\n\n    # Selectors\n    accept_btn=\"#root > div > div.cookies-message > button.cta-btn.no-select\"\n    solutions_menu=\"#root > div > div:nth-child(1) > nav > div.menu > div.sections > div:nth-child(2)\"\n    qa_consultancy=\"#root > div > div:nth-child(1) > nav > div.menu > div.sections > div:nth-child(2) > div.menu-block > div > div.links > div.link-col.left > div:nth-child(1) > a > div.link-name.cut-text.no-select\"\n    contact_us_btn=\"#root > div > div:nth-child(1) > nav > div.menu > div.right-side > a\"\n    first_name = '#firstName'\n    last_name = '#lastName'\n    email = '#email'\n    company = '#company'\n    message = '#message'\n\n    # Inputs\n    fn=\"Teodora\"\n    ln=\"Jovcheska\"\n    em=\"jovcheskateodora@gmail.com\"\n    comp=\"TDL\"\n    mess=\"Hello\"\n\n    driver.navigate_to(url)\n\n    driver.e(\"css\", accept_btn).wait_until_visible().click()\n\n    driver.e(\"css\", solutions_menu).wait_until_visible().click()\n\n    driver.e(\"css\", qa_consultancy).wait_until_visible().click()\n\n    driver.e(\"css\", contact_us_btn).wait_until_visible().click()\n\n    driver.e(\"css\", first_name).wait_until_visible().send_keys(fn)\n\n    driver.e(\"css\", last_name).wait_until_visible().send_keys(ln)\n\n    driver.e(\"css\", email).wait_until_visible().send_keys(em)\n\n    driver.e(\"css\", company).wait_until_visible().send_keys(comp)\n\n    driver.e(\"css\", message).wait_until_visible().send_keys(mess)\n\n    driver.save_screenshot(\"contact_us_page.png\")"}