from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(executable_path='C:/Users/shiro/Downloads/chromedriver_win32/chromedriver')
driver.get('https://www.origo.hu/nagyvilag/index.html')
driver.implicitly_wait(10)

driver.find_element_by_css_selector('.fc-button-label').click()

driver.find_element_by_css_selector('.oc-loadMore.btn.obtn').click()
r=1
templist= []
df = 

while(r>25):
    try:
        origoTitle = driver.find_element_by_tag_name("h2").text
        origoDescription = driver.find_element_by_class_name("ait-lead").text

# for element in origoDescription:
#     print(element.text)
        dict = {'Headlines': origoTitle, 'Small Description': origoDescription}
        templist.append(dict)
        df = pd.DataFrame(templist)
        r+= 1
    except NoSuchElementException: 
        break


df.to_csv('origo.csv')

driver.quit()
