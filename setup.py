#! python3

import json, sys
import cipher

# {user: username, pass: password}
configData = {}
configData.setdefault('user', '')
configData.setdefault('password', '')
cipherSuite = None

def isEqualPassword(pw1, pw2):
    return pw1 == pw2

def UserRegistration(newUsername): 
    
    while True:

        pw1 = win_getpass()
        pw2 = win_getpass('Enter password again: ')

        if isEqualPassword(pw1, pw2):
            global cipherSuite
            cipherSuite = cipher.generateCipherSuite() # generate a cipher suite
            encryptedPass = cipher.encrypt(pw1, cipherSuite)  
            break

        print('Passwords did not match!')

    configData['user'] = newUsername
    configData['password'] = encryptedPass.decode('UTF-8') # string for JSON


    # write to JSON
    with open('config22.json', 'w') as f:
        json.dump(configData, f)



# borrowed***
def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getch()."""
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
            msvcrt.putwch('*')
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
