#connect to SSH by python pexpect

from pexpect import pxssh
import getpass
s = pxssh.pxssh()
s.force_password = True
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
s.login (hostname, username, password)
s.sendline('ls')
s.prompt()
print s.before
