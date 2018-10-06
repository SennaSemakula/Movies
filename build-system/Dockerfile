FROM ubuntu:latest
MAINTAINER Senna Semakula-Buuza "senna.semakula@outlook.com"

#Update the image to retrieve the latest packages
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python-pip
RUN apt-get install -y python3-pip

COPY app/requirements.txt app/graph.py app/plot.py /app/movies.py app/app.py /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN pip install imdbpy 
RUN pip install bokeh 

ENTRYPOINT ["python"]
CMD ["app.py"]

