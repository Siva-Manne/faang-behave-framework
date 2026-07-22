from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    URL = "https://www.saucedemo.com/inventory.html"
    
    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    PAGE_TITLE = (By.CLASS_NAME, "title") # "Products"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_visible(self):
        return self.URL in self.driver.current_url and self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()
    
    def welcome_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text
    
    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()