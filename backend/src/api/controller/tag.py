from flask import Blueprint, jsonify
from backend.src.api.db import video_repository

tag = Blueprint('tag', __name__)


@tag.route('/api/tags')
def take_tags():
    sorted_tags = video_repository.take_sorted_tags()
    # 大量の動画に紐づくタグは有用ではないと考え、以下の通り絞り込みを行う。
    filtered_tags = [element for element in sorted_tags
                     if 2 <= element['frequency'] < (sorted_tags[0]['frequency'] / 4)]
    response = {
        "tags": filtered_tags
    }
    return jsonify(response)
