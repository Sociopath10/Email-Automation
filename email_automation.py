from smtplib import SMTP

conn=SMTP("YOUR SMTP ADDRESS","YOUR PORT NO")
conn.ehlo()
conn.starttls()
log=conn.login("YOUR e-mail","YOUR PASSWORD")
print(log)
#to check if authentication succeeded
message = """From: <your email address>
To: Alpha Test <receipient address>
Subject: SMTP e-mail test\n\n
This is a test e-mail message. or Type any message
"""
status=conn.sendmail("sender's email as above ","receipient email",message)
print(status)
#to check if sendmail() succeeded
conn.quit()
#to close connection 