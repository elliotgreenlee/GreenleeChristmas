import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def index():
    gifts2024 = Gift.query.filter_by(year='2024').all()
    return render_template('index.html', gifts=gifts2024)
