FROM python:3.9-buster

# Updating system and installing libraries
RUN apt-get update && apt-get install -y gettext

# Set work directory
WORKDIR /usr/src/app

# Installing required plugins
ADD ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Create source directory
COPY . .

# Define entrypoint
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
