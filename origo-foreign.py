from keyword import kwlist
from lib2to3.pgen2.pgen import DFAState
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

temp1 = []
temp2 = []
webpageName = []
kw = []

origoTitle = driver.find_elements_by_tag_name("h2")

for i in origoTitle:
    temp1.append(i.text)
    webpageName.append('Origo')
    kw.append('global news')

origoDescription = driver.find_elements_by_class_name("ait-lead")

for i in origoDescription:
    temp2.append(i.text)

dict = {'Title':temp1, 'Description': temp2, 'News site': webpageName, 'Keyword': kw}
df= pd.DataFrame(dict)
df.to_csv('articles.csv', index=False, encoding='utf-8-sig')
driver.quit()
