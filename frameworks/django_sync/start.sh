#!/bin/sh

cd ..
/usr/local/bin/gunicorn -b 0.0.0.0:8080 app.app:app