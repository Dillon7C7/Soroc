#! python3

#import time, sys, json, os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def is_non_zero_file(fpath):
    '''returns true if file fpath both exists and is not empty'''
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

# if a configuration file hasn't been made, setup one
def checkConfiguration():
    if not is_non_zero_file('config.json'):
        import setup
        print('First run of the program? Need your reuse login credentials...')
        print('Enter your name: ', end='')
        username = input()
        configPass.UserRegistration(username)

##with open('config.json', 'r') as f:
##    config = json.load(f)
##
##  #edit the data
##config['key3'] = 'value3'



### JSON
##with open('config.json', 'r') as f:
##    print(json.load(f)['user'])


##caps = DesiredCapabilities.INTERNETEXPLORER
##caps['ignoreProtectedModeSettings'] = True
##
##url = 'http://soroc.com'
##
##driver = webdriver.Ie(capabilities=caps)
##
##nav = driver.get(url)
##nav.maximize_window()
##
##orderID = r'ctl00_ContentPlaceHolder1_txtRecvSorocRef'
##searchButtonID = r'ctl00_ContentPlaceHolder1_cmdSearch'
##reuseCentreLinkID = r'ctl00_ContentPlaceHolder1_dgResult_ctl03_lnkReUse'















##try:
##    driver = webdriver.Ie(capabilities=caps)
##
##    
##except WebDriverException:
##    print('Error (will add specific errors later)')
##    sys.exit()




# send login name and pass
# navigate to reuse application
# loop through dictionary (actually don't need to store data),
# using dictionary information to fill out stuff
# use IDs to fill in information
# open checklist
# use IDs to fill in information
# exit cehcklist
# complete
# next iteration of loop...



##url = driver.command_executor._url
##session_id = driver.session_id
##
##driver = webdriver.Remote(command_executor=url,desired_capabilities={})
##driver.session_id = session_id


#def loginToReuse

