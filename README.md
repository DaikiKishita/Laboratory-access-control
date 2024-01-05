# LAC
this is lab's application

### 環境ファイルの準備
/server/backendの直下にenvsフォルダを作成
envs直下に.envファイルを追加して下記の通りに作成する

### 環境ファイル
```envs
host="write your mysql container IP"
user="LACkun"
dbname="LAC"
password="LACpass"

webhook_url(discord)
```
現在ではenvファイルからの読み込みが出来ないため、setting.pyファイルに直接書き込んでいる

### 起動
```bash
docker-compose build
docker-compose up -d
```

### mysqlのIP確認方法
```bash
docker exec -it LAC-mysql bash
```

上記のコマンドを入力した後下記を実行
```bash
cat /etc/hosts/
```

出て来たIPを環境ファイルに入力

### 再度起動
```bash
docker-compose up -d
```