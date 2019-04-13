#
# Dockerfile to run python application 
#
FROM python:3-alpine

# set node workdir
WORKDIR /opt/python

# Metadata
LABEL   Author="Alcindo Schleder<alcindoschleder@gmail.com>" \
        maintainer="Alcindo Schleder<alcindoschleder@gmail.com>" \
        version="1.0" \
        description="This is a simple VUTTR front end Application that consume vuttr API service."

# copy app directory to /opt/python container directory 
ADD vuttr /opt/python

# Install all dependencies for the app
#RUN pip install py-mysql \
#    && pip install py-mongo

VOLUME /opt/python

# Run application
CMD [ "python", "/opt/python/vuttr/vuttr.py" ]
