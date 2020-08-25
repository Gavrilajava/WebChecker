from flask import Flask
from flask import render_template
from website import Website
import logging
import re
import sys

app = Flask(__name__)

# avoid caching for development purposes
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

w = Website('https://duckduckgo.com')
w = Website('https://www.google.com/pagedoesntexist')
w = Website('https://http.cat/')

@app.route("/")
def home():
    app.logger.info("checking")
    Website.check_all()
    return render_template(
        "home.html",
        pages=Website.all,
        length=len(Website.all)
    )

