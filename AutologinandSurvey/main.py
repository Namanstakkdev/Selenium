# os module for saving the webpage
import os
import time
# Setting up the chrome webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
# import module for logging purposes
import logging
from dotenv import load_dotenv
load_dotenv()

# fucntion for setting up the logging structure
driver = webdriver.Chrome()
# maximize browser
driver.maximize_window()

username = os.getenv('USER')
password = os.getenv('PASSWORD')


class access_github:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        # Launch the browser and open the github URL in your web drive
        # Navigate to the application home page
        driver.get("https://github.com/login")
        time.sleep(5)
        uname = driver.find_element("id", "login_field")
        uname.send_keys(self.username)

        pword = driver.find_element("id", "password")
        pword.send_keys(self.password)
        time.sleep(5)
        driver.find_element(By.NAME, 'commit').click()
        time.sleep(5)

        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script(
                "return document.readyState === 'complete'")
        )

        # Verify that the login was successful.
        error_message = "Incorrect username or password."
        # Retrieve any errors found.
        errors = driver.find_elements(By.CLASS_NAME, "flash-error")

        # When errors are found, the login will fail.
        if any(error_message in e.text for e in errors):
            print("Login failed")
        else:
            print("Login successful")

        time.sleep(5)

    def clickRepo(self):
        repo = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[6]/div/aside/div/loading-context/div/div[1]/div/ul/li[1]/div/div/a")
        repo.click()
        print("Opened Up the Repo")
        time.sleep(5)

    def saveScreenshot(self):
        driver.get_screenshot_as_file(
            ".\\AutologinandSurvey\screenshots\screenshot.png")
        driver.save_screenshot(
            ".\\AutologinandSurvey\screenshots\screenshot.png")
        print("Screenshot Saved!")

    def saveWebPage(self):
        # get file path to save page
        n = os.path.join(
            "C:\Stakkdev\Tasks\Selenium Tasks\AutologinandSurvey\savedPages", "Page.html")
        # open file in write mode with encoding
        f = codecs.open(n, "w", "utf−8")
        # obtain page source
        h = driver.page_source
        # write page source content to file
        f.write(h)
        print("Webpage Saved.")

    def clickMenu(self):
        # click_menu method, displays drop down menu
        menu = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details")
        menu.click()
        print("Menu Clicked")
        time.sleep(5)

    def logout(self):
        logout = driver.find_element(By.CLASS_NAME, "dropdown-signout")
        logout.click()
        print("Logged Out!")
        time.sleep(5)

    def getlogs(self):
        logging.basicConfig(filename="C://Stakkdev//Tasks//Selenium Tasks//AutologinandSurvey//logs//logs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I: %M: %S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        print("Logs Generated.")


acc = access_github(username, password)
acc.getlogs()

acc.login()
acc.clickRepo()
acc.saveScreenshot()
acc.saveWebPage()
acc.clickMenu()
acc.logout()
acc.getlogs()
