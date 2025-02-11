FROM python:3.9.20-slim-bullseye

RUN apt-get update && \
    apt-get -y install python3-pip \
    socat

RUN useradd ctf
WORKDIR /home/ctf

COPY app.py      /home/ctf/
COPY key.txt    /home/ctf/
COPY requirements.txt /home/ctf/

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf
RUN pip3 install -r /home/ctf/requirements.txt

EXPOSE 9090
ENTRYPOINT ["socat", "TCP-LISTEN:9090,reuseaddr,fork,nodelay,su=ctf", "EXEC:'python3 app.py'"]