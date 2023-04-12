# Async Python Web Frameworks comparison

https://MiramiKing.github.io/becnmarks/
----------
#### Updated: 2023-04-12

----------

This is a simple benchmark for python async webframeworks. Almost all of the
frameworks are ASGI-compatible. 

The objective of the benchmark is not testing deployment (like uvicorn vs
hypercorn and etc) or database (ORM, drivers) but instead test the frameworks
itself. The benchmark checks request parsing (body, headers, formdata,
queries), routing, responses.

## Table of contents

* [The Methodic](#the-methodic)
* [The Results](#the-results-2023-04-12)
    * [Accept a request and return HTML response with a custom dynamic header](#html)
    * [Parse path params, query string, JSON body and return a json response](#api)
    * [Parse uploaded file, store it on disk and return a text response](#upload)
    * [Composite stats ](#composite)



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22starlette%22%2C%22baize%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22tornado%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B494445%2C342015%2C330450%2C234780%2C191400%2C122220%2C44580%5D%7D%5D%7D%7D' />

## The Methodic

The benchmark runs as a [Github Action](https://github.com/features/actions).
According to the [github
documentation](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
the hardware specification for the runs is:

* 2-core vCPU (Intel® Xeon® Platinum 8272CL (Cascade Lake), Intel® Xeon® 8171M 2.1GHz (Skylake))
* 7 GB of RAM memory
* 14 GB of SSD disk space
* OS Ubuntu 20.04

[ASGI](https://asgi.readthedocs.io/en/latest/) apps are running from docker using the gunicorn/uvicorn command:

    gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 app:app

Applications' source code can be found
[here](https://github.com/klen/py-frameworks-bench/tree/develop/frameworks).

Results received with WRK utility using the params:

    wrk -d15s -t4 -c64 [URL]

The benchmark has a three kind of tests:

1. "Simple" test: accept a request and return HTML response with custom dynamic
   header. The test simulates just a single HTML response.

2. "API" test: Check headers, parse path params, query string, JSON body and return a json
   response. The test simulates an JSON REST API.

3. "Upload" test: accept an uploaded file and store it on disk. The test
   simulates multipart formdata processing and work with files.


## The Results (2023-04-12)

<h3 id="html"> Accept a request and return HTML response with a custom dynamic header</h3>
<details open>
<summary> The test simulates just a single HTML response. </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 17255 | 4.10 | 4.59 | 3.68
| [baize](https://pypi.org/project/baize/) `0.20.1` | 12904 | 5.64 | 6.18 | 4.96
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 12895 | 5.81 | 6.27 | 4.93
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 8230 | 6.60 | 9.99 | 8.00
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7199 | 8.76 | 8.92 | 8.89
| [tornado](https://pypi.org/project/tornado/) `6.2` | 3383 | 18.88 | 18.97 | 18.91
| [django](https://pypi.org/project/django/) `4.2` | 1165 | 52.74 | 54.24 | 55.11


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 10024 | 6.95 | 8.22 | 6.35
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 7680 | 8.29 | 10.76 | 8.30
| [baize](https://pypi.org/project/baize/) `0.20.1` | 6385 | 10.21 | 10.44 | 10.01
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 5488 | 9.24 | 15.39 | 11.63
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3358 | 18.91 | 19.06 | 19.06
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2728 | 23.40 | 23.63 | 23.46
| [django](https://pypi.org/project/django/) `4.2` | 1023 | 60.27 | 67.68 | 62.45

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 5684 | 8.79 | 15.07 | 11.24
| [baize](https://pypi.org/project/baize/) `0.20.1` | 2741 | 22.44 | 26.39 | 23.37
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 2226 | 33.80 | 37.40 | 28.68
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2203 | 28.96 | 29.21 | 29.04
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2037 | 31.34 | 31.64 | 31.40
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 1934 | 39.25 | 42.76 | 33.02
| [django](https://pypi.org/project/django/) `4.2` | 784 | 77.95 | 89.82 | 81.46


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 494445 | 6.61 | 9.29 | 7.09
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 342015 | 15.97 | 18.14 | 13.97
| [baize](https://pypi.org/project/baize/) `0.20.1` | 330450 | 12.76 | 14.34 | 12.78
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 234780 | 18.36 | 22.71 | 17.55
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 191400 | 18.88 | 19.06 | 19.0
| [tornado](https://pypi.org/project/tornado/) `6.2` | 122220 | 24.54 | 24.75 | 24.59
| [django](https://pypi.org/project/django/) `4.2` | 44580 | 63.65 | 70.58 | 66.34

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)