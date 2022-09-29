## セットアップ

### Docker イメージの作成

docker-compose.yml があるディレクトリで下記コマンドを実行します。
すると、Docker Image が作成されます。
ソースを変更したときはビルドしてください。

```bash
docker-compose build
```

依存パッケージをインストールします

```bash
docker-compose run --entrypoint "poetry init" judge-cool-value-bot
```

```bash
docker-compose run --entrypoint "poetry install" judge-cool-value-bot
```

```bash
docker-compose run --entrypoint "poetry add discord.py" judge-cool-value-bot
```

新しい Python パッケージを追加した場合は下記コマンドで再ビルドをします

```bash
docker-compose build --no-cache
```

### 実行

```bash
docker-compose run --entrypoint "poetry run python3 api/main.py" judge-cool-value-bot
```
