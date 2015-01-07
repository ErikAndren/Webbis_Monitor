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

last_stored_entry = sql_handle.fetch_last_entry()
print "Stored entry is ", str(last_stored_entry)
i = last_stored_entry
none_cnt = 0

while True:
    i = i + 1

    if i >= max_i:
        break

    newWebbis = webbis.fetchExternal(str(i))
    if newWebbis == None:
        none_cnt++
        if none_cnt >= 3:
            break
        continue

    sql_handle.store(newWebbis)
    sql_handle.update_last(i)
    
# Send email
