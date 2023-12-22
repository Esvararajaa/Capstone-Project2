import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Test_data import data
from Test_locators import locators


class Test_Employee:

    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_forgot_link(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        print("Login page url opened successfully")
        self.driver.find_element(By.XPATH, locators.l_forgot().pwd_link).click()
        print("Forgot your password? link is clicked")
        ur_name = self.driver.find_element(By.NAME, locators.l_forgot().user)
        if ur_name.is_displayed():
            print("Username text box is visible")
            ur_name.send_keys(data.Dforgot().user)
            print("Value is sent to the username text box")
        else:
            print("Username text box is not visible")
        self.driver.find_element(By.CSS_SELECTOR, locators.l_forgot().forgot_btn).click()
        success_txt = self.driver.find_element(By.CSS_SELECTOR, locators.l_forgot().success_msg).text
        assert success_txt == 'Reset Password link sent successfully'
        print(f"{success_txt} to the registered email id")

    def test_nav_options(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        print("Login page url opened successfully")
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(data.Data().username01)
        print("Username entered")
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(data.Data().password01)
        print("Password entered")
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        print("Login successfull")
        self.driver.find_element(By.XPATH, locators.option().admin_opt).click()
        print("Admin option clicked")
        title = self.driver.title
        if title == 'OrangeHRM':
            print(f"Title of this page is {title}")
        else:
            print(f"Title of this page is {title}")
        option = self.driver.find_elements(By.XPATH, locators.option().navig)
        for i in option:
            data.Data().com_nav.append(i.text)
        assert data.Data().com_nav == data.Data().nav
        print("List of the Body nav options are:-")
        c = 0
        for n in data.Data().com_nav:
            c = c + 1
            print(f"{c}. {n}")

    def test_menu(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        print("Login page url opened successfully")
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(data.Data().username01)
        print("Username entered")
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(data.Data().password01)
        print("Password entered")
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        print("Login successfull")
        self.driver.find_element(By.XPATH, locators.option().admin_opt).click()
        print("Admin option clicked")
        menu = self.driver.find_elements(By.XPATH, locators.menu().opt)
        for m in menu:
            data.Data().com_menu.append(m.text)
        assert data.Data().com_menu == data.Data().menu
        print("List of Menu options are:-")
        cnt = 0
        for m in data.Data().com_menu:
            cnt = cnt + 1
            print(f"{cnt}. {m}")

