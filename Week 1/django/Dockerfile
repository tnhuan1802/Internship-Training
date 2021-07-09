FROM python:3.8.3-slim-buster 
# Make python outputs go straight to the terminal
ENV PYTHONUNBUFFERED 1
WORKDIR /django

# Copy the requirements file to the new working directory
COPY requirements.txt requirements.txt
# Install all the requirements/dependencies
RUN pip3 install -r requirements.txt

# ADD docker-entrypoint.sh /docker-entrypoint.sh
# RUN chmod a+x /docker-entrypoint.sh
# ENTRYPOINT ["/docker-entrypoint.sh"]
# Copy everything
COPY . .