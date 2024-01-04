# LAC
lab's application

### 環境ファイル
```env
TOKEN(discordbot)
channelid(discord)

host(mysql)
user(LACkun)
dbname(LAC)
password(LACpass)

webhook_url(discord)
```
現在ではenvファイルからの読み込みが出来ないため、setting.pyファイルに直接書き込んでいる


### 起動
```bash
docker-compose build
docker-compose up -d
```

