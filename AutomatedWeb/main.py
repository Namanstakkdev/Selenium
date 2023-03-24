import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the application home page
driver.get("https://www.google.com/")

time.sleep(3)

# Get the search textbox
search_field = driver.find_element("name", "q")

# Enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
search_field.send_keys("Qui est Arnold Schaw")

time.sleep(5)

search_field.submit()

time.sleep(5)
# Get the list of elements which are displayed after the search
# Currently on result page using find_elements_by_class_name method
lists = driver.find_elements(By.CLASS_NAME, "g")

time.sleep(5)
# Get the number of elements found
print("Found " + str(len(lists)) + "searches:")

# Iterate through each element and print the text that is
# name of the search

i = 0
html = ''
for listitem in lists:
    print(listitem.get_attribute("innerHTML"))
    html += listitem.get_attribute("innerHTML")
    html += "\n"
    i = i+1

f = open("data.html", "wb")
html = html.encode('utf-8')
f.write(html)
f.close()

# Close the browser window
driver.quit()
