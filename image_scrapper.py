import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
"""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

img_name = input("Name of image that you want to scrape from Google Images: ")
num_imgs = input("Number of images: ")

folder_name = input("Folder Name:")
os.makedirs(folder_name)

url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")

driver.get(url.format(s=img_name))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")

src = []
for img in imgResults:
    src.append(img.get_attribute('src'))

for i in range(int(num_imgs)):
    urllib.request.urlretrieve(str(src[i]),"./"+folder_name+"/"+img_name+"{}.jpg".format(i))