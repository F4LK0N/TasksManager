#! /bin/sh

python ./manage.py migrate

python ./manage.py createsuperuserwithpassword --email $ADMIN_EMAIL --username $ADMIN_LOGIN --password $ADMIN_PASS --preserve

