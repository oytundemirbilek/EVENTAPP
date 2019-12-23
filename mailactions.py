
import imaplib, email, smtplib
import sqlite3
from email.header import decode_header
import os

def SendMail(user, password, subject, body, sendMailAddress):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, password)
        
        msg = f'Subject:{subject} \n\n {body}'
        smtp.sendmail(user, sendMailAddress, msg)
        return("Mail sended!")
def Login(user, password):
    con = imaplib.IMAP4_SSL("imap.gmail.com")
    con.login(user, password)
    con.select("INBOX")
    inboxList = []
    sentList = []
    result, data = con.search(None, "ALL")
    for num in data[0].split():
        result, data = con.fetch(num, '(RFC822)')
        if (result != 'OK'):
            return "error cannot fetch mail"

        raw = (data[0][1].decode("utf-8"))
        email_message = email.message_from_string(raw)
        inboxList.append(email_message)
        sender = GetSender(email_message)
        title = GetTitle(email_message)
        body = GetBody(email_message)
        Insert("inbox", sender, title, body)
        
    con.select('"[Gmail]/Sent Mail"')
    result, data = con.search(None, "ALL")
    for num in data[0].split():
        result, data = con.fetch(num, '(RFC822)')
        if (result != 'OK'):
            print=("Error cannot fetch mail",num)
            return

        raw = (data[0][1].decode("utf-8"))
        email_message = email.message_from_string(raw)
        sentList.append(email_message)
        title = GetTitle(email_message)
        body = GetBody(email_message)
        Insert("sendbox","",title,body)
   
    return "succesfull login"