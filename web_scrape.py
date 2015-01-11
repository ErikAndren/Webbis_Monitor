#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#Scrapes the webbis page

import webbis
import webbis_sql
import smtplib

# Send email
def send_email(username, password):
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail("erik.andren@gmail.com", ["erik.andren@gmail.com"], "Testing")
    server.quit()

#mail_passwd = raw_input('Enter mail password:')

sql_handle = webbis_sql.WebbisSql('webbis.db')

last_stored_entry = sql_handle.fetch_last_entry()
print "Stored entry is ", str(last_stored_entry)
i = last_stored_entry
none_cnt = 0
max_i = 10000

#send_email("erik.andren@gmail.com", mail_passwd)

while True:
    i = i + 1

    if i >= max_i:
        break

    newWebbis = webbis.fetchExternal(str(i))
    if newWebbis == None:
        none_cnt = none_cnt + 1
        if none_cnt >= 3:
            break
        continue

    sql_handle.store(newWebbis)
    sql_handle.update_last(i)
    
