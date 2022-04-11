FROM python:3

WORKDIR /LoaderoProject

ADD main.py ./

ADD requirements.txt ./

RUN pip install -r requirements.txt

COPY ./loadero ./loadero

ENTRYPOINT [ "python", "./main.py" ]
