from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from urllib import request
from urllib.parse import urljoin

## Initiate selenium driver
options = Options()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

## www.mozocry.com
baseurl = 'http://www.mozocry.com/'
subpages = [
    "", "#hedorosan", "#spectral", "#goldfish", "#beenk", "#game",
    "#stareater", "#zd", "#cb", "#trafri", "#sictic", "#etc"
]

# image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'swf']
image_extensions = ['jpg', 'jpeg', 'png']
base_window_width = 1920
base_window_height = 1080
page_load_time = 3


def routine(pageurl):
    print("loading...")
    driver.get(pageurl)
    sleep(page_load_time)

    ## 1. Take a full-page screenshot
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    screenshot_name = "screenshot_{}.png".format(pageurl.split('/')[-1])
    driver.save_screenshot(screenshot_name)
    print(pageurl)

    ## 2. Download all images
    img_tag_lst = driver.find_elements_by_tag_name('img')
    a_tag_lst = driver.find_elements_by_tag_name('a')
    image_url_lst = []
    for img_tag in img_tag_lst:
        relurl = img_tag.get_attribute('src')
        image_url_lst.append(urljoin(baseurl, relurl))
    for a_tag in a_tag_lst:
        relurl = a_tag.get_attribute('href')
        ext = relurl.split('/')[-1].split('.')[-1]
        if ext.lower() in image_extensions:
            image_url_lst.append(urljoin(baseurl, relurl))
    for img_url in image_url_lst:
        image_name = img_url.split('/')[-1]
        request.urlretrieve(img_url, image_name)
        print(img_url)


if __name__ == '__main__':
    for subpage in subpages:
        routine(urljoin(baseurl, subpage))
