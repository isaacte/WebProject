# Pull base image
FROM python:3-alpine

#Create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app
#Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


#Install software
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
    
#Copy project
COPY . .

#Install requirements.txt
RUN pip install -r requirements.txt

#Create static and media repositories to be served via ngnix
RUN mkdir static
RUN mkdir media


#Copy entrypoint script
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

#Give app user the ownership of the files
RUN chown -R app:app $APP_HOME

#Change to app user
USER app

#Set entrypoint
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
