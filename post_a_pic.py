#!/usr/bin/env python
# coding=utf-8

import sendweibo
addr = raw_input('which picture do you want to post?')
s = raw_input('input some description?')
if not addr and not s:
	sendweibo.post_pic()
elif not addr:
	sendweibo.post_pic(s)
else:
	sendweibo.post_pic(s, addr)
	
	

