from flask import Flask, render_template, redirect, request, url_for
# import mysql.connector

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/portfolio-details')
def portfolioDetails():
    return render_template('portfolio-details.html')

if __name__ == '__main__':
    app.run(debug=True)