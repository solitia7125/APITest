from selenium import webdriver
b=webdriver.Chrome()
b.get('http://www.maiziedu.com/')
b.maximize_window()
ele=b.find_element_by_link_text('企业直通班')
ele.click()