import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def index():
    gifts2021 = Gift.query.filter_by(year='2021').all()
    return render_template('index.html', gifts=gifts2021)
