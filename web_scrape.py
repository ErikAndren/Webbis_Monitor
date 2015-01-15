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
    
    message = 'Subject: %s\n\n%s' % ("En webbismatchning har hittats", "Testing")
    server.sendmail("erik.andren@gmail.com", ["erik.andren@gmail.com"], message)
    server.quit()

#mail_passwd = raw_input('Enter mail password:')

sql_handle = webbis_sql.WebbisSql('webbis.db')

last_stored_entry = sql_handle.fetch_last_entry()
print "Stored entry is ", str(last_stored_entry)
# i = last_stored_entry
i = 0
none_cnt = 0
max_i = 3

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

    # Check if any of the rules matches the newly downloaded entry
    rule_match_cursor = sql_handle.rule_match(newWebbis)
    while True:
        result_row = rule_match_cursor.fetchone()
        if result_row == None:
            break
    
        print "Found match", result_row
#        send_email(


    
