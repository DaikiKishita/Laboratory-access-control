# LAC
this is lab's application

### 環境ファイルの準備
/server/backendの直下にenvsフォルダを作成
envs直下に.envファイルを追加して下記の通りに作成する

### 環境ファイル
```envs
host="write your host IP"
user="root"
dbname="LAC"
password="root"

webhook_url(discord)
```
現在ではenvファイルからの読み込みが出来ないため、setting.pyファイルに直接書き込んでいる

自身のホストIPを環境ファイルに入力

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

その後...
```bash
cd frontend
curl -sL https://deb.nodesource.com/setup_14.x | bash -
apt-get install -y nodejs
apt-get install -y npm
npm install -g @vue/cli
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
npm install --force
npm run build
```
※buildには時間がかかります

### errorの確認
```bash
docker-compose logs
```