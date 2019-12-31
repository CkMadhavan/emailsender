from flask import Flask , render_template,request , redirect , url_for
import os
import smtplib

app = Flask(__name__)

@app.route('/<vars>')
def index(vars):
    try:
        
        email = os.environ['EMAIL_ADDRESS']
        password = os.environ['PASSWORD']
        to = vars.split('|-|-|-|-|-|')[0]
        subject = vars.split('|-|-|-|-|-|')[1]
        msg = vars.split('|-|-|-|-|-|')[2]
        
        subject = subject.replace('nextline' , '\n')
        subject = subject.replace('_' , ' ')
        msg = msg.replace('nextline' , '\n')
        msg = msg.replace('_' , ' ')
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email , password)
        message = 'Subject: {}\n\n{}'.format(subject , msg)
        server.sendmail(email , to,message)
        server.quit()
        
        return 'Succefully Sent Email From {} To {}'.format(email,to)
        
    except Exception as e:
        return str(e)
   
if __name__ == "__main__":
    app.run()
