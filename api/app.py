import logging
import os

from flask import Flask
from dotenv import load_dotenv

from models import db
from pages import index, christmas2020, christmas2021, christmas2023


app = Flask(__name__)

# Merge gunicorn and flask logging
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

# Load environment variables
load_dotenv()
environment_debug = bool(os.environ.get('DEBUG'))
environment_database_url = str(os.environ.get('DATABASE_URL'))
# Fix https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy
# -dialectspostgre Recommended solution from Heroku.
if environment_database_url and environment_database_url.startswith("postgres://"):
    environment_database_url = environment_database_url.replace("postgres://", "postgresql://", 1)
app.logger.info(environment_debug)
app.logger.info(environment_database_url)


# Flask app settings
debug = environment_debug
app.config['SQLALCHEMY_DATABASE_URI'] = environment_database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database settings
db.init_app(app)


# Urls
app.add_url_rule('/', 'index', view_func=index.index, methods=['GET'])
app.add_url_rule('/christmas2023', 'christmas2023', view_func=christmas2023.christmas2023, methods=['GET'])
app.add_url_rule('/christmas2021', 'christmas2021', view_func=christmas2021.christmas2021, methods=['GET'])
app.add_url_rule('/christmas2020', 'christmas2020', view_func=christmas2020.christmas2020, methods=['GET'])

if __name__ == "__main__":
    app.run(debug=debug)
