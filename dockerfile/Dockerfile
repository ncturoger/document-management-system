FROM python:3.6.3

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Place requirements in docker image
ADD ./requirements.txt /usr/src/app/requirements.txt

# Install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set executable pythonpath for Flask app
ENV FLASK_APP /usr/src/app/app.py
