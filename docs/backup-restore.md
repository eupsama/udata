# Backup


# Restore

## Mongodb

```shell
docker-compose exec db bash -c 'mongorestore --drop --db udata /data/db/dump-prod/udata/'
```
