FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential locales
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE pt_BR:pt:en  
ENV LC_ALL en_US.UTF-8 
COPY . /app
WORKDIR /app
VOLUME /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]

#docker build -t flask-app:latest .
#docker run -p 5000:5000 -v /Users/rodrigodmpa/Documents/IA/web:/app flask-app
#docker exec -i -t name-container bash