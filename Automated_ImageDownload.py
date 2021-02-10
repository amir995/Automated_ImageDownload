from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
#///////////////////////
my_options = webdriver.ChromeOptions()
#my_options.add_argument("--headless")
#my_options.add_argument("--incognito")
#my_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Football"+Keys.RETURN)


print(driver.title)
time.sleep(0.5)
pyautogui.moveTo(343, 249)
pyautogui.click(button='left')
time.sleep(5)
pyautogui.moveTo(442,436)
pyautogui.click(button='right')
time.sleep(2)
pyautogui.moveTo(503,313)
pyautogui.click(button='left')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
driver.close()
