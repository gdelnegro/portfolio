#!/usr/bin/env bash

NAME="portfolio"                                  # Name of the application
PROJECT_DIR=/opt/portfolio
BASE_DIR=${PROJECT_DIR}"/src"
SOCKFILE=${PROJECT_DIR}"/portfolio.sock"  # we will communicate using this unix socket
USER=gdelnegro                                        # the user to run as
GROUP=webapps                                    # the group to run as
NUM_WORKERS=2                                    # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=base.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=base.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $PROJECT_DIR
source ./virtualenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$BASE_DIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $PROJECT_DIR/virtualenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
#  --bind 0.0.0.0:8000 \

## Start Gunicorn processes
#echo Starting Gunicorn.
#exec gunicorn helloworld.wsgi:application \
#    --bind 0.0.0.0:8000 \
#    --workers 3