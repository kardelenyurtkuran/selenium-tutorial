from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser= webdriver.Chrome()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url) #chrome üzerinden verilen linki açmak için
time.sleep(5) #5sn açık kalacak


elements = browser.find_elements(By.CSS_SELECTOR,".content") #. olursa class, # olursa id'si content olanı çekersin

for element in elements:
    print("***********")
    print(element.text)
browser.close()