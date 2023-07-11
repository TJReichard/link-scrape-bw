import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

# Load and access environment variables
load_dotenv()
domain = os.getenv('domain')
login = os.getenv('login_mail')
pw = os.getenv('password')
path = os.getenv('driver_path')

link_list = []

# Set up Firefox options
options = Options()
options.add_argument('--headless')  # Run Firefox in headless mode (without opening a browser window)

# Set up Selenium service
service = Service(path)

# Set up Selenium driver
driver = webdriver.Firefox(service=service, options=options)

# URL of the webpage to crawl
url = domain

# Navigate to the webpage
driver.get(url)

#login
email = driver.find_element(By.NAME, "email")
email.send_keys(login)

password = driver.find_element(By.NAME, "password")
password.send_keys(pw)
password.send_keys(Keys.ENTER)

email = ""
password = ""

#  wait for page load
time.sleep(10)

#navigate to correct page
menu_item = driver.find_element(By.LINK_TEXT, "Mention List")
menu_item.click()

# wait for page load
time.sleep(10)


#prepare scraping of links from all pages by finding the pagination 
next = driver.find_element(By.CLASS_NAME, "next")
print("first: ", next)
while next:

    # Find elements with the class "mention_date"
    elements = driver.find_elements(By.CLASS_NAME, 'mention__date')

    # Extract href references from the elements
    hrefs = [element.get_attribute('href') for element in elements]

    # Print the extracted href references
    for href in enumerate(hrefs, start=1):
        link_list.append(href)

# check if last page is reached and exit while loop
    try:
        next.click()
        time.sleep(10)
        next = driver.find_element(By.CLASS_NAME, "next")
    except:
        print("last page")
        next = False
    else:
        next.click()
        time.sleep(10)
        next = driver.find_element(By.CLASS_NAME, "next")

# create csv file from list with the link and the appropriate numbers        
else:
    print(link_list)

    filename = "insta_link_list.csv"
    header = ["number", "link"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(link_list)

    print(f"CSV file '{filename}' has been created and saved.")

    # Close the browser
    driver.quit()

