#!/bin/bash

NAME="portfolio"                                  # Name of the application
BASEDIR=/opt/portfolio
DJANGODIR="$BASEDIR/src"             # Django project directory
SOCKFILE="$DJANGODIR/portfolio.sock"  # we will communicte using this unix socket
USER=gdelnegro                                        # the user to run as
GROUP=webapps                                    # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=portfolio.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=portfolio.wsgi                     # WSGI module name
LOGFILE=/opt/portfolio/logs/gunicorn.log

#export SERVER_ENV=DEVEL

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $BASEDIR/virtualenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $BASEDIR/virtualenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-file=$LOGFILE\
