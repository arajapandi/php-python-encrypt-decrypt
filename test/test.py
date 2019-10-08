#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
from MyCypher import MyCypher


"""
This file will print encrypted / decrypted values based on input
"""

if __name__ == "__main__":

    flag = sys.argv[1]
    secret = sys.argv[2]
    iv = sys.argv[3]

    cipher = MyCypher(iv)

    if (flag == 'encrypt'):
        print(cipher.encrypt(secret).decode("utf-8"))

    if (flag == 'decrypt'):
        print(cipher.decrypt(secret.encode("utf-8")))
