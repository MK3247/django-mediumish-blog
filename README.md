# Django Blog

[![](https://img.shields.io/pypi/pyversions/Django.svg)](https://python.org/downloads/)
[![](https://img.shields.io/badge/django-2.0%20%7C%202.1%20%7C%202.2-success.svg)](https://djangoproject.com/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://choosealicense.com/licenses/mit/)

Mediumish blog using Django Framework

Features
=
* Search 
* Comments 
* Tags 
* Search by Tags 
* Post by similarities
* Customized admin panel

How To Use
=
## clone the project and install the requirements 

> Make sure you have already installed python3 and git.
```
$ git clone https://github.com/MK3247/django-mediumish-blog.git && cd django-mediumish-blog
$ pipenv install -r requirements.txt
```
## Migrate & Collect Static
```
$ python manage.py migrate
$ python manage.py collectstatic
```
## Create Admin User
```
$ python manage.py createsuperuser
```
## Run Server
```
$ python manage.py runserver
```
> Enter your browser http://localhost:8000/. You can login via admin in http://localhost:8000/admin/.

TODOS
=
- Change Style
- Reply comment
- Create following system
- Read later post
- Like post
