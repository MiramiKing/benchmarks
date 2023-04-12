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



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22starlette%22%2C%22baize%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22tornado%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B495315%2C340230%2C330300%2C239400%2C190185%2C123885%2C45690%5D%7D%5D%7D%7D' />

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
[here](https://github.com/MiramiKing/benchmarks/tree/master/frameworks).

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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 17215 | 4.24 | 4.56 | 3.79
| [baize](https://pypi.org/project/baize/) `0.20.1` | 12814 | 5.76 | 6.08 | 4.96
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 12680 | 5.92 | 6.34 | 5.01
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 8343 | 9.08 | 9.69 | 7.66
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7144 | 8.75 | 8.95 | 8.96
| [tornado](https://pypi.org/project/tornado/) `6.2` | 3338 | 19.14 | 19.20 | 19.17
| [django](https://pypi.org/project/django/) `4.2` | 1199 | 51.36 | 58.04 | 53.48


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 10045 | 7.57 | 8.19 | 6.34
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 7699 | 9.99 | 10.69 | 8.28
| [baize](https://pypi.org/project/baize/) `0.20.1` | 6413 | 10.14 | 10.35 | 9.97
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 5635 | 13.62 | 14.55 | 11.32
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3327 | 19.08 | 19.26 | 19.24
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2825 | 22.56 | 22.65 | 22.65
| [django](https://pypi.org/project/django/) `4.2` | 1052 | 58.57 | 60.60 | 60.83

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 5761 | 8.82 | 14.61 | 11.08
| [baize](https://pypi.org/project/baize/) `0.20.1` | 2793 | 22.14 | 25.75 | 22.91
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 2303 | 33.70 | 35.93 | 27.74
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2208 | 28.81 | 29.12 | 28.98
| [tornado](https://pypi.org/project/tornado/) `6.2` | 2096 | 30.37 | 30.58 | 30.50
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 1982 | 38.57 | 41.17 | 32.24
| [django](https://pypi.org/project/django/) `4.2` | 795 | 77.14 | 81.02 | 80.36


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 495315 | 6.88 | 9.12 | 7.07
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 340230 | 16.54 | 17.65 | 13.68
| [baize](https://pypi.org/project/baize/) `0.20.1` | 330300 | 12.68 | 14.06 | 12.61
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 239400 | 20.42 | 21.8 | 17.07
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 190185 | 18.88 | 19.11 | 19.06
| [tornado](https://pypi.org/project/tornado/) `6.2` | 123885 | 24.02 | 24.14 | 24.11
| [django](https://pypi.org/project/django/) `4.2` | 45690 | 62.36 | 66.55 | 64.89

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)