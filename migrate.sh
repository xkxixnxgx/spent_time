#!/bin/sh
 
export FLASK_APP=webapp && flask db migrate -m "Миграция базы данных"

