#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#Scrapes the webbis page

from lxml import html
from lxml import cssselect
import requests
import sys
import webbis
import webbis_sql

webbis_id = '4555'

sql_handle = webbis_sql.WebbisSql('webbis.db')

page = requests.get('http://www.akademiska.se/sv/Webbisar/Webbis/?WebbisID=' + webbis_id)
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

# FIXME: Possible to replace with XPath equivalent to remove cssselect dependency
meta_content = tree.cssselect('meta[property="og:title"]')[0].get('content')

print 'Parents: ', parents[0]
print 'Gender: ', gender[0]
print 'Name: ', name[0]
print 'Birth date: ', birthdate[0]
print 'Birth time: ', birthtime[0]
print 'Weight: ', weight[0]
print 'Length: ', length[0]
print 'City: ', city[0]
print 'Comment: ', comment[0]
print 'Content: ', meta_content

newWebbis = webbis.Webbis(webbis_id, parents[0], gender[0], name[0], birthdate[0], birthtime[0], weight[0], length[0], city[0], comment[0])

# Store in database
sql_handle.store(newWebbis)

# Send email
