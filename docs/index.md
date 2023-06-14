---
layout: home
list_title: Archive
description: Python web-frameworks benchmarks
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>

This benchmark provides a straightforward evaluation of Python async web-frameworks,
with the majority of frameworks being compatible with ASGI.

While the benchmark does not assess deployment 
(such as uvicorn versus hypercorn, etc.) or databases (ORMs, drivers),
it seeks to evaluate the strength of the frameworks themselves. 
The benchmark analyzes request parsing (including body, headers, formdata, and queries), routing, and responses.

* Read about the benchmark: [The Methodic](methodic.md)
* Check complete results for the latest benchmark here: [Results (2023-06-14)](_posts/2023-06-14-results.md)


## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['blacksheep','blacksheep','starlette','starlette','baize','baize','fastapi','fastapi','aiohttp','aiohttp','tornado','tornado','django','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['495315','487290','340230','336840','331215','330300','239400','234660','190185','185955','123885','119475','45690','38865',],
                    backgroundColor: [
                        '#4E79A7', '#A0CBE8', '#F28E2B', '#FFBE7D', '#59A14F', '#8CD17D', '#B6992D', 
                    ]
                },
            ]
        }
    });
</script>

Sorted by sum of completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 495315 | 6.88 | 9.12 | 7.07
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 487290 | 7.65 | 9.32 | 7.23
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 340230 | 16.54 | 17.65 | 13.68
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 336840 | 11.86 | 19.18 | 14.29
| [baize](https://pypi.org/project/baize/) `0.20.1` | 331215 | 13.14 | 14.79 | 13.17
| [baize](https://pypi.org/project/baize/) `0.20.1` | 330300 | 12.68 | 14.06 | 12.61
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 239400 | 20.42 | 21.8 | 17.07
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 234660 | 14.18 | 23.9 | 17.76
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 190185 | 18.88 | 19.11 | 19.06
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 185955 | 19.5 | 19.92 | 19.66
| [tornado](https://pypi.org/project/tornado/) `6.2` | 123885 | 24.02 | 24.14 | 24.11
| [tornado](https://pypi.org/project/tornado/) `6.2` | 119475 | 25.12 | 25.56 | 25.19
| [django](https://pypi.org/project/django/) `4.2` | 45690 | 62.36 | 66.55 | 64.89
| [django](https://pypi.org/project/django/) `4.2` | 38865 | 71.95 | 78.5 | 76.22


More details: [Results (2023-06-14)](_posts/2023-06-14-results.md)