#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#Scrapes the webbis page

from lxml import html
from lxml import cssselect
import requests
import sys
import webbis
import webbis_sql

sql_handle = webbis_sql.WebbisSql('webbis.db')

i = 1

while True:
    newWebbis = webbis.fetchExternal(str(i))
    if newWebbis == None:
        break
    
    i = i + 1

# Send email
