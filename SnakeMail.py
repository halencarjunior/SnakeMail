#!/usr/bin/env python

############################################################
#
# SnakeMail - Python Script for Sendmail
# Version AWS Simple Email Service 0.0.1
# Script by: Humberto Junior
#
############################################################

import argparse
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

VERSION="0.01"
MESSAGE="SnakeMail - Python Script for SendMail"

############################################################
#
# AWS SES User and Password Configuration
#
usuario = 'YOUR-USER-HERE'
senha = 'YOUT-PASSWORD-HERE'

def send_plain(host,port,efrom,to,subject,message,debug=0):

    COMMASPACE = ', '
    # Formating Email Body
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = efrom
    msg['To'] = to
    msg.attach(MIMEText(message,'plain'))

    print("==> Sending Email")
    print("[-] Using Plain - NO SLL - AUTH OK\n")

    try:
    	server = smtplib.SMTP(host, port)
    	server.set_debuglevel(debug)
    	server.ehlo()
    	server.login(usuario, senha)
    	server.sendmail(efrom,to, msg.as_string())
    	server.quit()

        print('--------------------------------------------------')
    	print('[+] Email Sent\n')
        print('[+] From: ' + efrom)
        print('[+] To: ' + to + '\n')

    except NameError as erro:
        print 'Erro Sending email ' + erro


def send_plain_noauth(host,port,efrom,to,subject,message,debug=0):

    COMMASPACE = ', '
    # Formating Email Body
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = efrom
    msg['To'] = to
    msg.attach(MIMEText(message,'plain'))

    print("==> Sending Email")
    print("[-] Using Plain - NO SLL - NO AUTH\n")

    try:
    	server = smtplib.SMTP(host, port)
    	server.set_debuglevel(debug)
    	server.ehlo()
    	server.sendmail(efrom,to, msg.as_string())
    	server.quit()

        print('--------------------------------------------------')
    	print('[+] Email Sent\n')
        print('[+] From: ' + efrom)
        print('[+] To: ' + to + '\n')

    except NameError as erro:
        print 'Error Sending email ' + erro

def send_ssl(host,port,efrom,to,subject,message,debug=0):

    COMMASPACE = ', '
    # Formating Email Body
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = efrom
    msg['To'] = to
    msg.attach(MIMEText(message,'plain'))

    print("==> Sending Email")
    print("[-] Using Plain - SLL OK - AUTH OK\n")

    try:
    	server = smtplib.SMTP(host, port)
    	server.set_debuglevel(debug)
    	server.ehlo()
        server.starttls()
    	server.login(usuario, senha)
    	server.sendmail(efrom,to, msg.as_string())
    	server.quit()

    	print('[+] Email Enviado\n')
        print('[+] From: ' + efrom + '\n')
        print('[+] To: ' + to + '\n')

    except NameError as erro:
        print 'Error Sending email ' + erro

def main():
    parser = argparse.ArgumentParser(prog='SnakeMail', formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
  _________              __             _____         .__.__
 /   _____/ ____ _____  |  | __ ____   /     \ _____  |__|  |
 \_____  \ /    \\__  \ |  |/ // __ \ /  \ /  \\__  \ |  |  |
 /        \   |  \/ __ \|    <\  ___//    Y    \/ __ \|  |  |__
/_______  /___|  (____  /__|_ \\___  >____|__  (____  /__|____/
        \/     \/     \/     \/    \/        \/     \/

Version 0.0.1
by Humberto Jr

Script for AWS Simple Email Service

''')
    parser.add_argument('-H', '--host', nargs='?', required=True, help='IP or Hostname')
    parser.add_argument('-p', '--port', nargs='?', type=int, help='Port of Senmail (25,465,587). Default=25', default='25')
    parser.add_argument('-a', '--auth', action='store_true', help='Use Authentication. Need User and Password Configurations')
    parser.add_argument('-s', '--ssl', action='store_true', help='Use TLS for Secure Connection')
    parser.add_argument('-f', '--efrom', nargs='?', type=str, required=True,  help='E-mail sent FROM')
    parser.add_argument('-t', '--to', nargs='?', type=str, required=True, help='Email or e-mail list to send Message')
    parser.add_argument('-u', '--subject', nargs='?', type=str, required=True, help='Email subject')
    parser.add_argument('-m', '--message', nargs='?', type=str, required=True, help='Message body')
    parser.add_argument('-d', '--debug', nargs='?', type=int, help='Set Debug Level 1-4')

    args = parser.parse_args()

    hostip = args.host
    hostport = args.port
    emailfrom = args.efrom
    emailto = args.to
    emailsubject = args.subject
    emailmessage = args.message
    emaildebug = args.debug

    if (args.auth != True and args.ssl != True):
        if (args.debug > 0):
            send_plain_noauth(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage,emaildebug)
        else:
            send_plain_noauth(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage)

    if (args.auth == True and args.ssl != True):
        if (args.debug > 0):
            send_plain(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage,emaildebug)
        else:
            send_plain(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage)

    if (args.ssl == True):
        if (args.debug > 0):
            send_ssl(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage,emaildebug)
        else:
            send_ssl(hostip,hostport,emailfrom,emailto,emailsubject,emailmessage)

if __name__ == '__main__':
    main()
