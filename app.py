from flask import Flask, render_template, request
import yagmail
import requests
from dotenv import load_dotenv
import os
load_dotenv(override=True)


app = Flask(__name__,template_folder='templates')

RECAPTCHA_VERIFICATION_URL = os.getenv("RECAPTCHA_VERIFICATION_URL")
RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY")
GMAIL_ID_SENDER = os.getenv("GMAIL_ID_SENDER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
GMAIL_ID_RECIEVER = os.getenv("GMAIL_ID_RECIEVER")

@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/portfolio-details')
def portfolioDetails():
    return render_template('portfolio-details.html')

@app.route('/api/contact',methods=["POST"])
def contact():
    # Get the data from the request
    recaptcha = request.form.get('g-recaptcha-response')
    if recaptcha:
        # Check if the recaptcha is valid
        response = requests.post(RECAPTCHA_VERIFICATION_URL, data={
            'secret': RECAPTCHA_SECRET_KEY,
            'response': recaptcha
        })
        response = response.json()
        if response['success']:
            # Send the email
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')
            # Send the email
            content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
            subject_mail = "Message from aakarsh.is-a.dev"
            yag = yagmail.SMTP(GMAIL_ID_SENDER,GMAIL_APP_PASSWORD)
            yag.send(GMAIL_ID_RECIEVER, subject_mail, content)
            return "OK",200
        return "Invalid Recaptcha",400  
    return "Recaptcha is required",400

if __name__ == '__main__':
    app.run(debug=True)