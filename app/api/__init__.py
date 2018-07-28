from flask import Blueprint

# This instance of a Blueprint that represents the api blueprint
api = Blueprint('api', __name__)

from . import views
