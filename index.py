# --------------------- IMPORTS ---------------------
# main selenium webdrive
from selenium import webdriver

# provides support for keyboard keys e.g. mocking a keypress
from selenium.webdriver.common.keys import Keys

# importing options to make the browser headless i.e. doesn't open a window
# while doing all the scraping / crawling stuff
from selenium.webdriver.chrome.options import Options

from getFedora import savePosts
from db import getNewPosts
# --------------------- INIT STUFF ---------------------

options = webdriver.ChromeOptions()  # importing for making chrome headless
options.add_argument('headless')   # headless means chrome doesn't pop up

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)


def login(username, password):

    # email id / username
    username = username

    # password
    password = password

    # -------- logging in ------
    # going to login page
    url = 'https://twitter.com/login'

    # getting url
    driver.get(url)

    # email id
    # js-username-field -> email
    inputElement = content = driver.find_element_by_class_name('js-username-field')
    inputElement.send_keys(username)

    # password
    # js-password-field -> password
    inputElement = content = driver.find_element_by_class_name('js-password-field')
    inputElement.send_keys(password)

    # sending form/input
    inputElement.send_keys(Keys.RETURN)


def postTweet(tweetMessage):
    # Already Logged In

    # message to be tweeted
    tweetMessage = tweetMessage

    # -------- POSTING TWEET ----------

    # going to page meant for posting
    url = 'https://twitter.com/compose/tweet'
    driver.get(url)

    # typing message
    inputElement = driver.find_element_by_class_name('public-DraftEditor-content')
    inputElement.send_keys(tweetMessage)

    # sending tweet
    submitButton = driver.find_element_by_css_selector('div[data-testid=tweetButton]')
    submitButton.click()


def execute(username, password):
    # saving new posts to DB
    savePosts()

    # Status Print
    print('Posts saved')

    # getting and saving new posts
    # if there are new posts, result will be a list of post dictionaries
    # else, i.e. no new posts, result will be a string with the message
    # 'No new posts'
    result = getNewPosts()

    # status print
    print('Scraped Fedora site and saved all new posts in db (IF ANY)')

    if type(result) == str:     # i.e. no new posts

        print(result)
        print('Exiting the program')

    else:                       # i.e. there are new posts

        # logging into twitter
        login(username, password)

        # iterating through new posts
        for post in result:

            # generating message to be sent
            msg = f"{post['title']}\n\n{post['link']}"

            # posting tweet
            postTweet(msg)

        print('Tweeted all new posts!')
        print('Exiting the program')

# type in your twitter username and password as below
# execute(<username>, <password>)

# closing tab/window
driver.close()
