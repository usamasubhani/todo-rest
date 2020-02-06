From python:alpine3.7 
COPY ./ ./todo-microservice
WORKDIR /todo-microservice
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV development
ENV FLASK_APP api
CMD flask run --host=0.0.0.0