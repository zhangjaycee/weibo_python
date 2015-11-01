#!/usr/bin/env python
# coding=utf-8
import httplib,json,urllib,webbrowser,time
from xml.dom.minidom import parseString
from weibo import APIClient
from re import split
import urllib2
import urllib

APP_KEY = '136591678' #youre app key
APP_SECRET = '39854172c17f36fdb2a82bcf446719b5' #youre app secret  
CALLBACK_URL = 'http://www.163.com'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print "[Step 1]open this url and copy the code:"
print "[url]",url
code = raw_input("[Step 2]please paste the code here:")
r = client.request_access_token(code)
access_token = r.access_token # The token return by sina
expires_in = r.expires_in
print "[Request Succeed]:"
print "[access token]",access_token
print "[expires in]",expires_in
if access_token:
	print "[Writing to the file..]"
	f = open("token.txt", "w")
	f.write(access_token)
	f.write("\n")
	f.write(str(expires_in))
	f.close
	print "[Write file Succeed]"
print "[Done!]"
