from flask import Flask
from flask import render_template
from flask import request
from website import Website
import re


app = Flask(__name__)

# avoid caching for development purposes
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['GEVENT_SUPPORT'] = True

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Set up initial websites:

Website('https://duckduckgo.com')
Website('https://www.google.com/pagedoesntexist')
Website('https://http.cat/')

#

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        Website(request.form['url'])
    Website.check_all()
    return render_template(
        "home.html",
        pages=Website.all,
        length=len(Website.all)
    )




