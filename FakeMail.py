#!/usr/bin/env python
import smtplib

SERVER = "localhost"

FROM = "akterf@ecs.csus.edu"
TO = ["chaiq@ecs.csus.edu"] # must be a list

SUBJECT = raw_input('Enter Title Here: ')#enter the title

TEXT = raw_input('Enter Message Here: ')# enter message

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
