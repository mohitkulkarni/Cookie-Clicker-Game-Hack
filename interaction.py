# Cookie Clicker hack

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def timer(parm):
    global counter_stop
    if parm == "start":
        counter_stop = time.time() + 5
        return True

# --------------------------------------------- add your chrome web driver path here ----------------------------------
chrome_driver_path = "Your driver path(eg: C/user/documents)"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
counter_stop = 0
while True:
    timer("start")
    main_loop = True
    while main_loop:
        cookie.click()

        if time.time() > counter_stop:
            try:
                money = int(driver.find_element_by_id("cookies").text.split()[0])
            except ValueError:
                money = int(driver.find_element_by_id("cookies").text.split()[0].replace(",", ""))
            if money > 130000:
                rew4 = driver.find_element_by_id("product4")
                rew4.click()
            elif money > 12000:
                rew3 = driver.find_element_by_id("product3")
                rew3.click()
            elif money > 1100:
                rew2 = driver.find_element_by_id("product2")
                rew2.click()
            elif money > 115:
                rew1 = driver.find_element_by_id("product1")
                rew1.click()
            elif money > 20:
                rew0 = driver.find_element_by_id("product0")
                rew0.click()
            main_loop = False
            print("clicked")
