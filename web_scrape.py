#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#Scrapes the webbis page

from lxml import html
from lxml import cssselect
import requests

import sys

page = requests.get('http://www.akademiska.se/sv/Webbisar/Webbis/?WebbisID=4555')
tree = html.fromstring(page.text)

parents = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bparenttxt"]/text()')

gender = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bgendertxt"]/text()')

name = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bNametxt"]/text()')

birthdate = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bbirthdatetxt"]/text()')

birthtime = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bbirthtimetxt"]/text()')

weight = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bweighttxt"]/text()')

length = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_blengthtxt"]/text()')

city = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bcitytxt"]/text()')

comment = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bcommenttxt"]/text()')

# FIXME: Possible to replace with 
meta_content = tree.cssselect('meta[property="og:title"]')[0].get('content')

# http://stackoverflow.com/questions/22745876/python-print-unicode-list
# Convert list elements to unicode
parent_utf = repr([x.encode(sys.stdout.encoding) for x in parents]).decode('string-escape')
name_utf = repr([x.encode(sys.stdout.encoding) for x in name]).decode('string-escape')
city_utf = repr([x.encode(sys.stdout.encoding) for x in city]).decode('string-escape')
comment_utf = repr([x.encode(sys.stdout.encoding) for x in comment]).decode('string-escape')

print 'Parents: ', parent_utf
print 'Gender: ', gender
print 'Name: ', name_utf
print 'Birth date: ', birthdate
print 'Birth time: ', birthtime
print 'Weight: ', weight
print 'Length: ', length
print 'City: ', city_utf
print 'Comment: ', comment_utf

print 'Content: ', meta_content

# Store in database


# Send email
