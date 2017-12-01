#! python3

import json, sys, os
import cipher


## USE OOP LATER


# {user1: (encyrptedPass1, cipherKey), user2: (encyrptedPass2, cipherKey),...}
# [configData1, configData2,...]
configData = {}
listOfUsers = [cipher.generateKey()]

def enableProtectedMode():
    '''Enable protected mode in Internet Explorer'''
    # SECURITY ZONES ARE AS FOLLOWS:
    # 0 is the Local Machine zone
    # 1 is the Intranet zone
    # 2 is the Trusted Sites zone
    # 3 is the Internet zone
    # 4 is the Restricted Sites zone
    # CHANGING THE SUBKEY VALUE "2500" TO DWORD 0 ENABLES PROTECTED MODE FOR THAT ZONE.
    # IN THE CODE BELOW THAT VALUE IS WITHIN THE "SetValueEx" FUNCTION AT THE END AFTER "REG_DWORD".
    #os.system("taskkill /F /IM iexplore.exe")
    # need 1 2 3 4

    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\' 
         
    try:
        for c in range(5):      
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyVal + str(c), 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, '2500', 0, winreg.REG_DWORD, 0)
        print('enabled protected mode')
    except Exception as e:
        print('failed to enable protected mode', e)


##def isNonZeroFile(fpath):
##    '''returns true if file fpath both exists and is not empty'''
##    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def isFile(fpath):
    '''returns true if file fpath exists'''
    return os.path.isfile(fpath)

def isEqualPassword(pw1, pw2):
    '''returns true if strings pw1 and pw2 match, else false'''
    return pw1 == pw2

def userRegistration(username):
    
    print('First time using this program? Need your login credentials')
    
    while True:

        pw1 = winGetPass()
        pw2 = winGetPass('Enter password again: ')

        if isEqualPassword(pw1, pw2):
            
            cipherSuite = cipher.generateCipherSuite(keyForAll) # generate a cipher suite
            cipherKey[username] = cipherSuite
            
            encryptedPass = cipher.encrypt(pw1, cipherSuite)
            
            configData[username] = encryptedPass.decode('UTF-8') # string for JSON
            with open('config.json', 'w') as f:
                data = json.load(f) # get dictionary in json
                updatedData = dict(data.items() + configData.items()) # make new dict with json values + new user
                json.dump(updatedData, f) # write to json
            break

        print('Passwords did not match!')

    # MAYBE MAKE SECOND JSON FOR KEYS
    
    
# Command line version ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def userLogin(): 

    print('Enter your username: ', end='')
    username = input()

    if not isFile('config.json'):  # if the config file doesn't exist, create one
        with open('config.json', 'w') as f:
            json.dump(listOfKeyAndUsers, f)

    with open('config.json', 'r') as f:
        data = json.load(f)
        
        for element in data[1:]: # find the dict containing user information, skip key
            if username not in element:
                userRegistration(username)  # register user
                
            else:         # "login"
                userInfo = element
                break
                while True:
                    
                    password = winGetPass()
                    encryptedPass = cipher.encrypt(password, cipherKey[username])
                    
                    if isEqualPassword(encryptedPass, data[username].encode('UTF-8')):
                        break

                    print('Password incorrect!')


# borrowed***
def winGetPass(prompt='Password: ', promptChar='*', stream=None):
    '''Prompt for password with echo off, using Windows getch().'''
##    if sys.stdin is not sys.__stdin__:
##        return fallback_getpass(prompt, stream)
    import msvcrt
    for c in prompt:         
        msvcrt.putwch(c)        # prints the prompt to the terminal
    pw = ''
    while True:
        c = msvcrt.getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':         # CTRL-c
            raise KeyboardInterrupt
        if c == '\b':
            if pw == '':
                pass
            else:
                pw = pw[:-1]
                msvcrt.putwch('\b')
                msvcrt.putwch(' ')
                msvcrt.putwch('\b')
        else:
            pw = pw + c
            msvcrt.putwch(promptChar)
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw




##   #read data from file
##with open('config.json', 'r') as f:
##    config = json.load(f)
##
##  #edit the data
##config['key3'] = 'value3'
##
###write it back to the file
##with open('config.json', 'w') as f:
##    json.dump(config, f)









##uname.send_keys(config['user']['name'])
##pword.send_keys(config['user']['password'])  
