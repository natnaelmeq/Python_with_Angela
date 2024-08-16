from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # this is for enter and click after enter the data

#keep chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,value="fname")
last_name = driver.find_element(By.NAME,value="lname")
email = driver.find_element(By.NAME,value="email")


first_name.send_keys("Natnael")
last_name.send_keys("Gashaw")
email.send_keys("natnaelmeq@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR,value="form button")
submit.click()

