import imapclient
import getpass
import ssl
import pyzmail

# username / password from user input
user = input("Enter username: ")
passwd = getpass.getpass("Enter Password: ")

# get around the un-verified SSL connection by creating our own context
# if we had a "normal" SSL certificate, this would not be needed
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# connect to the IMAP server
conn = imapclient.IMAPClient("172.22.80.39", ssl=True)

# authenticate with the server
conn.login(user , passwd)

# see what is in th primary mailbox for this account
conn.select_folder("INBOX", readonly=True)

message_ids = conn.search(['ALL'])

print("there are", len(message_ids), "messages in the INBOX")

# get each message seperately
messages = conn.fetch(message_ids, "BODY[]")

for k in messages:
    one_message = messages[k]

    # handle the fact that both the key and the value are given
    # to use a bytes() and not str()
    text = one_message[b"BODY[]"]
    # text = text.decode('utf-8')

    # print(text)

    # alternative to extract more data with pyzmail
    email = pyzmail.PyzMessage.factory(text)
    subj =  email.get_subject()
    from_addr = email.get_addresses("from")

    # todo: see what the email's charset is and only use utf-8 if we get a None back
    text_part = email.text_part.get_payload().decode('utf-8')

    # outputs for pyzmail
    print("Subject:", subj)
    print("From:", from_addr[0])
    print("")
    print(text_part)

    # simply a pause button
    input("Press ENTER to continue:")