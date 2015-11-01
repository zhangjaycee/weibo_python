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

token_f = open("token.txt", "r")
access_token = token_f.readline().strip()
expires_in = token_f.readline().strip()

client.set_access_token(access_token, expires_in)

def get_user_id():
	code = get_code()
	r = client.request_access_token(code).uid
	return r
def get_user_info():
	r=client.get.users__show(uid=get_user_id())
	return r
def get_format_time(times):
	return time.strftime("%Y.%m.%d %H:%M:%S", time.strptime("%s"%times, "%a %b %d %H:%M:%S +0800 %Y"))
def repost(ids,text):
	test = client.get.statuses__mentions()
	print test.statuses[0].text,test.statuses[0].user.screen_name
	ids = test.statuses[0].id
	return client.post.statuses__repost(id=ids,status=text)
def post(texts):
	return client.post.statuses__update(status=texts)
def get_mention():
	test = client.get.statuses__mentions().statuses[0]
	return ('%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s')%(get_format_time(test.created_at),test.id,test.user.id,test.user.screen_name,test.text)
def get_comments():
	comments = client.get.comments__to_me(count=1).comments[0].status
	return ('%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s')%(get_format_time(comments.created_at),comments.id,comments.user.id,comments.user.screen_name,comments.text)
def send_comments(ids,texts):
	client.post.comments__create(id=ids,comment=texts)
def post_pic(texts = 'post a picture', addr = '/home/jaycee/Desktop/test.png'):#post_pic('hello world')
	pics = open(addr, 'rb')
	return client.upload.statuses__upload(status=texts,pic=pics)



