# Async Python Web Frameworks comparison

https://MiramiKing.github.io/becnmarks/
----------
#### Updated: 2023-06-15

----------

This benchmark provides a straightforward evaluation of Python async web-frameworks,
with the majority of frameworks being compatible with ASGI.

While the benchmark does not assess deployment 
(such as uvicorn versus hypercorn, etc.) or databases (ORMs, drivers),
it seeks to evaluate the strength of the frameworks themselves. 
The benchmark analyzes request parsing (including body, headers, formdata, and queries), routing, and responses.

## Table of contents

* [The Methodic](#the-methodic)
* [The Results](#the-results-2023-06-15)
    * [Accept a request and return HTML response with a custom dynamic header](#html)
    * [Parse path params, query string, JSON body and return a json response](#api)
    * [Parse uploaded file, store it on disk and return a text response](#upload)
    * [Composite stats ](#composite)



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22blacksheep%22%2C%22baize%22%2C%22starlette%22%2C%22baize%22%2C%22starlette%22%2C%22fastapi%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22aiohttp%22%2C%22tornado%22%2C%22tornado%22%2C%22django%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B488070%2C417555%2C324255%2C317775%2C279480%2C262845%2C231855%2C193425%2C187590%2C156375%2C123630%2C102600%2C46215%2C36120%5D%7D%5D%7D%7D' />

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


## The Results (2023-06-15)

<h3 id="html"> Accept a request and return HTML response with a custom dynamic header</h3>
<details open>
<summary> The test simulates just a single HTML response. </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 17071 | 4.30 | 4.63 | 3.83
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 14541 | 4.68 | 5.41 | 4.49
| [baize](https://pypi.org/project/baize/) `0.20.3` | 12601 | 5.88 | 6.34 | 5.08
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 11788 | 6.41 | 6.85 | 5.39
| [baize](https://pypi.org/project/baize/) `0.20.3` | 11150 | 6.32 | 7.17 | 5.70
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 9810 | 7.01 | 8.16 | 6.50
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 8113 | 9.44 | 10.11 | 8.02
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7042 | 8.92 | 9.12 | 9.09
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 6687 | 9.89 | 12.20 | 9.76
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 5890 | 10.59 | 11.05 | 10.88
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3285 | 19.45 | 19.53 | 19.48
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2826 | 22.83 | 23.13 | 22.65
| [django](https://pypi.org/project/django/) `4.2.2` | 1204 | 50.89 | 52.34 | 53.33
| [django](https://pypi.org/project/django/) `4.2.2` | 929 | 66.60 | 72.28 | 68.95


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 9732 | 7.54 | 8.37 | 6.55
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 8698 | 7.80 | 9.54 | 7.32
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 7226 | 10.65 | 11.36 | 8.82
| [baize](https://pypi.org/project/baize/) `0.20.3` | 6258 | 10.37 | 10.60 | 10.21
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 5862 | 11.01 | 14.04 | 10.88
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5421 | 13.93 | 15.34 | 11.78
| [baize](https://pypi.org/project/baize/) `0.20.3` | 5276 | 12.03 | 12.63 | 12.12
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 4619 | 14.67 | 18.02 | 13.82
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3317 | 19.20 | 19.26 | 19.29
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2839 | 22.52 | 22.57 | 22.55
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2787 | 22.66 | 23.00 | 22.95
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2248 | 28.12 | 29.36 | 28.46
| [django](https://pypi.org/project/django/) `4.2.2` | 1073 | 57.11 | 58.56 | 59.51
| [django](https://pypi.org/project/django/) `4.2.2` | 851 | 71.12 | 80.97 | 75.04

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 5735 | 11.11 | 14.55 | 11.14
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 4598 | 13.84 | 17.79 | 13.89
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2758 | 22.28 | 26.09 | 23.22
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2206 | 27.87 | 33.04 | 28.99
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 2171 | 35.53 | 37.54 | 29.42
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2147 | 29.72 | 29.84 | 29.80
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2118 | 30.08 | 30.26 | 30.19
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1923 | 39.48 | 42.52 | 33.22
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 1851 | 39.62 | 44.02 | 34.50
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 1766 | 35.97 | 36.57 | 36.23
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 1748 | 36.04 | 37.44 | 36.60
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1589 | 45.00 | 50.19 | 40.24
| [django](https://pypi.org/project/django/) `4.2.2` | 804 | 73.85 | 77.55 | 79.32
| [django](https://pypi.org/project/django/) `4.2.2` | 628 | 97.13 | 107.08 | 101.71


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 488070 | 7.65 | 9.18 | 7.17
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 417555 | 8.77 | 10.91 | 8.57
| [baize](https://pypi.org/project/baize/) `0.20.3` | 324255 | 12.84 | 14.34 | 12.84
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 317775 | 17.53 | 18.58 | 14.54
| [baize](https://pypi.org/project/baize/) `0.20.3` | 279480 | 15.41 | 17.61 | 15.6
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 262845 | 19.21 | 22.07 | 17.29
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 231855 | 20.95 | 22.66 | 17.67
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 193425 | 23.19 | 26.8 | 21.27
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 187590 | 19.28 | 19.41 | 19.39
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 156375 | 23.1 | 23.83 | 23.48
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 123630 | 24.02 | 24.12 | 24.07
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 102600 | 28.97 | 29.69 | 29.11
| [django](https://pypi.org/project/django/) `4.2.2` | 46215 | 60.62 | 62.82 | 64.05
| [django](https://pypi.org/project/django/) `4.2.2` | 36120 | 78.28 | 86.78 | 81.9

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)