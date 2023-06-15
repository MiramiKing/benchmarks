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



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22baize%22%2C%22starlette%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22tornado%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B526020%2C353400%2C336285%2C247155%2C211470%2C134790%2C52755%5D%7D%5D%7D%7D' />

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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 18565 | 2.65 | 4.86 | 3.65
| [baize](https://pypi.org/project/baize/) `0.20.3` | 13632 | 3.60 | 6.73 | 4.68
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 12446 | 3.94 | 7.36 | 5.12
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 8348 | 5.82 | 11.01 | 7.83
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7662 | 8.36 | 8.39 | 8.35
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3614 | 17.67 | 17.73 | 17.70
| [django](https://pypi.org/project/django/) `4.2.2` | 1382 | 44.51 | 45.84 | 46.55


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 10339 | 4.74 | 8.99 | 6.17
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 7399 | 6.61 | 12.51 | 8.63
| [baize](https://pypi.org/project/baize/) `0.20.3` | 6898 | 8.65 | 10.24 | 9.27
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5795 | 8.47 | 16.00 | 11.02
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3916 | 16.31 | 16.42 | 16.34
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3056 | 20.93 | 20.99 | 20.93
| [django](https://pypi.org/project/django/) `4.2.2` | 1241 | 50.06 | 51.44 | 51.56

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 6164 | 7.96 | 14.97 | 10.37
| [baize](https://pypi.org/project/baize/) `0.20.3` | 3030 | 20.24 | 23.86 | 21.14
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 2574 | 19.12 | 35.82 | 24.83
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2520 | 25.44 | 25.54 | 25.43
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 2334 | 20.98 | 39.69 | 27.38
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2316 | 27.56 | 27.68 | 27.61
| [django](https://pypi.org/project/django/) `4.2.2` | 894 | 68.85 | 77.04 | 71.49


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 526020 | 5.12 | 9.61 | 6.73
| [baize](https://pypi.org/project/baize/) `0.20.3` | 353400 | 10.83 | 13.61 | 11.7
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 336285 | 9.89 | 18.56 | 12.86
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 247155 | 11.76 | 22.23 | 15.41
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 211470 | 16.7 | 16.78 | 16.71
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 134790 | 22.05 | 22.13 | 22.08
| [django](https://pypi.org/project/django/) `4.2.2` | 52755 | 54.47 | 58.11 | 56.53

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)