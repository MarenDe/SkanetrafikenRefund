from selenium import webdriver
from selenium import common
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui  import Select
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def complain(userTarget, timeDelayed, trainStationFrom, trainStationTo):
	# Load Data
	with open('data/jojo_cards.json') as json_data:
		data = json.load(json_data)

	options = Options()
	##options.set_headless(headless=True)

	browser = webdriver.Firefox(firefox_options=options, executable_path='vendor/geckodriver')
	##browser.implicitly_wait(60)
	browser.get(url = data["URL"])

	#TODO: common.exceptions.NoSuchElementException handling

	# Page 1
	browser.find_element_by_css_selector("button.standard-btn").click() # append guiden to URL to skip this step

	# Page 2
	browser.find_element_by_id("IsJOJO").click()
	browser.find_element_by_id("JOJOCrdNr").send_keys(data[userTarget]["JOJOCrdNr"])
	browser.find_element_by_id("JOJOControlValCode").send_keys(data[userTarget]["JOJOControlValCode"])
	element = browser.find_element_by_id("btnjojocard1")
	element.click()
	element.submit()
	##browser.find_element_by_css_selector('button.standard-btn.continue').click()

	# Page 3
	##browser.find_element_by_css_selector('select.valid')
	#element = browser.find_element_by_name("Deleyed")

	def find(driver):
		element = driver.find_element_by_xpath('//*[@id="Deleyed"]')
		if element:
			return element
		else:
			return False

	element = WebDriverWait(browser, 120).until(find)

	select = Select(browser.find_element_by_name("Deleyed"))
	select.select_by_value(data['timeDelayed'][timeDelayed])


	##element = browser.find_element_by_xpath("//select[@id='Deleyed']")
	all_options = element.find_elements_by_tag_name("option")
	for option in all_options:
		print("Value is: %s" % option.get_attribute("value"))

	browser.find_element_by_id("TravelFromStandard").send_keys(data["trainStations"][trainStationFrom])
	browser.find_element_by_id("TravelToStandard").send_keys(data["trainStations"][trainStationTo])