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



newWebbis = webbis.fetchExternal(webbis_id)

# Send email
