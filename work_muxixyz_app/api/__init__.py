from flask import Blueprint

api=Blueprint("api",__name__)

from . import management, project, file, share, status, message
