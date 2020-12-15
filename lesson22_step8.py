from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "C:\Program Files\Google\Chrome\Application\chromedriver"}
browser = webdriver.Chrome(desired_capabilities=cap, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")
import os


link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("Smolensk@mail.ru")


upload_button = browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'upload.txt')         # добавляем к этому пути имя файла 
upload_button.send_keys(file_path)


button = browser.find_element_by_tag_name("button")
button.click()
