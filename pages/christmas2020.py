import logging
from flask import render_template
from models import Gift

log = logging.getLogger('gunicorn.error')


def christmas2020():
    all_gifts = Gift.query.all()
    return render_template('christmas2020.html', gifts=all_gifts)
