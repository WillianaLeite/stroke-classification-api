FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]