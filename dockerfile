#comment

FROM python:3.7.2-stretch

COPY ./api /api   
WORKDIR /api 

RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install default-jdk -y

RUN pip install -r ./requirements.txt 
ENV FLASK_APP=app.py 
ENV FLASK_ENV=development
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]