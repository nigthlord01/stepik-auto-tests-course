from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")

link = "http://suninjuly.github.io/registration1.html"
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
