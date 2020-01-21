# --------------------- IMPORTS ---------------------
# main selenium webdrive
from selenium import webdriver
from db import saveNewPost
# provides support for keyboard keys e.g. mocking a keypress
from selenium.webdriver.common.keys import Keys

# importing options to make the browser headless i.e. doesn't open a window
# while doing all the scraping / crawling stuff
from selenium.webdriver.chrome.options import Options

# using beautiful soup to parse the page
from bs4 import BeautifulSoup


# --------------------- INIT STUFF ---------------------

options = webdriver.ChromeOptions()  # importing for making chrome headless
options.add_argument('headless')   # headless means chrome doesn't pop up

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)


# saves all new post in the db
def savePosts():

    # url to scrape
    url = 'https://fedoramagazine.org/'
    driver.get(url)

    # soupifying the source code
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    titles = soup.find_all('h2', {'class': 'post-title'})

    for el in titles:
        currAnchor = el.find('a')
        # saveNewPost only stores a 'post' document in the db if it's new
        saveNewPost(currAnchor['title'], currAnchor['href'])

    # closing window
    driver.close()
