#comment

FROM python:3.7.2-slim 

COPY ./api /api   
WORKDIR /api 

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt 
RUN export FLASK_APP=app.py 
RUN export FLASK_ENV=development
RUN flask run