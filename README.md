# 3bot-crypto

The [3bot-crypto](https://github.com/3bot/3bot-crypto) toolkit contains various cryptographic modules for the 3bot ecosystem.

# Installation 

This package is basically installed as dependency from [3bot](https://github.com/3bot/3bot) and the [3bot-worker](https://github.com/3bot/3bot-worker) 
but could also be used by 3rd party apps and modules that implements against the 3bot API and endpoints. 
It implements the packing, compressing and encryption for messages to be transported over the wire. 

Install the latest, stable package from PyPI:
	
	pip install threebot-crypto


To get the latest commit from GitHub

	pip install -e git+git://github.com/3bot/threebot-crypto.git#egg=threebot_crypto


# Configuration

In /etc/3bot/config.ini add your worker `SECRET_KEY`. This must be set on my.3bot.io or your instance as well.
 

# Usage

	import threebot_crypto
	FLAGS = 0
	data = {'number': 1, 'year': 2014, 'name': 'Joe Block'}
	
	# Encrypt and send data to worker
	request = threebot_crypto.encrypt(data)
	client.send(request, flags=FLAGS)
	
	# Receive answer from worker and decrypt
    response = conn.client.recv(FLAGS)
    result = threebot_crypto.decrypt(response)
	
	

# Dependencies

3bot-crypto use the following libraries.

* Python 
* pycrypto >= 2.6.1
* msgpack-python >= 0.4.1 

# History & Changelog

## 1.0.15

Release date: 01 Sep 2014

### What's new?

* Stable release
