from flask import Blueprint, jsonify
from backend.src.api.db import video_repository

tag = Blueprint('tag', __name__)


@tag.route('/api/tags')
def response_tags():
    response = {
        "tags": video_repository.take_filtered_sorted_tags()
    }
    return jsonify(response)
