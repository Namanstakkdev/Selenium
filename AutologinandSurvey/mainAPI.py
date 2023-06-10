from dotenv import load_dotenv
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import json

f = open('api.json')
data = json.load(f)

f.close()

load_dotenv()

driver = webdriver.Chrome()
driver.maximize_window()

username = data["credentials"]["user"]
password = data["credentials"]["pass"]


class access_github:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):

        driver.get(data["url"])
        time.sleep(5)
        uname = driver.find_element("id", "login_field")
        uname.send_keys(self.username)

        pword = driver.find_element("id", "password")
        pword.send_keys(self.password)
        time.sleep(5)
        driver.find_element(
            By.XPATH, data["clicks"]["xpaths_arr"][0]).click()
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

    def click(self, i):
        repo = driver.find_element(
            By.XPATH, data["clicks"]["xpaths_arr"][i])
        repo.click()
        print("Clicked Xmap - "+i)
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

    def getlogs(self):
        logging.basicConfig(filename="C://Stakkdev//Tasks//Selenium Tasks//AutologinandSurvey//logs//logs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I: %M: %S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        print("Logs Generated.")


acc = access_github(username, password)
acc.getlogs()

acc.login()
# acc.saveScreenshot()
for i in range(1, data["clicks"]["no_of_clicks"]):
    acc.click(i)
acc.saveWebPage()
acc.getlogs()
