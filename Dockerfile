FROM python:3.11-slim
WORKDIR /docker-meteo
RUN pip install requests python-dotenv
COPY meteo.py .
COPY .env .
CMD ["python", "meteo.py"]