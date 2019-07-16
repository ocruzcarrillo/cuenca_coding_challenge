FROM python:3.7

WORKDIR /app

COPY requirements.txt ./

COPY . /app

RUN apt-get update \
	&& apt-get install -y postgresql postgresql-contrib \
	&& update-rc.d postgresql enable \
	&& service postgresql restart \
	&& su - postgres \
	&& psql -a -f "./config/database_setup.sql" \
	&& pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]