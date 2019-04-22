import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.keys import Keys
print("Enter name of the uta student ")
name=input()
print("Enter University Name initials or ful name")
uni=input()
service = service.Service('D:/Research/edgeX/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
a=driver.get('https://google.com/');
search = driver.find_element_by_name('q')
search.send_keys(name," ",uni)
search.send_keys(Keys.RETURN)
finder=driver.find_element_by_partial_link_text("linked")
finder.click()
education=driver.find_element_by_class_name("topcard__headline")
print(education.text)