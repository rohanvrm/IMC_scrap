from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep 
from openpyxl import load_workbook, cell
import csv
import xlsxwriter
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import WebDriverWait as W

import requests, six
import lxml.html as lh

import pandas as pd
import time
import os

MAX_PAGE_NUM=49 
# for 1 to page 50



driver = webdriver.Chrome(executable_path=r"C:\Users\Rohan\Downloads\chromedriver")
url="https://www.nmc.org.in/information-desk/indian-medical-register"

driver.get(url)
driver.switch_to.window(driver.window_handles[1]) 

asd=driver.find_element_by_css_selector("#advance_form > div:nth-child(5) > div > div > button")

#select = Select(asd)
asd.click()
dd=driver.find_element_by_css_selector("#advance_form > div:nth-child(5) > div > div > ul > li:nth-child(33) > a")
dd.click()


btn=driver.find_element_by_css_selector("#doctor_advance_Details")
btn.click()
# #Select se = new Select(driver.findElement(By.xpath("//*[@id='advsmcId']")));
# wait_time_out = 5
# id_locator="advsmcId"
# wait_variable = W(driver, wait_time_out)
# dropt = Select(wait_variable.until(E.presence_of_element_located((By.ID, id_locator))))
# dropt.select_by_value("1")
#for option in time_element.options:

#Create a handle, page, to handle the contents of the website
# page = requests.get(url)

# #Store the contents of the website under doc
# doc = lh.fromstring(page.content)

# #Parse data that are stored between <tr>..</tr> of the site's HTML code
# tr_elements = doc.xpath('//tr')

# #Check the length of the first 12 rows
# for T in tr_elements[:12]:
#     print(len(T))
noList=[]
nameList = []
yearList = []
regnoList = []
fatherList=[]
councilList=[]

#sleep(3)
numpg =0
while(numpg<97):
   sleep(5)
   tbody=driver.find_element_by_css_selector("#doct_info5 > tbody")
   
   tbody_rows = tbody.find_elements_by_tag_name('tr')
   
   for tbody_row in tbody_rows:
      
      cell0=  tbody_row.find_elements_by_tag_name("td")[0]
      
      cell1 = tbody_row.find_elements_by_tag_name("td")[1]
      
      cell2 = tbody_row.find_elements_by_tag_name("td")[2]
      
      cell3 = tbody_row.find_elements_by_tag_name("td")[3]
     
      cell4 = tbody_row.find_elements_by_tag_name("td")[4]
      
     
      cell5 = tbody_row.find_elements_by_tag_name("td")[5]
      
      
      noList.append(cell0.text)
      yearList.append(cell1.text)
      regnoList.append(cell2.text)
      councilList.append(cell3.text)
      nameList.append(cell4.text)
      fatherList.append(cell5.text)
      
      # for cell in tbody_row.find_elements_by_tag_name('td'):
      #     #print(cell.text)
      #     myList.append(cell.text)


   nextpg=driver.find_element_by_css_selector("#doct_info5_next")
   nextpg.click()
   numpg+=1
   print(numpg)
   

workbook = xlsxwriter.Workbook('D:\\dev_\imc_scrap.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0    
for item in noList:
   worksheet.write(row, column, item)
   
   row+=1

row = 0
column = 0    
for item in yearList:
   worksheet.write(row, 1, item)
   
   row+=1

row = 0
column = 0 
for i in regnoList :
   worksheet.write(row,2,i)
   row+=1

row = 0
column = 0 
for j in councilList :
   worksheet.write(row,3,j)
   row+=1

row = 0
column = 0 
for j in nameList :
   worksheet.write(row,4,j)
   row+=1

row = 0
column = 0 
for j in fatherList :
   worksheet.write(row,5,j)
   row+=1


workbook.close()


print("DONE")




