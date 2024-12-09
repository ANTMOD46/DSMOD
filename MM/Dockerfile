FROM python:3.11-slim

WORKDIR / MM

COPY . .

RUN pip install django

RUN python manage.py migrate

EXPOSE 9999

CMD ["python","manage.py","runserver","0.0.0.0:9999"]



FROM python:3.11-slim

WORKDIR /MM

COPY . .

RUN pip install django

RUN python manage.py migrate

EXPOSE 9999

CMD ["python","manage.py","runserver","0.0.0.0:9999"]


docker build -t tanoii:1.0 .
docker run --name tanoii -p 9999:9999 tanoii:1.0 






FROM python:3.11-slim

WORKDIR / MM

COPY . .

RUN pip install django

RUN python manage.py migrate

EXPOSE 9999

CMD ["python","manage.py","runserver","0.0.0.0:9999"]



FROM python:3.11-slim 

WORKDIR /MM

COPY . .

RUN pip install django 

RUN python manage.py migrate

EXPOSE 9999

CMD ["python","manage.py","runserver","0.0.0.0:9999"]

docker build -t modtanoii:1.0 .
docker run --name modtanoii -p 9999:9999 modtanoii:1.0 























#เวลารัน 
docker build -t tanoii:1.0 .   
docker run --name tanoii -p 9999:9999 tanoii:1.0   

docker build -t tanoii:1.0 .
docker build -t tanoii:1.0 .
docker build -t tanoii:1.0 .

docker run --name tanoii -p 9999:9999 tanoii:1.0
docker rub --name tanoii -p 9999:9999 tanoii:1.0
docker run --name tanoii -p 9999:9999 tanoii:1.0