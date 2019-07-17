#!/usr/bin/env python

import pwn
import re

greeting_message = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"

xor_string = '\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x5c\x10\x06\x06\x18\x45\x51\x00\x5d\x00'

print re.findall('picoCTF{.*?}', pwn.xor(greeting_message, xor_string))[0]
 
