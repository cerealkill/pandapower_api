# REST API for Pandapower Simulations
Http API endpoint for the pandapower library

```shell script
docker run -p 80:80 pauldepraz/pandapowerapi
```

To interact with API use [Insomnia.rest](https://insomnia.rest/download) and import the Insomnia Workspace from the `docs/` folder to hit the ground running!

Alternativelly, use curl or httpie on the cmd.
````shell script
curl 127.0.0.1/api/v1/run
curl 127.0.0.1/api/v1/load/active
curl 127.0.0.1/api/v1/load/reactive
````

## Continuous integrations
* Build and test pipeline on Github for all commits
* Dockerhub build updates `latest` tag for changes on the `master` branch

## Running on a local machine
Run on the already installed Gunicorn wsgi server.
```shell script
virutalenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:80 api.server:rest
```

For wsgi alternatives check Flask documentation [here](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/).

### Running the tests
These commands will run all the tests, static analysis, code audit and display coverage.

Powered by [pytest](https://github.com/pytest-dev/pytest) test framework, [pylama](https://github.com/klen/pylama) code audit tool, and [coveragepy](https://github.com/nedbat/coveragepy).
````shell script
coverage run -m pytest --pylama && coverage report
````

### Building a Docker container

Build a local docker image.
```shell script
docker build -t pauldepraz/pandapowerapi -f Dockerfile.alpine .
```

Run the container and map the internal ports to host.
```shell script
docker run -p 80:80/tcp pauldepraz/pandapowerapi
```


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
