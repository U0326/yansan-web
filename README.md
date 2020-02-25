# yansan-web
[ヤンサンNavi](http://yansan-navi.garaku.work)のWebサイトを構成するプロジェクトです。プロジェクトの全容は[こちら](https://github.com/U0326/yansan-integration)をご覧ください。

ヤンサンNaviは、漫画家である山田玲司先生の番組「[山田玲司のヤングサンデー](https://www.youtube.com/channel/UC09D3M_DdLaZMJnZp0v4pLQ)」の動画を整理し、ヤンサンライフを支援することを目的としています。

## 要求事項
以下を事前にインストールしておく必要があります。
* Docker Engine: 1.13.0以上
* Python: 3.8以上
* npm: 3.0.0以上

## ローカルでの実行方法
```
git clone https://github.com/U0326/yansan-web.git
cd yansan-web

python -m venv venv
. venv/bin/activate
pip install -r ./backend/requirements.txt

npm --prefix frontend/ install
npm --prefix frontend/ run build_dev

// 別ウィンドウを開き、以下を実行する。
docker run --rm -p 27017:27017 --name test-mongo mongo
// 上記の起動完了後に、元のウィンドウで以下を実行する。
docker run --rm --link test-mongo -v `pwd`/test/db_dump:/backup mongo bash -c 'mongorestore --db yansan_db --host test-mongo /backup/yansan_db'

python bootstrap.py --development
```

## プロジェクト概要
- frontend: Vueを利用した、Web画面に関連するソースが含まれています。(合わせて[こちら](./frontend/README.md)もご覧ください。)
- backend: Pythonを利用した、WebAPIに関連するソースが含まれています。(合わせて[こちら](./backend/README.md)もご覧ください。)
