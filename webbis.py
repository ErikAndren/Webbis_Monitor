#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Webbis class definition

from lxml import html
from lxml import cssselect
import requests
import sys

class Webbis:
    'Class containing all data for a Webbis'

    def __init__(self, webid, parents, gender, name, birthdate, birthtime, weight, length, city, comment):
        self.webid = webid
        self.parents = parents
        self.gender = gender
        self.name = name
        self.birthdate = birthdate
        self.birthtime = birthtime
        self.weight = weight
        self.length = length
        self.city = city
        self.comment = comment

    def displayWebbis(self):
        print "Webid: ", self.webid, ", Parents: ", self.parents, ", Gender: ", self.gender, ", Name: ", self.name, ", Birthdate", self.birthdate, ", Birthtime ", self.birthtime, ", Weight ", self.weight, ", Length ", self.length, ", City ", self.city, ", Comment ", self.comment

    def fetchExternal(self, webbis_id):
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

        newWebbis = Webbis(webbis_id, parents[0], gender[0], name[0], birthdate[0], birthtime[0], weight[0], length[0], city[0], comment[0])

        return newWebbis
