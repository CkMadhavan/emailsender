from flask import Flask , render_template,request , redirect , url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return (os.environ['EMAIL_ADDRESS'])
   
if __name__ == "__main__":
    app.run()
