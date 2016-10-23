
from selenium import webdriver

browser = webdriver.Chrome('/home/miles/ejercicios_libro/chromedriver')
#browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
