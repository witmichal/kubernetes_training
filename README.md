# stop / remove all containers with filtered name

```shell
# start
docker ps -a -f name="app-postgres|app-svc" | awk 'NR>1 {print $1}' | xargs docker up

# stop
docker ps -a -f name="app-postgres|app-svc" | awk 'NR>1 {print $1}' | xargs docker stop

# remove
docker ps -a -f name="app-postgres|app-svc" | awk 'NR>1 {print $1}' | xargs docker rm
```

```shell
docker ps -a -f name="app-postgres|app-svc"
```
