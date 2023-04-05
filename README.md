
# Web Project - ReadMore

## Use in local (docker-compose)
In order to run the application in docker compose you must follow these steps:

1. Clone this repository: `git clone https://github.com/isaacte/WebProject`
2. Set `POSTGRES_USER` (User of the Postgres DB), `POSTGRES_PASSWORD` (Password for the user) and `POSTGRES_DB` (Name of the dabase) on docker-compose.yaml. *This step is not required (but strongly recommended) as there are some default values declared.
3. Create a `.env` file in the root path of the folder containing the following information:
```
DEBUG=<0|1>
SECRET_KEY=<secret_key>
DJANGO_ALLOWED_HOSTS=<127.0.0.1, localhost, ...>
DATABASE_URL=<postgres://dbuser:dbpassword@dbhost:dbport/dbname>
```
The variables can be changed to configure the application as desired.

4. Execute the docker compose application (this will build the images if does not exist): `docker compose up`

5. If you want to rebuild the images you can use the following command: `docker compose up --build`

If you want to run some commands you can attach to the docker `web` container or run it via docker compose exec as following: `docker compose exec web <command>`

## Deploy to fly.io
In order to deploy the application in [fly.io](https://fly.io) you must be registered and have the [Fly CLI](https://fly.io/docs/flyctl/) installed with the account logged in.

1. Clone this repository: `git clone https://github.com/isaacte/WebProject`
2. Create a `.env` file in the root path of the folder containing the following information:
```
DEBUG=<0|1>
DJANGO_ALLOWED_HOSTS=<domain.fly.dev>
```
The variables can be changed to configure the application as desired.\
*Fly.io will automatically deploy a Postgres DB and add the DATABASE_URL in the enviroment variable.

3. Run `fly launch --copy-config --dockerfile Dockerfile --ignorefile .dockerignore`.
4. Follow the steps of the wizard that will ask you for the app name, a region to deploy, if you want to setup a Postgresql database now (Say yes), an Upstash Redis database now (Say no) and if you want to deploy now (Say yes).
5. After the setup finishes anotate the `DATABASE_URL` and `SECRET_KEY` for further usages`
6. After deploying you can deploy the application via `fly deploy`.
7. After deploying you can open the application via `fly open`.
8. After opening the application you should apply database migrations and collect statics. Run: `fly ssh console -C "python code/manage.py migrate"`  to apply the migrations into the database and `fly ssh console -C "python code/manage.py collectstatic"` to collect the static files.
