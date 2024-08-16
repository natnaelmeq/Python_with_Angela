from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # this is for enter and click after enter the data


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


no_of_articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# no_of_articles.click()
# print(f"Number of articles: {no_of_articles.text}")

search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")

search.send_keys("natnael", Keys.ENTER)
