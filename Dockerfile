FROM python:3

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/
COPY app/ ./

CMD [ "flask", "run", "--host=0.0.0.0"]