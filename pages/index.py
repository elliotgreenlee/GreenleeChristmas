import logging
from flask import request, redirect, url_for, session, render_template
from app import db
from models import Gift

log = logging.getLogger('gunicorn.error')


def index():
    all_gifts = Gift.query.all()
    return render_template('index.html', gifts=all_gifts)
