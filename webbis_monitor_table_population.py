#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('webbis.db')

with con:
    cur = con.cursor()    

    # Create table
    cur.execute("CREATE TABLE IF NOT EXISTS LAST_ID(Id INT primary key, last INT)")
    
    # Create last id control
    cur.execute("INSERT OR IGNORE INTO LAST_ID VALUES(0, 0)")

    # Create webbis table
    cur.execute("Create TABLE IF NOT EXISTS WEBBIS( \
    Id INT primary key, \
    parents TEXT, \
    gender TEXT, \
    name TEXT, \
    birthdate TEXT, \
    birthtime TEXT, \
    weight INT, \
    length INT, \
    city TEXT,  \
    comment TEXT \
    )")

    
