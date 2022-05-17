from selenium import webdriver
driver = webdriver.Chrome("E:\chromedriver.exe")

driver.get("https://www.youtube.com/")
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys("natalia qa")
button = driver.find_element_by_class('//*[@id="search-icon-legacy"]/yt-icon')
button.click()
sleep(6)