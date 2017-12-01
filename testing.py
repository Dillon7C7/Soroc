#! python3

from selenium import webdriver
import json, winreg, setup, cipher

def main():
    
    setup.userLogin()
    
    url = 'http://timetracker.soroc.com'

    setup.enableProtectedMode()
    browser = webdriver.Ie()
    browser.maximize_window()
    browser.get(url)

   #read data from file
    with open('config.json', 'r') as f:
        configData = json.load(f)
    print(configData['password'])
    print(configData['password'].encode('UTF-8'))
    deee = configData['password'].encode('UTF-8')
    print(setup.cipherSuite)
    print(cipher.decrypt(deee, setup.cipherSuite))


if __name__ == '__main__':

    main()
