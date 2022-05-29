* chech version of python 

        python --version

* setup environment for python project

        python -m venv .venv

* install python and upgrade

        pip install --upgrade pip

* Install django and it's version 4

        pip install django

* create project level application.

        django-admin startproject todo_rest

* create app level application

        python manage.py startapp todo_app

* run your project

        python manage.py runserver

* create requirements.txt files which holds the all installed packages

        pip freeze > requirements.txt

* Migrate the data in sqlite3 database 

        python manage.py makemigrations 
        python manage.py migrate

* create super user

        python manage.py createsuperuser

* create login app

        python manage.py startapp login_app

* create a middleware app

        python manage.py startapp ipfilter_middleware






