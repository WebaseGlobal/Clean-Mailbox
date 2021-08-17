import imaplib
import email
import io
import sys
from email.header import decode_header
from getpass import getpass

username = ""
imapinput = ""

text = '''Pass an arguments to run the script:
    -h                       : help
    -m <sample@domain.com>   : email
    -i <mail.domain.com>     : imap'''

if len(sys.argv) <4:
    print(text)
    sys.exit()

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
    print(text)
    sys.exit()
elif '-m' in sys.argv and '-i' in sys.argv:
    for i in range(len(sys.argv)):
        if '-m' in sys.argv[i]:
            username = sys.argv[i+1]
        if '-i' in sys.argv[i]:
            imapinput = sys.argv[i+1]
else:
    print('Unknown parameters. Please run cleanMailbox.py -h to display help.')
    sys.exit()

print('Please type password below:')
password = getpass()

try:
    print('Connecting...')
    imap = imaplib.IMAP4(imapinput)
except:
    print('Invalid IMAP (Failure).')
    sys.exit()

try:
    imap.login(username, password)
except imaplib.IMAP4.error:
    print("Authentication Problem. Please try again later.")
    sys.exit()

imap.select("INBOX")

count = 0
file1 = io.open('blacklist', encoding='utf-8')
Lines = file1.readlines()
for line in Lines:
    status, messages = imap.search(None, 'FROM '+line)
    print(line)

    messages = messages[0].split(b' ')
    for mail in messages:
        if mail:
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode('utf8')
                    print("Deleting", subject)
            imap.store(mail, "+FLAGS", "\\Deleted")
imap.expunge()
imap.close()
imap.logout()