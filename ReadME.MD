# hackathon_vol.6_api

## こだわりポイント



## 開発期間

2,3日

## 使用技術
- HTML/CSS
- JavaScript
- React
- FastAPI
- GPT-3.5

## チーム開発で利用したツール
- Slack
- Discord
- git
- Github
- Figma

## 開発環境

dockerで一括管理



## 起動方法
hackathon_vol.6_api/api/routers/apikey.pyを作成し
```
key="{openaiのAPIKEY}"
```
を記述

hackathon_vol.6_api直下に移動し、ターミナルで以下の順番でスクリプトを実行する
```
$docker-compose build

$ docker-compose run --entrypoint "poetry install --no-root" demo-app

$ docker-compose build --no-cache
```
↓コンテナが動いた状態で
```
$ docker-compose exec demo-app poetry run python -m api.migrate_db

$docker-compose up
```

## データベースの確認方法

## 以下のコマンドをターミナルで順番に打つ
```
$ docker-compose exec db mysql demo

mysql> SHOW TABLES; (テーブルの確認)

mysql> DESCRIBE tasks;  (taskテーブルの中身を確認)

mysql> DESCRIBE dones;  (doneテーブルの中身を確認)
```
## dockerが立ち上がっている状態で以下のコードを実行する(ユニットテストの際に使用、-Dは開発者モードの時のみ実行される。デプロイ時には関係しない)
```
$docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx
```
