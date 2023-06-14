# Async Python Web Frameworks comparison

https://MiramiKing.github.io/becnmarks/
----------
#### Updated: 2023-06-14

----------

This benchmark provides a straightforward evaluation of Python async web-frameworks,
with the majority of frameworks being compatible with ASGI.

While the benchmark does not assess deployment 
(such as uvicorn versus hypercorn, etc.) or databases (ORMs, drivers),
it seeks to evaluate the strength of the frameworks themselves. 
The benchmark analyzes request parsing (including body, headers, formdata, and queries), routing, and responses.

## Table of contents

* [The Methodic](#the-methodic)
* [The Results](#the-results-2023-06-14)
    * [Accept a request and return HTML response with a custom dynamic header](#html)
    * [Parse path params, query string, JSON body and return a json response](#api)
    * [Parse uploaded file, store it on disk and return a text response](#upload)
    * [Composite stats ](#composite)



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22baize%22%2C%22starlette%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22tornado%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B488070%2C324255%2C317775%2C231855%2C187590%2C123630%2C46215%5D%7D%5D%7D%7D' />

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


## The Results (2023-06-14)

<h3 id="html"> Accept a request and return HTML response with a custom dynamic header</h3>
<details open>
<summary> The test simulates just a single HTML response. </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 17071 | 4.30 | 4.63 | 3.83
| [baize](https://pypi.org/project/baize/) `0.20.3` | 12601 | 5.88 | 6.34 | 5.08
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 11788 | 6.41 | 6.85 | 5.39
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 8113 | 9.44 | 10.11 | 8.02
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7042 | 8.92 | 9.12 | 9.09
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3285 | 19.45 | 19.53 | 19.48
| [django](https://pypi.org/project/django/) `4.2.2` | 1204 | 50.89 | 52.34 | 53.33


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 9732 | 7.54 | 8.37 | 6.55
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 7226 | 10.65 | 11.36 | 8.82
| [baize](https://pypi.org/project/baize/) `0.20.3` | 6258 | 10.37 | 10.60 | 10.21
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5421 | 13.93 | 15.34 | 11.78
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3317 | 19.20 | 19.26 | 19.29
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2839 | 22.52 | 22.57 | 22.55
| [django](https://pypi.org/project/django/) `4.2.2` | 1073 | 57.11 | 58.56 | 59.51

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 5735 | 11.11 | 14.55 | 11.14
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2758 | 22.28 | 26.09 | 23.22
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 2171 | 35.53 | 37.54 | 29.42
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2147 | 29.72 | 29.84 | 29.80
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2118 | 30.08 | 30.26 | 30.19
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1923 | 39.48 | 42.52 | 33.22
| [django](https://pypi.org/project/django/) `4.2.2` | 804 | 73.85 | 77.55 | 79.32


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 488070 | 7.65 | 9.18 | 7.17
| [baize](https://pypi.org/project/baize/) `0.20.3` | 324255 | 12.84 | 14.34 | 12.84
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 317775 | 17.53 | 18.58 | 14.54
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 231855 | 20.95 | 22.66 | 17.67
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 187590 | 19.28 | 19.41 | 19.39
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 123630 | 24.02 | 24.12 | 24.07
| [django](https://pypi.org/project/django/) `4.2.2` | 46215 | 60.62 | 62.82 | 64.05

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)