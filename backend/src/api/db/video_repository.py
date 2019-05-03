from pymongo import MongoClient, DESCENDING
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


def take_filtered_sorted_tags():
    sorted_tags = take_sorted_tags()
    # 大量の動画に紐づくタグは有用ではないと考え、以下の通り絞り込みを行う。
    return [element for element in sorted_tags
            if 2 <= element['frequency'] < (sorted_tags[0]['frequency'] / 4)]


def take_sorted_video_list(tag):
    return list(video_info_collection.find({'tags': tag}, {'_id': 0}).sort('published_at', DESCENDING))


if __name__ == '__main__':
    print(take_sorted_video_list('山田玲司'))
