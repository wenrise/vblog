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
print(driver.window_handles)
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
pop = driver.find_element(By.XPATH,"//*[@id='ww']")
pop.click()
pop.send_keys('大米')
add = driver.find_element(By.XPATH,'//*[@id="s_btn_wr"]')
add.click()