# TODO-app

## Setup project

### Clone from the GitLab

```sh
git clone git@github.com:MilanTagline2021/TODO-app.git
cd TODO-app/
```

### Build the docker containers

```sh
docker-compose up -d --build
```

### Migrate the databases

```sh
docker-compose exec backend alembic upgrade head
```

You can see the all the modules running on the specified ports.

- [backend](http://0.0.0.0:3000/docs/)


### Create an autogenerate migration in the modules

```sh
docker-compose exec backend alembic revision --autogenerate -m [commit message]
```

### Check the status of all the containers

```sh
docker-compose ps -a
```

### Execute the command in the particular container

```sh
docker-compose exec [service] [command]
```

- `service`, service name mentioned in the docker-compose file
- `command`, any command to run in the container

### Stop the containers

```sh
docker-compose stop
```

### Remove the containers

```sh
docker-compose down
```