from pymongo import MongoClient
from backend import config

client = MongoClient(config.DB_HOST, config.MONGO_PORT)
db = client.yansan_db
video_info_collection = db.video_info
tags_collection = db.tags


def take_sorted_tags():
    pipe = [
        {'$unwind': '$video_id'},
        {'$group': {'_id': '$tag', 'frequency': {'$sum': 1}}},
        {'$sort': {'frequency': -1}}
    ]
    return list(tags_collection.aggregate(pipeline=pipe))


if __name__ == '__main__':
    result = take_sorted_tags()
    print(list(result))
