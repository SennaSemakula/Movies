FROM ubuntu:latest
MAINTAINER Senna Semakula-Buuza "senna.semakula@gmail.com"

#Update the image to retrieve the latest packages
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python-pip
RUN apt-get install -y python3-pip

COPY app/ /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN pip install imdbpy 
RUN pip install bokeh 
RUN pip install plotly 


ENTRYPOINT ["python"]
CMD ["app.py"]

