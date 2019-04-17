from flask import Blueprint, jsonify
from random import *

random = Blueprint('random', __name__)


@random.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)
