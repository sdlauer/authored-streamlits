##############################################
# Reads in the csv provided in the command line and
# visits every URL in the column labeled `site`
#
# Requires the selenium package to be installed and the
# Chrome webdriver to be installed in the environments path
# https://sites.google.com/chromium.org/driver/


import pandas as pd
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


sites = pd.read_csv(sys.argv[1])
driver = webdriver.Chrome()

for site in sites["site"]:
    #print(site)
    driver.get(site)
    time.sleep(7)
    try:
        button = driver.find_element_by_css_selector('.styles_restartButton__3YxAJ')
        print(site + ' is asleep trying to wake.')
        button.click()
        time.sleep(10)
    except NoSuchElementException:
        print(site + ' is working!')
        continue
    


driver.close()
