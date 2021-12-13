import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def christmas2020():
    gifts2020 = Gift.query.filter_by(year='2020').all()
    return render_template('christmas2020.html', gifts=gifts2020)
