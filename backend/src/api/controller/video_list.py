from flask import Blueprint, request, jsonify
from backend.src.api.db import video_repository
import math
import random

video_info = Blueprint('video_list', __name__)


@video_info.route('/api/video-list')
def response_video_list():
    name = request.args.get('name')
    if not name:
        name = random_pick_up()
    sorted_video_list = video_repository.take_sorted_video_list(name)
    response = {
        'searchTag': name,
        'videoList': sorted_video_list
    }
    return jsonify(response)


def random_pick_up():
    filtered_tags = video_repository.take_filtered_sorted_tags()
    return filtered_tags[math.floor(random.uniform(0, len(filtered_tags)))]['_id']
