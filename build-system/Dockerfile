FROM ubuntu:latest
MAINTAINER Senna Semakula-Buuza "senna.semakula@outlook.com"

#Update the image to retrieve the latest packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python-pip
COPY app/requirements.txt app/app.py /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN pip install imdbpy
RUN pip3 install bokeh
ENTRYPOINT ["python"]
CMD ["app.py"]

