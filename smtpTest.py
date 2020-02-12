import smtplib
import getpass

user = input("Enter username: ")
passwd = getpass.getpass("Enter Password: ")

# Connect to the server
conn = smtplib.SMTP("172.22.80.39", 587)

# Switch to encrypted mode
conn.starttls()

# Authenticate with the email server
conn.login(user, passwd)


# create a message to send
# needs to be in RFC822 format

# todo: should add other headers like Date : Line

mesg =  "To: monnin@localhost\r\n"
mesg += "From: user @ localhost\r\n"
mesg += "Subject: Test from Mark M\r\n"
mesg += "\r\n"

mesg += "This is an email from Mark. Done!"

# todo: should add some error checking for refused email messages
# todo: should protect with a TRY block for other email features

conn.sendmail("User@localhost","monnin@localhost", mesg)

# done? then end the TCP socket

conn.close()
