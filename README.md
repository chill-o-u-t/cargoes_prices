# cargoes_prices
- clone repository
```
git clone git@github.com:chill-o-u-t/cargoes_prices.git
cd cargo_prices/
```
- Edit .env
```
rename .env.template to .env
in .env
<user> to postgres user
<password> to postgres pass
<db_name> to database name
```
- Start with Docker
```
Edit in docker-compose
<user> to postgres user
<password> to postgres pass
<db_name> to database name
```
```
docker-compose up -d --build
```
- Create migrations
```
sudo docker-compose exec web aerich init -t app.core.confog.DATABASE_CONFIG
sudo docker-compose exec web aerich init-db
```
- info about enpoints at http://127.0.0.1:8000/docs
