# This is the module for Google Login. It is made using flask
# Flask can be understood easily but we need to think about the echo and secho
# The templates folder is a must. It cannot be deleted
# This prints out the Email and Password. BUt code can be modifed to change it

from flask import Flask, redirect, url_for, session, jsonify, render_template
from authlib.integrations.flask_client import OAuth
import webbrowser
import sys, os, signal
import logging
import click
from encrypt import savecred
import mysql.connector as mysql

somedict = {}
#The below code until the next comment is for hiding the output
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

#Defining the flask app
f_app = Flask(__name__)

# MySQL Connection
db = mysql.connect(host='libmgmt.heliohost.us', user='libmgmt', password='nevermindmf', database='libmgmt_bookstore')
cur = db.cursor()


def theoauth(flaskapp = Flask(__name__)):
    flaskapp.secret_key = "something"
    #Oauth Config.
    #Client ID and Client Secret are the main parts which was retreived from cloud.google.com
    oauth = OAuth(flaskapp)
    google = oauth.register(
        name='google',
        client_id='851573419140-jd37dtllvspbtgah49nslai01730oauv.apps.googleusercontent.com',
        client_secret='uhOCpxQZr3v8pvrSGh6abHFg',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
        client_kwargs={'scope': 'openid email profile'},
    )


    #The main screen (however, this page wont appear at all)
    #URL of this page will be "http://127.0.0.1:5000/"
    @flaskapp.route("/")
    def hlo():
        return 'Please go to http://127.0.0.1:5000/login'


    #Login Route
    #URL of this page is "http://127.0.0.1:5000/login"
    @flaskapp.route('/login')
    def login():
        google = oauth.create_client('google')
        redirect_uri = url_for('authorize', _external=True)
        return google.authorize_redirect(redirect_uri) # This statement redirects our app to google's login page

    #Authorisation Route
    #URL of this page is "http://127.0.0.1:5000/authorize"
    @flaskapp.route('/authorize')
    def authorize():
        global user_info
        google = oauth.create_client('google')
        token = google.authorize_access_token()
        resp = google.get('userinfo')
        resp.raise_for_status()
        user_info = resp.json()

        # Opening Application's website
        webbrowser.open('https://bstore21.heliohost.us/loginsucess.html')


        # Killing Flask
        os.kill(os.getpid(), signal.SIGINT)

        return 'OK'


    webbrowser.open('http://127.0.0.1:5000/login')
    flaskapp.run()


