from flask import Flask , render_template,request , redirect , url_for
import os
import smtplib

app = Flask(__name__)

@app.route('/<to>')
def index(to):
    try:
        
        email = os.environ['EMAIL_ADDRESS']
        password = os.environ['PASSWORD']
        emailto = to
        server = smtplib.SMTP('smpt.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email , password)
        message = 'Subject: {}\n\n{}'.format(subject , msg)
        server.sendmail(email , to,message)
        server.quit()
        return 'Succefully Sent Email From {} To {}'.format(email,to)
        
    except Exception as e:
        return e
   
if __name__ == "__main__":
    app.run()
