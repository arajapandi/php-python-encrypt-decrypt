#!/usr/bin/env python2
#encoding: UTF-8

# Python Class for AES encryption
"""
    Example Usage
    enc_str = cipher.encrypt('secret')
    enc_str = cipher.decrypt(enc_str)
    print enc_str; #secret
"""

from Crypto.Cipher import AES
import base64
import hashlib
import sys




class MyCypher:
    #Default Key for encryption
    rawkey      = 'asdfa923aksadsYahoasdw998sdsads'
    method      = AES.MODE_CFB
    blocksize   = 32  # 16, 32..etc
    padwith     = '`' # padding value for string  
    
    #lambda function for padding
    pad         = lambda self, s: s + (self.blocksize - len(s) % self.blocksize) * self.padwith
    
    """
    construct for cypher class - get, set key and iv
    """
    def __init__(self, iv, key=''):
        
        if(not key): 
            key = self.rawkey
            
        self.key    = key
        self.iv     = iv
    
    """
    get hased key - if key is not set on init, then default key wil be used
    """
    def getKEY(self):
        if(not self.key):
            sys.exit()
            
        return hashlib.sha256(self.key).hexdigest()[:32]
    
    """
    get hashed IV value - if no IV values then it throw error
    """
    def getIV(self):
        if(not self.iv):
            sys.exit()
            
        return hashlib.sha256(self.iv).hexdigest()[:16]
    
    """
    Encrypt given string using AES encryption standard
    """
    def encrypt(self, raw):
        cipher = AES.new(self.getKEY(), self.method, self.getIV(), segment_size=128)
        return base64.b64encode(cipher.encrypt(self.pad(raw)))
    
    """
    Decrypt given string using AES standard
    """
    def decrypt(self, encrypted):
        encrypted = base64.b64decode(encrypted)
        cipher = AES.new(self.getKEY(), self.method, self.getIV(), segment_size=128)
        return cipher.decrypt(encrypted).rstrip(self.padwith)
