from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(5)
ele = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/a[1]")
ActionChains(driver).move_to_element(ele).perform()
ele.click()
time.sleep(3)
pop = driver.find_element(By.XPATH,"//*[@id='header-link-wrapper']/li[9]/a")
pop.click()
