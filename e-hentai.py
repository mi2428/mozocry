from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

## mission-chan
url = 'https://e-hentai.org/s/7b1b30f886/409815-1'
count = 1
count_max = 218

## work the dial
# url = 'https://e-hentai.org/g/409830/9f5b22e25a/'
# count = 1
# count_max = 14

## Saterii
# url = 'https://e-hentai.org/g/409821/dbdbef9f51/'
# count = 1
# count_max = 14

## Cygnet
# url = 'https://e-hentai.org/g/409872/d0c8282d0d/'
# count = 1
# count_max = 43

## Konamilk Tsushin
# url = 'https://e-hentai.org/g/205814/5209dca57f/'
# count = 1
# count_max = 33

img_width = 450
img_height = 600
wait = 2

driver.set_window_size(img_width, img_height)
driver.get(url)
while count <= count_max:
    imgurl = driver.find_element_by_id('img').get_attribute('src')
    driver.get(imgurl)
    sleep(wait)
    if driver.save_screenshot(str(count) + '.png'):
        print(imgurl)
    driver.back()
    driver.find_element_by_id('next').click()
    count += 1
