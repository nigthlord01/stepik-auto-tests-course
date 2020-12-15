from selenium import webdriver
import math
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

option1 = browser.find_element_by_id("num1")
x = option1.get_attribute("data-value")

option2= browser.find_element_by_id("num2")
y = option2.get_attribute("data-value")

z = str( int(x + y) )
print(z)
browser.find_element_by_tag_name("dropdown").click()
browser.find_element_by_css_selector("[value='z']").click()

input = browser.find_element_by_id("answer")
input.send_keys(y)

