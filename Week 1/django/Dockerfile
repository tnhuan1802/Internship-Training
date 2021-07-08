FROM python:3.8.3-slim-buster 
# Make python outputs go straight to the terminal
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy the requirements file to the new working directory
COPY requirements.txt requirements.txt
# Install all the requirements/dependencies
RUN pip3 install -r requirements.txt
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# Copy everything
COPY . .