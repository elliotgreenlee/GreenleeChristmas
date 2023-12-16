import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def christmas2021():
    gifts2021 = Gift.query.filter_by(year='2021').all()
    return render_template('christmas2021.html', gifts=gifts2021)
