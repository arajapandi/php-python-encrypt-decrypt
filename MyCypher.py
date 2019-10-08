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
    # Default Key for encryption
    rawkey = 'asdfa923aksadsYahoasdw998sdsads'
    method = AES.MODE_CFB
    blocksize = 32  # 16, 32..etc
    padwith = '`'  # padding value for string

    # lambda function for padding
    def pad(self, s): return s + (self.blocksize - len(s) %
                                  self.blocksize) * self.padwith

    def __init__(self, iv, key=''):
        """
        construct for cypher class - get, set key and iv
        """
        if(not key):
            key = self.rawkey

        self.key = key
        self.iv = iv

    def getKEY(self):
        """
        get hashed key - if key is not set on init, then default key wil be used
        """
        if(not self.key):
            sys.exit()

        return hashlib.sha256(self.key.encode('utf-8')).hexdigest()[:32]

    def getIV(self):
        """
        get hashed IV value - if no IV values then it throw error
        """
        if(not self.iv):
            sys.exit()

        return hashlib.sha256(self.iv.encode('utf-8')).hexdigest()[:16]

    def encrypt(self, raw):
        """
        Encrypt given string using AES encryption standard
        """
        cipher = AES.new(self.getKEY(), self.method,
                         self.getIV(), segment_size=128)
        return base64.b64encode(cipher.encrypt(self.pad(raw)))

    """
    Decrypt given string using AES standard
    """

    def decrypt(self, encrypted):
        encrypted = base64.b64decode(encrypted)
        cipher = AES.new(self.getKEY(), self.method,
                         self.getIV(), segment_size=128)
        return cipher.decrypt(encrypted).decode('utf-8').rstrip(self.padwith)
