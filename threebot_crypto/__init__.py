#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import ConfigParser
import msgpack
import zlib
import cPickle as pickle

__all__ = ["encrypt", "decrypt", "SECRET_KEY"]

configfile = '/etc/3bot/config.ini'

if os.path.isfile(configfile):
    Config = ConfigParser.ConfigParser()
    Config.read(configfile)
else:
    print "No configfile found in: '%s'" % configfile
    sys.exit(2)

try:
    # Read secret key - never share yours!
    SECRET_KEY = Config.get('3bot-settings', 'SECRET_KEY')
except:
    print "Invalid configfile in: '%s'" % configfile
    sys.exit(2)

# Salt size in bytes
SALT_SIZE = 32

# Number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20

# The size multiple required for AES
AES_MULTIPLE = 16


def generate_key(secret_key, salt, iterations):
    assert iterations > 0
    key = secret_key + salt
    for i in range(iterations):
        key = hashlib.sha256(key).digest()
    return key


def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text


def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])
    text = padded_text[:-padding_size]
    return text


def encrypt(json_dict, secret_key=SECRET_KEY):
    obj = msgpack.packb(json_dict, use_bin_type=True)
    p = pickle.dumps(obj, protocol=-1)
    plaintext = zlib.compress(p)
    salt = Crypto.Random.get_random_bytes(SALT_SIZE)
    key = generate_key(secret_key, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad_text(plaintext, AES_MULTIPLE)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext_with_salt = salt + ciphertext
    return ciphertext_with_salt


def decrypt(ciphertext, secret_key=SECRET_KEY):
    salt = ciphertext[0:SALT_SIZE]
    ciphertext_sans_salt = ciphertext[SALT_SIZE:]
    key = generate_key(secret_key, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext_sans_salt)
    com_plaintext = unpad_text(padded_plaintext)
    try:
        dec_plaintext = zlib.decompress(com_plaintext)
    except zlib.error:
        sys.stderr.write("\nCannot decrypt message. Maybe your keys are not identic.\n")
        return None
    unp_plaintext = pickle.loads(dec_plaintext)
    plaintext = msgpack.unpackb(unp_plaintext, encoding='utf-8')
    return plaintext
