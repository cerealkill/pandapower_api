# REST API for Pandapower Simulations
Http API endpoint for the pandapower library

### Running on local machine
Run on the already installed Gunicorn wsgi server with 4 parallel workers.
```shell script
virutalenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:80 api.server:rest
```
Use curl or httpie to check if it works, I like [Insomnia.rest](https://insomnia.rest/download). Import the Insomnia Workspace from the `docs/` folder to hit the ground running!
````shell script
curl 127.0.0.1
http 127.0.0.1
````

For wsgi alternatives check Flask documentation [here](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/).

### Running the tests
These commands will run all the tests, static analysis, code audit and display coverage.

Powered by [pytest](https://github.com/pytest-dev/pytest) test framework, [pylama](https://github.com/klen/pylama) code audit tool, and [coveragepy](https://github.com/nedbat/coveragepy).
````shell script
coverage run -m pytest --pylama && coverage report
````

## Links
* Pandapower [website](https://www.pandapower.org/)
* Pandapower [docs](https://pandapower.readthedocs.io/en/v2.2.2/)
* Pandapower [repo](https://github.com/e2nIEE/pandapower)
* Compiled list of [REST](https://standards.rest/) standards
  * [Message Syntax and Routing](https://tools.ietf.org/html/rfc7230)
  * [Semantics and Content](https://tools.ietf.org/html/rfc7231)
  * [Conditional Requests](https://tools.ietf.org/html/rfc7232)
  * [Range Requests](https://tools.ietf.org/html/rfc7233)
  * [Caching](https://tools.ietf.org/html/rfc7234)
  * [Authentication](https://tools.ietf.org/html/rfc7235)
  * [URI](https://tools.ietf.org/html/rfc3986)
  * [JSON](https://tools.ietf.org/html/rfc8259)
  * [Datetime format](https://tools.ietf.org/html/rfc3339)
