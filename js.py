from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

dr = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
dr.implicitly_wait(10)
dr.get("http://www.mazegenerator.net/")
# dr.get('https://www.csdn.net/')

#locator = (By.LINK_TEXT, u'首页')
locator1 = (By.ID, u'MazeDisplay')
# 使用显式等待
try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator1))
# visibility_of_element_located

finally:
    print("maze load complete")

# time.sleep(5)
#print(dr.find_element_by_link_text('About').get_attribute('href'))

# JS1 = "document.title='xxxxxx';"
# dr.execute_script(JS1)
#
# time.sleep(1)
# JS2 = r"alert($(document).attr('title'));"
# dr.execute_script(JS2)
#
# time.sleep(10)

dr.quit()
