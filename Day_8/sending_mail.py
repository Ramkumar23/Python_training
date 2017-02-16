

import smtplib
import getpass
import sys
host = "smtp.gmail.com"
port = 587
server =smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username = raw_input("Enter Mail Id :")
v1=sys.argv[1]
v2=sys.argv[2]
v3=sys.argv[3]
password=getpass.getpass("Enter Password :")
server.login(username,password)
to =v1
sub =v3

file =open(v2,'r')
mes = file.read()
message = "subject:  %s\n%s"%(sub,mes)
server.sendmail(username,to,message)


