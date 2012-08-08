#!/usr/bin/python
"""
google-search-deobfuscate

argv[1] is the input, stdout is filtered

code by froztbyte. MIT license, 2012
"""

from urlparse import urlparse
from urllib import unquote_plus
from sys import argv

url = urlparse(sys.argv[1])
params = dict([part.split('=') for part in url.query.split('&')])
print unquote_plus(params['url'])
