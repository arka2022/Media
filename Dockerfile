FROM python:3.10
LABEL maintainer="Parthasaradhi Terugu"
RUN mkdir /app
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install sudo
RUN apt-get install ffmpeg -y
EXPOSE 5003
ENTRYPOINT ["python"]
CMD ["main.py"]
