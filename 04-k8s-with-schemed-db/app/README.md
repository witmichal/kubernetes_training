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
curl 127.0.0.1:8111/counter
curl -X POST 127.0.0.1:8111/counter/increase
curl -X POST 127.0.0.1:8111/counter/reset
```
