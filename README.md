# short-url

Django web-application to generate short urls which redirect to provided url

## Installation
This application requires python 3.6 and above.
All commands run from the project root

To install run following command
````bash
make install
````
See Makefile to get more details

## Run
Activate virtual environment
```bash
. venv/bin/activate
```

Run Django web-service
```bash
python manage.py runserver 0.0.0.0:8000
```

## Testing
```bash
make test
```

#### FYI
This is a test application that is why I am fine with storing SECRET_KEY inside git 
repository

I tried to keep the application as simple as possible, also due to lack of time 
I decided to use sqlite instead of postgreesql to reduce the complexity of the 
installation
There is no any async workers. But it is MUST HAVE for such kind of applications. 
(See TODO's)


## TODO's

#### Project
* Expiration time for urls.
  - default, specified by user and infinity
* Cache most popular links 
  - 20-30% of total links number
  - LRU eviction policy
* Use background task to update url's stats
* Background task to generate short-codes upfront and store them in cache
* Authoriztion and url creation per user

#### Infrastructure
* Test coverage, linters, isort
* Create API documentation (DRF Built-in API documentation,DRF Self describing APIs,
  Swagger, etc )
* Split requirements.txt to requirements-base.txt and requirements-dev.txt
* Code quality checks (SonarQube)
* Analytics and Monitoring. ELK or Clickhouse, Grafana, Sentry
* Cache. Redis or similar cloud solution
* Use non-relational DB to store urls. MongoDB or cloud solution
* Setup background tasks, (Celery, Django-Q, Dramatiq, etc.)
* Data sharding (if needed)
