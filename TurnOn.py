import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

#opens browser
driver = webdriver.Chrome(executable_path=r"C:\Users\fedor\PycharmProjects\HeatTimer\chromedriver.exe")
driver.get("file:///E:/WTI%20-%20Network%20Power%20Switch.htm")

#maximizes window
driver.maximize_window()

#turn the oven 4 times(8 hours)
count = 0
while(count < 4):
    count = count + 1
    #select plug SnowStormDoor and turn off
    obj = Select(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[9]/td[7]/select"))
    obj.select_by_value("2")

    #press confirm actions
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input").click()

    #press Execute Actions
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input").click()

    #select plug SnowStormDoor and turn on
    obj = Select(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[9]/td[7]/select"))
    obj.select_by_value("1")

    #press confirm actions
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input").click()

    #press Execute Actions
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input").click()

    #browser waits 10 sec before continuing
    time.sleep(7200)

#shuts down Chrome and chromedriver service
driver.quit()