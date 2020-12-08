import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://formspree.io/f/mbjpzrvv'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	email = name.lower() + name_extra + '@outlook.com'
	discord = ''.join(random.choice(chars) for i in range(8))
	message = ''.join(random.choice(chars) for i in range(8))
        
	requests.post(url, allow_redirects=False, data={
                'email@email.com': email,
                'Adam': name,
		'Hi!': message,
	})
