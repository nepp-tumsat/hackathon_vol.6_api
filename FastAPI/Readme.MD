#cd コマンドでFastAPIに移動し、以下の順番でコードを実行する

$docker-compose build

$ docker-compose run --entrypoint "poetry install --no-root" demo-app

$ docker-compose build --no-cache

$docker-compose up


#dockerが立ち上がっている状態で以下のコードを実行する(ユニットテストの際に使用、-Dは開発者モードの時のみ実行される。デプロイ時には関係しない)
$docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx