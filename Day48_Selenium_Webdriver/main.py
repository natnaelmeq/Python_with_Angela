from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.de/-/en/BRUCE-H-LIPTOn/dp/9380480016/ref=sr_1_2?crid=3L9HPP50DZSND&dib=eyJ2IjoiMSJ9.Cp1Xv742QD8le7525KSYNYzjx9E0loEQpy0HQ6VkpGFYQgaH2CVKSOeX8XX7mgyiEmBrGkHdmMUTm6Abi6wnLn-vycxGODl4JdOWPZyZFZVAneWHGev4o6IMrViBLoHH1BGgwg3JoyTDtVzJTgGf7EWFmrHa2Hd1kuvaEx9t2RT0iGgbTSasV0dNTawX7JqDNPWJgojLva39QbMFPDQGqxkF0PrFatGom7mUaq6qtsM.2dVItN6XcCxjaC2JXipyTSWB32_f2jS3WBlKiIqepcQ&dib_tag=se&keywords=the+biology+of+belief&qid=1722580253&sprefix=THE+BIOLOGY+OF+%2Caps%2C170&sr=8-2")

price_dollar = driver.find_element(By.CLASS_NAME,value="a-size-medium")
print(f"The price is {price_dollar.text}")

#if we do know exact calling element we can use XPATH
driver.find_element(By.XPATH, value="xpaht value copy from the element")
