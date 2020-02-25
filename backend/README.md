# yansan-web/frontend
ヤンサンWebにおける、バックエンドのコードを含んだフォルダです。

## 仕様詳細
### API
#### タグ一覧取得
一定数の動画が紐付いているタグの一覧を取得するAPIです。  
URIは以下の通りです。
```
http://<HOSTNAME>/api/tags
```
以下形式のレスポンスが返却されます。
``` json
{
  "tags": [
    {
      "name": "山田玲司",
      "frequency": 5
    },
    {
      "name": "漫画",
      "frequency": 14
    }
  ]
}

```

#### タグ関連動画取得
指定されたタグに関連する動画の一覧を取得するAPIです。  
タグの指定が省略された場合、サーバ側でランダムにタグを選択し、関連する動画の一覧を返却します。  
URIは以下の通りです。
```
http://<ENDPOINT>/api/video-list?name=<tag value>
```
以下形式のレスポンスが返却されます。
``` json
{
  "searchTag": "漫画",
  "videoList": [
    {
      "id": "R0VMEAzykOE",
      "publishedAt": "2019-04-17T09:58:17.000Z",
      "title": "タイトル01",
      "tags": ["漫画", "山田玲司"]
    },
    {
      "id": "RLTUPbOuFWQ",
      "publishedAt": "2019-04-19T09:58:17.000Z",
      "title": "タイトル02",
      "tags": ["漫画", "山田玲司"]
    }
  ]
}
```
