# それぞれの使い方

## ・バックエンド
1. バックエンドのディレクトリに移動
```
$ cd back
```
2. 仮想環境の作成、アクティベート、パッケージインストール
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

3. 開発サーバーの起動
```
$ uvicorn main:app
```

## フロントエンド
1. フロントエンドのディレクトリに移動
```
$ cd front
```

2. 開発サーバーの起動
```
$ yarn serve
```
