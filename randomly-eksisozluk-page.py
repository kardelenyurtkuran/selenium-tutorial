from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser= webdriver.Chrome()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p=" #kaçıncı sayfaya gideceğin belli olmadığı için böyle bir url tanımlanır

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 3:
    randomPage = random.randint(1,1290) #1 ile 1290 arası rasgele bir sayfa seçmek için
    newUrl = url + str(randomPage)
    browser.get(newUrl) #chrome üzerinden verilen linki açmak için
    elements = browser.find_elements(By.CSS_SELECTOR,".content")  # . olursa class, # olursa id'si content olanı çekersin
    for element in elements:
        entries.append(element.text) # rasgele sayfada ki tüm .content içeriği
    time.sleep(0.5)  # 5sn açık kalacak
    pageCount += 1

with open("entries.txt", "w", encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + ".\n")
        file.write("***************")
        entryCount += 1

browser.close()




