from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep 
from openpyxl import load_workbook, cell
import openpyxl
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
sleep(3) 
#ff=driver.find_element_by_xpath("//*[@id=\"advsmcId\"]/option[2]")
asd=driver.find_element_by_css_selector("#advance_form > div:nth-child(5) > div > div > button")

#select = Select(asd)
asd.click()
sleep(1)
dd=driver.find_element_by_css_selector("#advance_form > div:nth-child(5) > div > div > ul > li:nth-child(3) > a")
dd.click()

btn=driver.find_element_by_css_selector("#doctor_advance_Details")
btn.click()

sleep(3)

nextpg=driver.find_element_by_css_selector("#doct_info5_next")
nextpg.click()



print("DONE")




