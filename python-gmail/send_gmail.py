#!/usr/bin/env python
import argparse, sys, smtplib
from email.mime.text import MIMEText

# if __name__ == "__main__":
parser = argparse.ArgumentParser(description='Python Gmail sender')
parser.add_argument('-u','--user', help='Gmail sender username', required=True)
parser.add_argument('-p','--password', help='Gmail sender password', required=True)
parser.add_argument('-t','--to', help='Mailto email address', required=True)
parser.add_argument('-s','--subject', help='Email subject', required=False)
parser.add_argument('-b','--body', help='Email body', required=False)
args = parser.parse_args()

msg = MIMEText(args.body)
msg['Subject'] = args.subject
msg['From'] = args.user
msg['To'] = args.to

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.login(args.user, args.password)
server.sendmail(args.user, args.to, msg.as_string())
server.quit()
