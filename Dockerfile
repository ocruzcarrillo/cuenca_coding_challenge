FROM python:3.7

WORKDIR /app

COPY requirements.txt ./

COPY . /app

USER root
RUN whoami \
	&& apt-get update \
	&& apt-get install -y postgresql postgresql-contrib 
RUN update-rc.d postgresql enable 

USER postgres
	 
RUN whoami \
	&& service postgresql restart \
	&& psql -a -f "./config/database_setup.sql" 

CMD ["python", "./main.py"]