import time
from selenium import webdriver
print('starting web scrapper')

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
#search_box = driver.find_elements_by_name('q')
search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('Clint Eastwood')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.get('http://www.google.com/')
driver.maximize_window()
time.sleep(3) # Let the user actually see something!
driver.get("https://github.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.close()
driver.quit()