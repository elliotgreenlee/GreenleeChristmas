import logging
from flask import render_template, request, redirect
from models import Gift

log = logging.getLogger('gunicorn.error')


def index():
    all_gifts = Gift.query.all()
    return render_template('index.html', gifts=all_gifts)
