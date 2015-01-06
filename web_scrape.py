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

i = 0
max_i = 2

while True:
    i = i + 1

    if i >= max_i:
        break

    newWebbis = webbis.fetchExternal(str(i))
    if newWebbis == None:
        continue

    sql_handle.store(newWebbis)
    sql_handle.update_last(i)
    
# Send email
