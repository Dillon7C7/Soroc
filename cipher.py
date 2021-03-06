from cryptography.fernet import Fernet

def generateCipherSuite():
    '''Generates a key and a cipher suite using that key; returns that suite'''
    key = Fernet.generate_key()
    cipherSuite = Fernet(key)
    return cipherSuite

def encrypt(plainText, cipherSuite):
    '''Takes a string, Fernet object and returns the corresponding encrypted bytes literal'''
    encodedPass = plainText.encode('UTF-8') # convert password (string) to bytes literal
    cipherText = cipherSuite.encrypt(encodedPass) # encrypt
    return cipherText
    
def decrypt(cipherText, cipherSuite):
    '''Takes a bytes literal, Fernet object and returns the corresponding decrypted string'''
    encodedPlainText = cipherSuite.decrypt(cipherText) # decrypt
    plainText = encodedPlainText.decode('UTF-8') # convert decrypted password to string
    return plainText
