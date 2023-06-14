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



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22blacksheep%22%2C%22blacksheep%22%2C%22starlette%22%2C%22starlette%22%2C%22baize%22%2C%22baize%22%2C%22baize%22%2C%22starlette%22%2C%22fastapi%22%2C%22fastapi%22%2C%22fastapi%22%2C%22aiohttp%22%2C%22aiohttp%22%2C%22aiohttp%22%2C%22tornado%22%2C%22tornado%22%2C%22tornado%22%2C%22django%22%2C%22django%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B495315%2C487290%2C431400%2C340230%2C336840%2C331215%2C330300%2C297210%2C289665%2C239400%2C234660%2C205095%2C190185%2C185955%2C167745%2C123885%2C119475%2C108585%2C45690%2C38865%2C36225%5D%7D%5D%7D%7D' />

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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 17215 | 4.24 | 4.56 | 3.79
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 16999 | 4.21 | 4.66 | 3.74
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 15095 | 4.57 | 5.20 | 4.26
| [baize](https://pypi.org/project/baize/) `0.20.3` | 13156 | 5.63 | 6.09 | 4.83
| [baize](https://pypi.org/project/baize/) `0.20.3` | 12814 | 5.76 | 6.08 | 4.96
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 12715 | 5.45 | 6.36 | 5.00
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 12680 | 5.92 | 6.34 | 5.01
| [baize](https://pypi.org/project/baize/) `0.20.3` | 11760 | 6.00 | 6.88 | 5.40
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 10801 | 6.47 | 7.54 | 5.89
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 8343 | 9.08 | 9.69 | 7.66
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 8241 | 6.51 | 10.12 | 7.83
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7144 | 8.75 | 8.95 | 8.96
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 7012 | 9.01 | 9.14 | 9.13
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 7003 | 9.32 | 11.78 | 9.42
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 6362 | 10.10 | 10.33 | 10.06
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3338 | 19.14 | 19.20 | 19.17
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 3278 | 19.44 | 19.73 | 19.53
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2963 | 21.53 | 22.27 | 21.61
| [django](https://pypi.org/project/django/) `4.2.2` | 1199 | 51.36 | 58.04 | 53.48
| [django](https://pypi.org/project/django/) `4.2.2` | 1014 | 59.51 | 64.81 | 63.29
| [django](https://pypi.org/project/django/) `4.2.2` | 897 | 68.62 | 74.41 | 71.40


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 10045 | 7.57 | 8.19 | 6.34
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 9953 | 7.47 | 8.25 | 6.39
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 8885 | 7.72 | 9.24 | 7.17
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 7699 | 9.99 | 10.69 | 8.28
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 7570 | 6.87 | 11.07 | 8.43
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 6575 | 10.58 | 12.60 | 9.70
| [baize](https://pypi.org/project/baize/) `0.20.3` | 6413 | 10.14 | 10.35 | 9.97
| [baize](https://pypi.org/project/baize/) `0.20.3` | 6317 | 10.27 | 10.63 | 10.13
| [baize](https://pypi.org/project/baize/) `0.20.3` | 5673 | 11.39 | 11.79 | 11.27
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5635 | 13.62 | 14.55 | 11.32
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5519 | 9.20 | 15.52 | 11.56
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 5025 | 13.19 | 16.69 | 12.70
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3327 | 19.08 | 19.26 | 19.24
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 3275 | 19.34 | 19.89 | 19.55
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2941 | 21.73 | 22.29 | 21.77
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2825 | 22.56 | 22.65 | 22.65
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2719 | 23.44 | 23.83 | 23.54
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2469 | 26.03 | 26.79 | 25.93
| [django](https://pypi.org/project/django/) `4.2.2` | 1052 | 58.57 | 60.60 | 60.83
| [django](https://pypi.org/project/django/) `4.2.2` | 903 | 67.78 | 71.09 | 70.82
| [django](https://pypi.org/project/django/) `4.2.2` | 874 | 71.11 | 77.25 | 73.13

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 5761 | 8.82 | 14.61 | 11.08
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 5534 | 11.26 | 15.05 | 11.55
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 4780 | 12.89 | 17.48 | 13.37
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2793 | 22.14 | 25.75 | 22.91
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2608 | 23.51 | 27.65 | 24.56
| [baize](https://pypi.org/project/baize/) `0.20.3` | 2381 | 25.68 | 30.48 | 26.88
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 2303 | 33.70 | 35.93 | 27.74
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2208 | 28.81 | 29.12 | 28.98
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 2171 | 23.26 | 40.12 | 29.43
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 2110 | 30.15 | 30.72 | 30.30
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 2096 | 30.37 | 30.58 | 30.50
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1982 | 38.57 | 41.17 | 32.24
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 1968 | 32.49 | 33.11 | 32.50
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 1935 | 37.35 | 42.54 | 33.02
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1884 | 26.83 | 46.05 | 33.89
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 1880 | 33.70 | 34.86 | 34.02
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 1807 | 35.41 | 36.38 | 35.40
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 1645 | 42.39 | 50.16 | 38.85
| [django](https://pypi.org/project/django/) `4.2.2` | 795 | 77.14 | 81.02 | 80.36
| [django](https://pypi.org/project/django/) `4.2.2` | 674 | 88.56 | 99.59 | 94.56
| [django](https://pypi.org/project/django/) `4.2.2` | 644 | 96.47 | 105.86 | 99.22


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 495315 | 6.88 | 9.12 | 7.07
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 487290 | 7.65 | 9.32 | 7.23
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 431400 | 8.39 | 10.64 | 8.27
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 340230 | 16.54 | 17.65 | 13.68
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 336840 | 11.86 | 19.18 | 14.29
| [baize](https://pypi.org/project/baize/) `0.20.3` | 331215 | 13.14 | 14.79 | 13.17
| [baize](https://pypi.org/project/baize/) `0.20.3` | 330300 | 12.68 | 14.06 | 12.61
| [baize](https://pypi.org/project/baize/) `0.20.3` | 297210 | 14.36 | 16.38 | 14.52
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 289665 | 18.13 | 20.89 | 16.2
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 239400 | 20.42 | 21.8 | 17.07
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 234660 | 14.18 | 23.9 | 17.76
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 205095 | 21.63 | 26.21 | 20.32
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 190185 | 18.88 | 19.11 | 19.06
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 185955 | 19.5 | 19.92 | 19.66
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 167745 | 21.84 | 22.49 | 21.95
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 123885 | 24.02 | 24.14 | 24.11
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 119475 | 25.12 | 25.56 | 25.19
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 108585 | 27.66 | 28.48 | 27.65
| [django](https://pypi.org/project/django/) `4.2.2` | 45690 | 62.36 | 66.55 | 64.89
| [django](https://pypi.org/project/django/) `4.2.2` | 38865 | 71.95 | 78.5 | 76.22
| [django](https://pypi.org/project/django/) `4.2.2` | 36225 | 78.73 | 85.84 | 81.25

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)