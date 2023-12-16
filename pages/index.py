import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def index():
    gifts2023 = Gift.query.filter_by(year='2023').all()
    return render_template('templates/index.html', gifts=gifts2023)
