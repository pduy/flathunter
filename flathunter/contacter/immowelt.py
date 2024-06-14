EXAMPLE_URL = "https://www.immowelt.de/expose/2e5n45s"
CONTACT_BUTTON_TITLE = "Anbieter kontaktieren"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


def contact_using_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/home/duypham/.config/google-chrome")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    # EXPORTED FROM SELENIUM IDE, cannot proceed because of the cookies banner
    # which blocks the contact form (id=usercentrics-root, real button ID concealed)
    element = driver.find_element(By.CSS_SELECTOR, "#btnContactBroker .btn__content")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, ".sd-ripple")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, "#btnContactBroker > .btn").click()
    element = driver.find_element(By.CSS_SELECTOR, ".sd-ripple")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.ID, "dropdown_input_salutation").click()
    driver.find_element(By.CSS_SELECTOR, "sd-dropdown-item:nth-child(1) > .dropdown__item").click()
    driver.find_element(By.ID, "firstname").click()
    driver.find_element(By.ID, "firstname").send_keys("Duy")
    driver.find_element(By.ID, "lastname").send_keys("Pham")
    driver.find_element(By.ID, "email").send_keys("pham.duy89@gmail.com")
    driver.find_element(By.ID, "tel").click()
    driver.find_element(By.ID, "tel").click()
    driver.find_element(By.ID, "tel").send_keys("015163224218")
    driver.find_element(By.ID, "street").click()
    driver.find_element(By.ID, "street").send_keys("Max-Lingner-Str 12A")
    driver.find_element(By.ID, "zipcode").send_keys("13189")
    driver.find_element(By.ID, "city").send_keys("Berlin")
    driver.find_element(By.ID, "dropdown_input_householdIncome").click()
    driver.find_element(By.ID, "dropdown_input_householdIncome").click()
    driver.find_element(By.CSS_SELECTOR, "sd-dropdown-item:nth-child(6) > .dropdown__item").click()
    driver.find_element(By.ID, "dropdown_input_employmentStatus").click()
    driver.find_element(By.CSS_SELECTOR, "sd-dropdown-item:nth-child(3) > .dropdown__item").click()
    driver.find_element(By.ID, "dropdown_input_householdSize").click()
    driver.find_element(By.CSS_SELECTOR, "sd-dropdown-item:nth-child(3) > .dropdown__item").click()

    driver.quit()


if __name__ == "__main__":
    contact_using_selenium(EXAMPLE_URL)
