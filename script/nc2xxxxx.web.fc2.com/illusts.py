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

## http://nc2xxxxx.web.fc2.com/
baseurl = 'http://nc2xxxxx.web.fc2.com/stock/'
subpages = []
start = 11
for i in range(start, 57):
    n = str(i*10).zfill(3)
    subpages.append("{}.html".format(n))

image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'swf']
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
    print(pageurl)
    driver.save_screenshot(screenshot_name)

    ## 2. Download all images
    image_url_lst = []
    rel_url_lst = []
    rel_url_lst.extend([tag.get_attribute('src') for tag in driver.find_elements_by_tag_name('img')])
    rel_url_lst.extend([tag.get_attribute('href') for tag in driver.find_elements_by_tag_name('a')])
    for relurl in rel_url_lst:
        if relurl is None:
            continue
        ext = relurl.split('/')[-1].split('.')[-1]
        if ext.lower() in image_extensions:
            image_url_lst.append(urljoin(baseurl, relurl))
    for img_url in image_url_lst:
        image_name = img_url.split('/')[-1]
        print(img_url)
        try:
            request.urlretrieve(img_url, image_name)
        except Exception:
            print("skipped:", img_url)


if __name__ == '__main__':
    for subpage in subpages:
        routine(urljoin(baseurl, subpage))
