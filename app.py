import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#req = requests.get("https://tshc.gov.in/Hcdbs/search.do")
#soup = BeautifulSoup(req.content, "html.parser")


def my_detail(court_number):
    print(court_number)
    initial_url = "https://tshc.gov.in/Hcdbs/search.do"

    driver = webdriver.Chrome() #options=chrome_options
    driver.get(initial_url)

    # time.sleep(5)

    button_value = 'DAILY LIST'
    next_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='" + button_value + "']")
    next_button.click()

    time.sleep(5)

    button_value = 'COURT WISE'
    next_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='" + button_value + "']")
    next_button.click()

    time.sleep(5)

    dropdown_id = 'court'
    dropdown = driver.find_element(By.ID, dropdown_id)

    select = Select(dropdown)

    select.select_by_value(court_number)

    elements = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")

    filtered_elements = []
    desired_text1 = "GANDHAM DURGA BOSE"
    desired_text2 = "ALTAF FATHIMA"

    for x in elements:
        if desired_text1 in x.get_attribute("outerHTML"):
            filtered_elements.append(x)
        if desired_text2 in x.get_attribute("outerHTML"):
            filtered_elements.append(x)
            # print(x.get_attribute("outerHTML"))

    for y in filtered_elements:
        item_no = y.find_element(By.XPATH, ".//td[@data-label='S.No']").text
        case_detail = y.find_element(By.XPATH, ".//td[@data-label='Case Det']").text
        # print(y.get_attribute("outerHTML"))
        print("The case: " + case_detail + "is listed in COURT NO." + court_number + " with an item number: " + item_no + "\n")

    driver.quit()


# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

initial_url = "https://tshc.gov.in/Hcdbs/search.do"

driver = webdriver.Chrome(options=chrome_options)
driver.get(initial_url)

# time.sleep(5)

button_value = 'DAILY LIST'
next_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='" + button_value + "']")
next_button.click()

time.sleep(5)

button_value = 'COURT WISE'
next_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='" + button_value + "']")
next_button.click()

time.sleep(5)

dropdown_id = 'court'
dropdown = driver.find_element(By.ID, dropdown_id)
select = Select(dropdown)

# Get all the values from the dropdown
dropdown_values = [option.text for option in select.options]

for a in dropdown_values[1:]:
    i = a[-2:].replace(" ", "")
    my_detail(str(i))

driver.quit()
