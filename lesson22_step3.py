from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser.get(link)


n1 = browser.find_element_by_id("num1")
n2 = browser.find_element_by_id("num2")

x = n1.text
y = n2.text
s = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(s))


button = browser.find_element_by_class_name("btn.btn-default")
button.click()


