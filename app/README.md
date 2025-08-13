# docker image

## test the app (app dir)
cd app
python3 -m venv .
source ./bin/activate
pip install --no-cache-dir -r requirements.txt
python ./app.py

## build image (app dir)
docker build . -t app_with_db:001

## start container
docker run -p 8888:5000 -d --name app_with_db app_with_db:001
curl 0.0.0.0:8888

## start/inspect/stop/remove container (app_with_db)
docker start $(docker ps -aqf "name=app_with_db")
docker stop $(docker ps -aqf "name=app_with_db")
docker inspect $(docker ps -aqf "name=app_with_db") | jq ".[0].State.Status"
docker rm $(docker ps -aqf "name=app_with_db")
