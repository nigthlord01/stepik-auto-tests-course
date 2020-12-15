import math
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


input = browser.find_element_by_id("answer")
input.send_keys(y)
option1 = browser.find_element_by_css_selector("[type='checkbox']")
option1.click()
option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()
option1 = browser.find_element_by_class_name("[class='btn btn-default']")
button.click()
