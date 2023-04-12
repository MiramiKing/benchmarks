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



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22blacksheep%22%2C%22baize%22%2C%22starlette%22%2C%22baize%22%2C%22blacksheep%22%2C%22fastapi%22%2C%22starlette%22%2C%22baize%22%2C%22aiohttp%22%2C%22aiohttp%22%2C%22fastapi%22%2C%22tornado%22%2C%22aiohttp%22%2C%22flask_sync%22%2C%22django_sync%22%2C%22tornado%22%2C%22django%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B506010%2C505020%2C358755%2C352125%2C340680%2C299235%2C224565%2C215310%2C199815%2C181980%2C173640%2C145410%2C122565%2C114615%2C94950%2C77430%2C74175%2C40260%2C26880%5D%7D%5D%7D%7D' />

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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 20165 | 3.02 | 3.20 | 3.18
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 19914 | 3.03 | 3.17 | 3.24
| [baize](https://pypi.org/project/baize/) `0.20.1` | 14606 | 4.15 | 4.37 | 4.40
| [baize](https://pypi.org/project/baize/) `0.20.1` | 13994 | 4.28 | 4.66 | 4.59
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 13146 | 4.38 | 4.67 | 4.93
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 10674 | 5.42 | 7.68 | 5.98
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 8135 | 6.65 | 10.25 | 7.84
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 7975 | 7.27 | 7.69 | 8.14
| [baize](https://pypi.org/project/baize/) `0.20.1` | 7771 | 6.74 | 10.90 | 8.20
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 6232 | 10.17 | 10.43 | 10.27
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 5920 | 10.54 | 11.02 | 10.85
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 5076 | 10.21 | 16.68 | 13.68
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 4057 | 15.42 | 16.23 | 15.78
| [tornado](https://pypi.org/project/tornado/) `6.2` | 3103 | 19.18 | 20.10 | 20.78
| [flask_sync](https://pypi.org/project/flask_sync/) `` | 2484 | 24.05 | 24.77 | 25.86
| [django_sync](https://pypi.org/project/django_sync/) `` | 2009 | 28.80 | 30.97 | 32.01
| [tornado](https://pypi.org/project/tornado/) `6.2` | 1966 | 32.13 | 33.31 | 32.55
| [django](https://pypi.org/project/django/) `4.2` | 913 | 61.92 | 76.60 | 70.14
| [django](https://pypi.org/project/django/) `4.2` | 697 | 92.07 | 100.64 | 91.91


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 10513 | 5.90 | 6.15 | 6.10
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 10371 | 5.91 | 6.29 | 6.18
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 7887 | 7.82 | 8.25 | 8.14
| [baize](https://pypi.org/project/baize/) `0.20.1` | 7341 | 8.30 | 8.76 | 8.71
| [baize](https://pypi.org/project/baize/) `0.20.1` | 6830 | 8.78 | 9.68 | 9.42
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 5878 | 8.73 | 14.56 | 10.86
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 5692 | 10.87 | 11.26 | 11.26
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 4697 | 10.88 | 18.50 | 13.60
| [baize](https://pypi.org/project/baize/) `0.20.1` | 3899 | 16.41 | 17.37 | 16.40
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3510 | 17.99 | 18.44 | 18.24
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3359 | 18.50 | 19.36 | 19.06
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 3261 | 15.91 | 26.37 | 19.60
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2840 | 22.23 | 22.98 | 22.54
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2107 | 29.88 | 31.12 | 30.37
| [flask_sync](https://pypi.org/project/flask_sync/) `` | 2057 | 30.73 | 31.30 | 31.11
| [django_sync](https://pypi.org/project/django_sync/) `` | 1857 | 34.08 | 34.56 | 34.44
| [tornado](https://pypi.org/project/tornado/) `6.2` | 1677 | 37.86 | 39.16 | 38.16
| [django](https://pypi.org/project/django/) `4.2` | 1006 | 59.39 | 64.08 | 63.65
| [django](https://pypi.org/project/django/) `4.2` | 619 | 101.58 | 106.92 | 103.18

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 3397 | 15.22 | 25.32 | 18.81
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 3241 | 19.49 | 19.94 | 19.83
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 3198 | 19.61 | 20.20 | 20.09
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 2442 | 25.67 | 26.27 | 26.25
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2390 | 26.57 | 27.34 | 26.87
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2297 | 27.27 | 28.53 | 28.00
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2228 | 28.09 | 29.18 | 28.77
| [baize](https://pypi.org/project/baize/) `0.20.1` | 1970 | 32.55 | 35.18 | 32.54
| [baize](https://pypi.org/project/baize/) `0.20.1` | 1888 | 33.76 | 36.59 | 33.99
| [flask_sync](https://pypi.org/project/flask_sync/) `` | 1789 | 35.52 | 36.17 | 35.83
| [baize](https://pypi.org/project/baize/) `0.20.1` | 1651 | 37.63 | 43.57 | 38.75
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 1522 | 34.05 | 56.76 | 41.98
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 1477 | 42.78 | 44.19 | 43.29
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 1357 | 37.52 | 64.35 | 47.06
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 1304 | 46.61 | 47.90 | 47.82
| [tornado](https://pypi.org/project/tornado/) `6.2` | 1302 | 48.56 | 50.07 | 49.10
| [django_sync](https://pypi.org/project/django_sync/) `` | 1296 | 48.85 | 49.67 | 49.46
| [django](https://pypi.org/project/django/) `4.2` | 765 | 77.62 | 86.37 | 83.83
| [django](https://pypi.org/project/django/) `4.2` | 476 | 129.47 | 138.19 | 133.76


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 506010 | 9.51 | 9.9 | 9.82
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 505020 | 9.47 | 9.75 | 9.72
| [baize](https://pypi.org/project/baize/) `0.20.1` | 358755 | 15.0 | 16.1 | 15.22
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 352125 | 12.62 | 13.06 | 13.11
| [baize](https://pypi.org/project/baize/) `0.20.1` | 340680 | 15.61 | 16.98 | 16.0
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 299235 | 9.79 | 15.85 | 11.88
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 224565 | 21.58 | 22.28 | 22.41
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 215310 | 17.19 | 28.5 | 21.14
| [baize](https://pypi.org/project/baize/) `0.20.1` | 199815 | 20.26 | 23.95 | 21.12
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 181980 | 18.24 | 18.74 | 18.46
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 173640 | 18.77 | 19.64 | 19.3
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 145410 | 21.21 | 35.8 | 26.78
| [tornado](https://pypi.org/project/tornado/) `6.2` | 122565 | 23.17 | 24.09 | 24.03
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 114615 | 29.36 | 30.51 | 29.81
| [flask_sync](https://pypi.org/project/flask_sync/) `` | 94950 | 30.1 | 30.75 | 30.93
| [django_sync](https://pypi.org/project/django_sync/) `` | 77430 | 37.24 | 38.4 | 38.64
| [tornado](https://pypi.org/project/tornado/) `6.2` | 74175 | 39.52 | 40.85 | 39.94
| [django](https://pypi.org/project/django/) `4.2` | 40260 | 66.31 | 75.68 | 72.54
| [django](https://pypi.org/project/django/) `4.2` | 26880 | 107.71 | 115.25 | 109.62

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)