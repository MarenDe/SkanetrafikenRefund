"""
Skanetrafiken complaint automator 3000
"""

from selenium import webdriver
from selenium import common
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui  import Select
import json

with open('data.json') as json_data:
    data = json.load(json_data)

# add command line options with argparse or a bash wrapper to select data from data.
userTarget = "manel"
timeDelayed = "20min"
trainStationFrom = "from"
trainStationTo = "to"

options = Options()
#options.set_headless(headless=True)

browser = webdriver.Firefox(firefox_options=options, executable_path='../vendor/geckodriver')
browser.get(data["URL"])

# Page 1
browser.find_element_by_css_selector("button.standard-btn").click() # append guiden to URL to skip this step

# Page 2
browser.find_element_by_id("IsJOJO").click()
browser.find_element_by_id("JOJOCrdNr").send_keys(data[userTarget]["JOJOCrdNr"])
browser.find_element_by_id("JOJOControlValCode").send_keys(data[userTarget]["JOJOControlValCode"])
browser.find_element_by_id("btnjojocard1").click()
#browser.find_element_by_

# Page 3
select = Select(browser.find_element_by_name("Deleyed"))
#select.select_by_value(data[timeDelayed][])

browser.find_element_by_id("TravelFromStandard").send_keys(data["trainStations"][trainStationFrom])
browser.find_element_by_id("TravelToStandard").send_keys(data["trainStations"][trainStationTo])