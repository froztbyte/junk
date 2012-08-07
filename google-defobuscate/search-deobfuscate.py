#!/usr/bin/python
from urlparse import urlparse
from urllib import unquote_plus
from sys import argv

url = urlparse(sys.argv[1])
params = dict([part.split('=') for part in url.query.split('&')])
print unquote_plus(params['url'])
