from flask import Flask
from flask import request
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_email(to,sub,on):
    
    me = "christlloyd.lloyd2@gmail.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"{to} read your email."
    msg['From'] = me
    msg['To'] = me
    text=f"The email u sent to {to} subjected as {sub} has been read on {on}."
    part = MIMEText(text, 'plain')
    msg.attach(part)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('christlloyd.lloyd2@gmail.com','aabxruqcifzwtsrl')
    mail.sendmail(me, me, msg.as_string())
    mail.quit()
        
 
app = Flask(__name__)
 

@app.route('/', methods=['GET'])
def zero():
    to = request.args.get('to')
    sub = request.args.get('sub')
    on = datetime.now()
    send_email(to,sub,on)
    return '<img src=""  />'
 

if __name__ == '__main__':
 
    app.run()