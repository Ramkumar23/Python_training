import pexpect
import getpass
m_p = pexpect.spawn('python gmail_pr.py')
m_p.expect('gmail')
m_p.sendline('raagavendran@gmail.com')
password = getpass.getpass()
m_p.sendline(password)
m_p.expect('to')
m_p.sendline('raagavendran@gmail.com')
m_p.expect('sub')
m_p.sendline('test')
mp_p.close()
