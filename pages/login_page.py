from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"  # Replace with the actual login page URL
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def open(self):
        self.driver.get(self.URL)
        
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.handle_change_password_popup()  # Handle the popup after clicking login
        
    def error_message(self):
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return error_element.text
        except:
            return None

    def is_visible(self):
        # Wait for page to load and check if the login form is visible
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON)).is_displayed()
        return self.driver.current_url == self.URL
    
    def handle_change_password_popup(self):
       
        try:
            return
            # ok_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']")))
            # ok_button.click()
            # print("Closed Chrome password popup")
        except TimeoutException:
            pass # Popup didn't appear, continue