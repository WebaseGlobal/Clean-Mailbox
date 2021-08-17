# Clean-Mailbox

# Select INBOX folder
imap.select("INBOX")

# Select SPAM folder
imap.select("SPAM")

# Retrieve All Emails
status, messages = imap.search(None, "ALL")

# Retrieve Emails by Subject
status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')

# Retrieve Emails from Specific Date
status, messages = imap.search(None, 'SINCE "01-JAN-2021"')

# Retrieve Emails until Date
status, messages = imap.search(None, 'BEFORE "01-JAN-2021"')

# SSL
imaplib.IMAP4_SSL("imap.domain.com")

# NO SSL
imaplib.IMAP4("imap.domain.com")
