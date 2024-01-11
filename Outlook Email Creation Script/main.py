# Web automation script 
# Please enjoy and feel free to use
# capcha will need to be manualy solved
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

# For Email creation through outlook
driver.get('https://signup.live.com/signup?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&id=292841&contextid=B7965C1046BCEEEC&opid=120333FC0A870652&bk=1701830377&sru=https://login.live.com/login.srf%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26contextid%3dB7965C1046BCEEEC%26opid%3d120333FC0A870652%26mkt%3dEN-US%26lc%3d1033%26bk%3d1701830377%26uaid%3d0b0142ed87794b82b0de03f7ec8d4fe5&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=0b0142ed87794b82b0de03f7ec8d4fe5')

element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'liveSwitch'))
)

element.click()
time.sleep(2)

member_name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'MemberName'))
)

member_name_element.send_keys('TESTINGusername1234213')

driver.execute_script("OnNext();")

# more gobbolty gook
password_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'PasswordInput'))
)
password_element.send_keys('TestingPassword')
time.sleep(2)

# Execute JavaScript to click the next button
driver.execute_script("document.getElementById('iSignupAction').click();")

# Wait sequince 
first_name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'FirstName'))
)

#  first name
first_name_element.send_keys('YourFirstName')

# Wait for the 'LastName' element to be present
last_name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'LastName'))
)

#  last name
last_name_element.send_keys('YourLastName')

driver.execute_script("document.getElementById('iSignupAction').click();")

# Couldent figure out, straight ripped from web action becouse im a caveman
try:
    day_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'BirthDay'))
    )
    month_input = driver.find_element(By.ID, 'BirthMonth')
    year_input = driver.find_element(By.ID, 'BirthYear')

    day_input.send_keys('11')
    month_select = Select(month_input)
    month_select.select_by_value('8')  
    year_input.send_keys('1992')
except TimeoutException:
    print("TimeoutException: Script failed to locate the birthdate elements.")
    driver.quit()


try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'iSignupAction'))
    )
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    next_button.click()
except TimeoutException:
    print("TimeoutException: Script failed to locate the 'Next' button.")
    driver.quit()
    
try:
    # Adjust the time if needed
    next_puzzle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-theme='home.verifyButton']"))
    )
    print("Found the 'Next' button after solving the puzzle.")
    next_puzzle_button.click()
except TimeoutException:
    print("TimeoutException: Script failed to locate the 'Next' button after solving the puzzle.")
    driver.quit()
time.sleep(2)

input("Press Enter to close the script")

driver.quit()
