from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def execute_test_case(useremail, userpassword):
    print("test case 01 started")
    driver = webdriver.Chrome()
    #maximize the window size
    driver.maximize_window()
    #navigate to the url
    driver.get("https://www.facebook.com/")
    #identify the login email and password text box and enter the value
    time.sleep(1)
    e = driver.find_element(By.ID, "email")
    e.send_keys(useremail)
    time.sleep(1)
    p = driver.find_element(By.ID, "pass")
    p.send_keys(userpassword)
    time.sleep(1)
    #click on login button
    l = driver.find_element(By.NAME, "login")
    l.click()
    time.sleep(2)
    #Step05: close the browser
    driver.close()
    print("sample test case 01 successfully completed")
