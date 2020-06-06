# pandapower_api
Http API endpoint for the pandapower library

### Running the tests
These commands will run all the tests, static analysis, code audit and display coverage.

Powered by [pytest](https://github.com/pytest-dev/pytest) test framework, [pylama](https://github.com/klen/pylama) code audit tool, and [coveragepy](https://github.com/nedbat/coveragepy).
````shell script
coverage run -m pytest --pylama
coverage report
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
