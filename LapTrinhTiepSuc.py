#!/usr/bin/python

# -*- coding: utf-8 -*-

import random
import codecs
f = codecs.open("laptrinh_data.txt","r","utf-16")
s = f.read().split("LT - ")

fo = open("laptrinhtiepsuc.html", "w")
ft = open("laptrinhtiepsuc_template.html", "r")
fo.write(ft.read())
fo.write('<b>'+s[random.randrange(1,7)].encode('utf-8').replace('\n','<br/>')+'</b>')
fo.close()
ft.close()
f.close()
import webbrowser
webbrowser.open('laptrinhtiepsuc.html',new=2)
