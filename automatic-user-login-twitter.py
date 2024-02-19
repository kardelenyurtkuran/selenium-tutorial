from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://twitter.com/")
time.sleep(3)

login = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div") # Giris yap butonu xpath hali
login.click() #butona tıkla

time.sleep(5)

username = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input") #kullanıcı adı alanı XPATH
username.send_keys("XXXX") #twitter kullanıcı adı

rightButton = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div") #ileri butonu
rightButton.click()

time.sleep(2) #henüz password input alanı oluşmadan doldurmaya çalıştığı için hata alıyorsun.

password = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys("XXXX") #twitter şifre

loginButton = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
loginButton.click()

time.sleep(7)

browser.close()