## Technical decisions over the course of this project

### Strategy & Project Organizaiton
* Plan a first release features using Github's [Kanban](https://github.com/cerealkill/pandapower_api/projects/1).
* Plan a first release features using Github's [Kanban](https://github.com/cerealkill/pandapower_api/projects/1).
* Test-Driven Development approach to technical features, so test first, implement next.
* Use [Github](https://github.com/cerealkill/pandapower_api/actions) Continuous Integrations tools to automate build and test.
* Use [Dockerhub](https://hub.docker.com/repository/docker/pauldepraz/pandapowerapi/builds) Continuous Integrations tools to automate deployment and distribution.

### REST API Frameworks
* Tried [EVE Framework](https://docs.python-eve.org/en/stable/), my favorite, but the restriction to use a secondary application as a database made me change my mind.
* Tried [Django-Rest-Framework](https://www.django-rest-framework.org/), the branch still available [here](https://github.com/cerealkill/pandapower_api/tree/django_rest_api). I used to work with Django and it is just an overkill for this project, I would take a lot longer to remember and learn all the Django details and tools than using Flask.
* Used [Flask](https://flask.palletsprojects.com/en/1.1.x/), the framework I used most in my Python career and am very comfortable with.

### WSGI Server
* Used [Gunicorn](https://gunicorn.org/) that is shipped in the Python package manager and is pretty solid, can use multiple workers and other nice features. That is what I used for scaling apis in the past.

## Swagger
* Used [Flask-restful-swagger](https://github.com/rantav/flask-restful-swagger)

## Docker
* Used Debian based because I couldn't find the Alpine libraries I needed to compile pandapower. This makes the container a bit larger.
