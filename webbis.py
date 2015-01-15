#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Webbis class definition

from lxml import html
from lxml import cssselect
import requests
import sys

class Webbis:
    'Class containing all data for a Webbis'

    def __init__(self, webid, parents, gender, name, birthdate, birthtime, weight, length, city, twingender, twinname, twinbirthdate, twinbirthtime, twinweight, twinlength, twincity, comment):
        self.webid = webid
        self.parents = parents
        self.gender = gender
        self.name = name
        self.birthdate = birthdate
        self.birthtime = birthtime
        self.weight = weight
        self.length = length
        self.city = city

        self.twingender = twingender
        self.twinname = twinname
        self.twinbirthdate = twinbirthdate
        self.twinbirthtime = twinbirthtime
        self.twinweight = twinweight
        self.twinlength = twinlength
        self.twincity = twincity

        self.comment = comment

        # self.displayWebbis()

    def displayWebbis(self):
        print "Webid: ", self.webid, ", Parents: ", self.parents, ", Gender: ", self.gender, ", Name: ", self.name, ", Birthdate: ", self.birthdate, ", Birthtime: ", self.birthtime, ", Weight: ", self.weight, ", Length: ", self.length, ", City: ", self.city, ", Twin gender: ", self.twingender, " Twin name: ", self.twinname, " Twin birth date: ", self.twinbirthdate, " Twin birth time: ", self.twinbirthtime, " Twin weight: ", self.twinweight, " Twin length: ", self.twinlength, " Twin city: ", self.twincity, ", Comment ", self.comment

# FIXME: Migrate to static method instead
def fetchExternal(wid):
    page = requests.get('http://www.akademiska.se/sv/Webbisar/Webbis/?WebbisID=' + wid)
    tree = html.fromstring(page.text)

    parents = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bparenttxt"]/text()')
    gender = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bgendertxt"]/text()')
    name = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bNametxt"]/text()')
    birthdate = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bbirthdatetxt"]/text()')
    birthtime = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bbirthtimetxt"]/text()')
    weight = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bweighttxt"]/text()')
    length = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_blengthtxt"]/text()')
    city = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bcitytxt"]/text()')

    twingender = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwingendertxt"]/text()')
    twinname = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwinnametxt"]/text()')
    twinbirthdate = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwinbirthdatetxt"]/text()')
    twinbirthtime = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwinbirthtimetxt"]/text()')
    twinweight = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwinweighttxt"]/text()')
    twinlength = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwinlengthtxt"]/text()')
    twincity = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_btwincitytxt"]/text()')

    comment = tree.xpath('//*[@id="ctl00_MainRegion_MainContentRegion_webbisUnit_bcommenttxt"]/text()')

    #HACK: For some reason comment parsing fails when handling twins
    if len(parents) == 0:
        parents = [""]

    if len(gender) == 0:
        gender = [""]

    if len(name) == 0:
        name = [""]

    if len(birthdate) == 0:
        birthdate = [""]

    if len(birthtime) == 0:
        birthtime = [""]
    
    if len(weight) == 0:
        weight = [""]

    if len(length) == 0:
        length = [""]

    if len(city) == 0:
        city = [""]

    if len(twingender) == 0:
        twingender = [""]

    if len(twinname) == 0:
        twinname = [""]

    if len(twinbirthdate) == 0:
        twinbirthdate = [""]

    if len(twinbirthtime) == 0:
        twinbirthtime = [""]
    
    if len(twinweight) == 0:
        twinweight = [""]

    if len(twinlength) == 0:
        twinlength = [""]

    if len(twincity) == 0:
        twincity = [""]

    if len(comment) == 0:
        comment = [""]

    # FIXME: Possible to replace with XPath equivalent to remove cssselect dependency
    meta_content = tree.cssselect('meta[property="og:title"]')[0].get('content')
    
    if meta_content == 'Webbis':
        return None

    newWebbis = Webbis(wid, parents[0].rstrip(), gender[0].rstrip(), name[0].rstrip(), birthdate[0].rstrip(), birthtime[0].rstrip(), weight[0].rstrip(), length[0].rstrip(), city[0].rstrip(), twingender[0].rstrip(), twinname[0].rstrip(), twinbirthdate[0].rstrip(), twinbirthtime[0].rstrip(), twinweight[0].rstrip(), twinlength[0].rstrip(), twincity[0].rstrip(), comment[0].rstrip())

    return newWebbis
