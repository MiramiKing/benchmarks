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
            labels: ['blacksheep','baize','starlette','fastapi','aiohttp','tornado','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['526020','353400','336285','247155','211470','134790','52755',],
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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.15` | 526020 | 5.12 | 9.61 | 6.73
| [baize](https://pypi.org/project/baize/) `0.20.3` | 353400 | 10.83 | 13.61 | 11.7
| [starlette](https://pypi.org/project/starlette/) `0.28.0` | 336285 | 9.89 | 18.56 | 12.86
| [fastapi](https://pypi.org/project/fastapi/) `0.97.0` | 247155 | 11.76 | 22.23 | 15.41
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 211470 | 16.7 | 16.78 | 16.71
| [tornado](https://pypi.org/project/tornado/) `6.3.2` | 134790 | 22.05 | 22.13 | 22.08
| [django](https://pypi.org/project/django/) `4.2.2` | 52755 | 54.47 | 58.11 | 56.53


More details: [Results (2023-06-15)](_posts/2023-06-15-results.md)