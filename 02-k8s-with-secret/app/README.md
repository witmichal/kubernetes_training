# without docker-compose
## 1. start DB
```sh
docker run -p 5432:5432 --name postgres-db-17-5 -e POSTGRES_PASSWORD=mypassword postgres:17.5
```

## 2. test the app (app dir)

```sh
cd app
python3 -m venv .
source ./bin/activate
pip install --no-cache-dir -r requirements.txt
source export_vars.sh
python ./app.py
curl 0.0.0.0:5000
```

## 3. build image (app dir)

```sh
docker build . -t app_with_db:002
```

## 4. start container

```sh
docker run -p 8888:5000 -d --name app_with_db app_with_db:002
curl 0.0.0.0:8888
```

## 5. start/inspect/stop/remove container (app_with_db)

```sh
docker start $(docker ps -aqf "name=app_with_db")
docker stop $(docker ps -aqf "name=app_with_db")
docker inspect $(docker ps -aqf "name=app_with_db") | jq ".[0].State.Status"
docker rm $(docker ps -aqf "name=app_with_db")
```

# with docker-compose

```sh
docker-compose build
docker-compose up
docker-compose stop
docker-compose rm
```

## test
```shell
curl 127.0.0.1:8111
```