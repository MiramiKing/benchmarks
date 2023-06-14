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
            labels: ['blacksheep','baize','starlette','fastapi','aiohttp','tornado','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['488070','324255','317775','231855','187590','123630','46215',],
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
| [baize](https://pypi.org/project/baize/) `0.20.3` | 324255 | 12.84 | 14.34 | 12.84
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 317775 | 17.53 | 18.58 | 14.54
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 231855 | 20.95 | 22.66 | 17.67
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 187590 | 19.28 | 19.41 | 19.39
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 123630 | 24.02 | 24.12 | 24.07
| [django](https://pypi.org/project/django/) `4.2.2` | 46215 | 60.62 | 62.82 | 64.05


More details: [Results (2023-06-14)](_posts/2023-06-14-results.md)