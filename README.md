# SnakeMail v.0.0.1


Python script for Sendmail
AWS SES Optimized

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

## Requirements:

- python2.7

## Usage:

$ python SnakeMail.py -H 'host/domain' -p [port] -a -s -f 'Email-From' -t 'Email-To' -u 'Subject' -m 'Message' -d [0-4]

Options:

host, --HOST, -h               Configure IP or domain of SMTP Server

port, --port, -p               Configure Port of SMTP Server. e.g: 25 or 465 or 587 Default Value = 25

-a                             Use authentication. Configure user credentials in the script

-s                             Use TLS/SSL to connect SMTP server

-f, --efrom                    Configure the FROM e-mail. User a valid e-mail or verified e-mail/domain in case of AWS SES

-t, --to                       Configure the recipients e-mail. Could be used for more than one e-mail using commas to separate it. e.g: 'test@mail.com,test2.mail.com'

-u, --Subject                  Configure the e-mail Subject

-m, --message                  Configure the e-mail body Message (Don't use html tags here for while)

-d                             Configure the debug option for verbose sending. Values from 0 to 4. Default value = 0

help, --help, h
