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
* Check complete results for the latest benchmark here: [Results (2023-06-15)](_posts/2023-06-15-results.md)


## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['blacksheep','blacksheep','baize','starlette','baize','starlette','fastapi','fastapi','aiohttp','aiohttp','tornado','tornado','django','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['488070','417555','324255','317775','279480','262845','231855','193425','187590','156375','123630','102600','46215','36120',],
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


More details: [Results (2023-06-15)](_posts/2023-06-15-results.md)