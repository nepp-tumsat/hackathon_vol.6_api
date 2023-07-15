##データベースの確認方法

#以下のコマンドをターミナルで順番に打つ

$ docker-compose exec db mysql demo

mysql> SHOW TABLES; (テーブルの確認)

mysql> DESCRIBE tasks;  (taskテーブルの中身を確認)

mysql> DESCRIBE dones;  (doneテーブルの中身を確認)