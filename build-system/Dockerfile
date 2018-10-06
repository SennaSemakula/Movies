FROM ubuntu:latest
MAINTAINER Senna Semakula-Buuza "sennasemakula@hotmail.co.uk"

#Update the image to retrieve the latest packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python-pip
COPY requirements.txt app.py /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

