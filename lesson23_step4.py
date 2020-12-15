from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)


button = browser.find_element_by_tag_name("button")
button.click()


confirm = browser.switch_to.alert
confirm.accept()


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


input = browser.find_element_by_id("answer")
input.send_keys(y)


button = browser.find_element_by_class_name("btn.btn-primary")
button.click()
