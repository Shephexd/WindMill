FROM apache/airflow:2.1.1

# set args

# set envs
ENV PORT=8080

WORKDIR /app

USER root
RUN apt-get update \
    && apt install git -y

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r ./requirements.txt

COPY . /app
CMD ["airflow", "webserver"]
