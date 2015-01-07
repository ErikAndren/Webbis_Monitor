#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import webbis
import sys

class WebbisSql:
    'Class containing the sql stitching'

    def __init__(self, db):
        self.con = lite.connect(db)

        with self.con:
            cur = self.con.cursor()    

            # Create table
            cur.execute("CREATE TABLE IF NOT EXISTS LAST_ID(Id INT primary key, last INT)")
                
            # Create last id control, do not update 
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
            twingender TEXT, \
            twinname TEXT, \
            twinbirthdate TEXT, \
            twinbirthtime TEXT, \
            twinweight TEXT, \
            twinlength TEXT, \
            twincity TEXT, \
            comment TEXT \
            )")

            self.con.commit();

    def store(self, webbis):
        self.con.execute("INSERT OR REPLACE INTO WEBBIS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (webbis.webid,  webbis.parents,  webbis.gender,  webbis.name,  webbis.birthdate,  webbis.birthtime,  webbis.weight,  webbis.length,  webbis.city,  webbis.twingender, webbis.twinname, webbis.twinbirthdate, webbis.twinbirthtime, webbis.twinweight, webbis.twinlength, webbis.twincity, webbis.comment))
        self.con.commit();

    def update_last(self, new_id):
        update_string = "UPDATE LAST_ID SET last = MAX(Id, " + str(new_id) + ") WHERE Id = 0";
        self.con.execute(update_string)
        self.con.commit();

    def fetch_last_entry(self):
        cur = self.con.cursor()
        cur.execute("SELECT last FROM LAST_ID WHERE Id = 0");
        return cur.fetchone()[0]
        



