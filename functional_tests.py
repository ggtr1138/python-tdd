from selenium import webdriver

#browser = webdriver.Firefox()
# Firefox 45 isn't expected to work with the newest versions of selenium (3.4.0) and geckodriver (0.16.0)
# https://github.com/SeleniumHQ/selenium/issues/3884#issuecomment-296501573

browser = webdriver.Chrome()

browser.get('http://localhost:8000')

assert 'Django' in browser.title
