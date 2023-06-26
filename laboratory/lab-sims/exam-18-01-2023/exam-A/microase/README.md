docker compose build

docker compose up -d

locust -f locustfile.py

locust:
    number of users (peak concurrency): 100
    spawn rate: 10
    Host: http://127.0.0.1:5000/

no problem until 300-400 users (around 20 RPS)

then scale up
docker-compose up -d --scale string-service=6 --no-recreate

then it will scale better (around 40 RPS)