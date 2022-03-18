FROM python:3.10-bullseye
EXPOSE 8000
RUN pip install --upgrade pip
WORKDIR ./
RUN apt-get install default-libmysqlclient-dev
COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . ./
ENTRYPOINT []
CMD python3 manage.py migrate && sh -c "exec python3 manage.py runserver 0.0.0.0:8000"