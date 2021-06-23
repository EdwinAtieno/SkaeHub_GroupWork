#import webdriver from selenium library
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException
twitter_handle = input('Please input your Twitter handle here: ')

# The ChromeDriver class starts the ChromeDriver server process at creation and terminates it when quit is called
# But one can change the driver depending on engine e.g. Firefox,
driver = webdriver.Chrome()

# Tell the webdriver the time to wait before sending a "No such Element Exception"
driver.implicitly_wait(100)

# check incase of an error
try:
    driver.get('http://twitter.com/'+twitter_handle)

# error expexcted
except WebDriverException as e:
    print("An error occured ", e)

# Process to be done when there is no error
else:
    try:

        #opens the browser based on the twitter handle displaying the profile
        web_element = driver.find_element_by_xpath('//a[@href="/' + twitter_handle + '/followers"]')
    #checks an error
    except NoSuchElementException as e:
        print("An error occured ", e)

    #it prints the number of followers then closes the chrome openned
    else:
        print (web_element.text)

        # method to close & destroy both the WebDriver and Web Browser instances gracefully after each run of Test Execution.
        driver.quit()