from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

## mission-chan
# url = 'https://e-hentai.org/s/7b1b30f886/409815-1'
# count = 1
# count_max = 218

## work the dial
# url = 'https://e-hentai.org/s/517068ec74/409830-1'
# count = 1
# count_max = 15

## Saterii
# url = 'https://e-hentai.org/s/b9afb813e9/409821-1'
# count = 1
# count_max = 15

## Cygnet
# url = 'https://e-hentai.org/s/c407b61338/409872-1'
# count = 1
# count_max = 44

## Konamilk Tsushin
url = 'https://e-hentai.org/s/03c1d190b1/205814-1'
count = 1
count_max = 34

img_width = 450
img_height = 600
wait = 3

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
