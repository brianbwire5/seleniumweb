import pytest
import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


#def test_add_strings():
# result = my_functions.add("I like ", "burgers")
# assert result == "I like burgers"


def test_orangehrm_login(driver):
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    try:
        # Wait for the username input field to be visible
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_input.send_keys("Admin")

        # Find and fill the password field
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("admin123")

        # Find and click the login button
        login_button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        driver.implicitly_wait(30)
        print("Login was successfully executed")
    except TimeoutException:
        pytest.fail("Timeout: Username input field not found")
    except NoSuchElementException:
        pytest.fail("Element not found")


def test_open_drawer(driver):
    open_drawer = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')

    try:
        open_drawer.click()
        assert True, f"Click was successful"
        print("The drawer was opened successfully")
    except Exception as e:
        assert False, f"The drawer failed to open: {str(e)}"


def test_fill_form(driver):
    try:
        expose_form = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div['
                                          '1]/div/div[2]/div/div/i')
        expose_form.click()
        assert True, f"Click was successful"
        print("The leave page was opened successfully")
    except Exception as e:
        assert False, f"Leave form not available: {str(e)}"

    driver.implicitly_wait(15)

    try:
        date_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                                   '1]/div/div[1]/div/div[2]/div/div/input')

        date_input.send_keys("2024-12-01")
        assert True, f"First date input captured successfully"
        print("The first input date field captured successfully")
    except Exception as e:
        assert False, f"The first input date field captured successfully is not available: {str(e)}"

    try:
        date_input_two = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                       '2]/form/div[1]/div/div[2]/div/div[2]/div/div/input')

        date_input_two.send_keys("2024-12-12")
        assert True, f"Second date input captured successfully"
        print("The second input date field captured successfully")
    except Exception as e:
        assert False, f"The second input date field captured successfully is not available: {str(e)}"
    driver.implicitly_wait(20)

    try:
        # Select drop down menu
        drop_down_menu = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                       '2]/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/i')
        drop_down_menu.click()
        assert True, f"Field dropdown captured successfully"
        print("Field drop down captured successfully")
    except Exception as e:
        assert False, f"Field drop down captured successfully is not available: {str(e)}"

    try:
        option_rejected = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                              '1]/div/div[3]/div/div[2]/div/div[2]/div[1]')
        option_rejected.click()
        assert True, f"Field dropdown captured successfully"
        print("Rejected field  captured successfully")
    except Exception as e:
        assert False, f"Rejected field not captured successfully is not available: {str(e)}"

    try:
        drop_down_menu2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                        '2]/form/div[1]/div/div[4]/div/div[2]/div/div')
        drop_down_menu2.click()
        assert True, f"Field dropdown menu captured successfully"
        print("Field dropdown menu captured successfully")
    except Exception as e:
        assert False, f"Field dropdown menu not captured successfully: {str(e)}"

    try:
        option_select = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                            '1]/div/div[4]/div/div[2]/div/div[2]/div[2]')
        option_select.click()
        assert True, f"Option captured successfully"
        print("Option selected successfully")
    except Exception as e:
        assert False, f"Option not captured successfully: {str(e)}"

    try:
        type_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                                  '2]/div/div[1]/div/div[2]/div/div/input')
        type_name.send_keys("test")
        assert True, f"test value sent successfully"
        print("Test value sent successfully")
    except Exception as e:
        assert False, f"Test value was not sent: {str(e)}"

    time.sleep(10)

    try:
        type_search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                                    '2]/div/div[1]/div/div[2]/div/div[2]/div')
        type_search.click()
        assert True, f"Search was successfully"
        print("Searched successfully")
    except Exception as e:
        assert False, f"Search was not successful: {str(e)}"

    try:
        click_domain_icon = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                          '2]/form/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/i')

        click_domain_icon.click()
        assert True, f"Icon click done successfully"
        print("I con click done successfully")
    except Exception as e:
        assert False, f"Icon click was not successful: {str(e)}"

    try:
        select_domain = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                      '2]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[5]')

        select_domain.click()
        assert True, f"Select domain done successfully"
        print("Select domain done successfully")
    except Exception as e:
        assert False, f"I con click was not successful: {str(e)}"

    try:
        toggle_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div['
                                                      '2]/form/div[2]/div/div[3]/div/label/span')
        toggle_button.click()
        assert True, f"Toggle done successfully"
        print("Toggle done successfully")
    except Exception as e:
        assert False, f"Toggle click was not successful: {str(e)}"

    try:
        search_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div['
                                                      '3]/button[2]')
        search_button.click()
        assert True, f"Search button clicked successfully"
        print("Search clicked successfully")
    except Exception as e:
        assert False, f"Search click was successful: {str(e)}"
