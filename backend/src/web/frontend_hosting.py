from flask import Blueprint, render_template

frontend_hosting = Blueprint('frontend_hosting', __name__)


@frontend_hosting.route('/', defaults={'path': ''})
@frontend_hosting.route('/<path:path>')
def render(path):
    return render_template('index.html')
