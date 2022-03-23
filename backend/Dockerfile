FROM python:3.10-bullseye
EXPOSE 8000
RUN pip install --upgrade pip
WORKDIR ./
RUN apt-get update
RUN apt-get install default-libmysqlclient-dev
RUN apt-get install iputils-ping -y
COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . ./
ENTRYPOINT []
CMD python3 manage.py migrate && sh -c "exec python3 manage.py runserver 0.0.0.0:8000"