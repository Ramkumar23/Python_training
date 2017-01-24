import pexpect
import sys
import getpass
m = pexpect.spawn('python gmail_sample.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline("dhanushamail@gmail.com")
m.expect("Password:")
password = getpass.getpass()
m.sendline(password)
m.expect("To address :")
m.sendline("dhanushamail@gmail.com")
m.expect("Subject :")
m.sendline("test")
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")
m.sendline("end")
m.expect("test has been send to dhanushamail@gmail.com")
m.close()
