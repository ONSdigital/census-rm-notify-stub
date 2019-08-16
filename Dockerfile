FROM python:3.6-slim

WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip3 install pipenv && pipenv install --deploy --system

ENTRYPOINT ["python3"]
CMD ["app.py"]