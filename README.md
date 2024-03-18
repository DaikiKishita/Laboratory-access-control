# LAC
this is lab's application

### 環境ファイルの準備
enviromentsフォルダの直下に.envファイルを追加して下記の通りに作成する

### 環境ファイル
自身のホストIPを環境ファイルに入力
```envs
host="write your host IP"
user="root"
dbname="LAC"
password="root"

webhook_url(discord)
```


### 起動
```bash
docker-compose build
docker-compose up -d mysql
docker-compose up -d app
```

### nodeモジュールを入れる
まずはLACのコンテナに入る
```bash
docker exec -it LAC bash
```

その後は下記のコマンドを一つずつ実行してください
```bash
bash build.sh
```
※ビルドには時間がかかります

### 動いてないときの確認
```bash
docker-compose logs コンテナ名
```