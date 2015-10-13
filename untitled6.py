# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:22:45 2015

@author: bryan_000
"""

from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('http://www.realclearpolitics.com/epolls/2016/president/2016_presidential_race.html').read()
soup = BeautifulSoup(r)
print type(soup)

print soup.prettify()[0:1000]

from IPython.display import Image
Image('http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png')

from IPython.display import HTML
HTML('<iframe src=http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts width=700 height=500></iframe>')