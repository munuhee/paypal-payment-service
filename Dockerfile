FROM python:3.12-alpine
WORKDIR /paypal-payment-service
COPY . /paypal-payment-service
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "run.py"]