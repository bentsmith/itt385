import imapclient
import getpass
import backports.ssl

context = backports.ssl.SSLContext(backports.ssl.SSLContext.protocol.TLS)
user = input("Enter Username: ")
passwd = getpass.getpass("Enter Password: ")

conn = imapclient.IMAPClient("172.22.80.39", ssl=True)