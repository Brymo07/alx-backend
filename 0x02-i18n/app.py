#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from datetime import datetime
import locale


class Config(object):
	"""_summary_

	Returns:
					_type_: _description_
	"""
	LANGUAGES = ['en', 'fr']
	BABEL_DEFAULT_LOCALE = 'en'
	BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
	1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
	2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
	3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
	4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
	"""returns a user dictionary or None if the ID cannot be found
	"""
	login_id = request.args.get('login_as')

