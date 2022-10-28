FROM python:3.11-slim
WORKDIR /app
RUN  apt-get update && apt-get install -y libpq-dev build-essential libpcre3 libpcre3-dev
COPY requirements.txt ./
RUN python3 -m pip install --no-cache -r requirements.txt

COPY wsgi.py ./
COPY app ./app

CMD ["uwsgi", \ 
     "--http", ":80", \
     "--wsgi-file", "wsgi.py", \
     "--callable", "wsgi_app", \
     "--master", "--processes", "2", \
     "--threads", "1"]

