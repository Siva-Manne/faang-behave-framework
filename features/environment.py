from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import os
import allure
from allure import attachment_type


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  
    # Set up the Selenium WebDriver
    #service = Service(executable_path="path/to/chromedriver")  # Replace with the actual path to your ChromeDriver executable
    context.driver = webdriver.Chrome(options=options)  # You can change this to Firefox or any other browser
    
    """
    other way to install chrome with webdriver_manager
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    
    with explicitly specifying the path to the ChromeDriver executable:
    service = Service(executable_path="path/to/chromedriver")
    context.driver = webdriver.Chrome(service=service, options=options)

   """
    context.driver.implicitly_wait(10)  # Wait for elements to load (adjust as needed)
    
     # Init Page Objects
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = DashboardPage(context.driver)
    
    # Test data
    context.valid_user = "standard_user"
    context.valid_pass = "secret_sauce"
    

def after_scenario(context, scenario):
    if scenario.status == "failed":
        #capture screenshot on failure
        timestamp  = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"reports/screenshots/{scenario.name}_{timestamp}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=screenshot_path, attachment_type=attachment_type.PNG)
        context.driver.quit()

def before_all(context):
    os.makedirs("reports/allure-results", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    
def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

    
