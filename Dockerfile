FROM python:3

WORKDIR /usr/src/

# Install python requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Java, PySpark requirements
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean;

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV PYSPARK_PYTHON=python3

# Copy app files
WORKDIR /usr/src/app/
COPY app/ ./

CMD [ "flask", "run", "--host=0.0.0.0"]