---
layout: home
list_title: Archive
description: Python web-frameworks benchmarks
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>

This is a simple benchmark for python async web-frameworks. Almost all of the
frameworks are ASGI-compatible (aiohttp and tornado are exceptions on the
moment).

The objective of the benchmark is not testing deployment (like uvicorn vs
hypercorn and etc) or database (ORM, drivers) but instead test the frameworks
itself. The benchmark checks request parsing (body, headers, formdata,
queries), routing, responses.

* Read about the benchmark: [The Methodic](methodic.md)
* Check complete results for the latest benchmark here: [Results (2023-04-12)](_posts/2023-04-12-results.md)


## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['blacksheep','starlette','baize','fastapi','aiohttp','tornado','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['495315','340230','330300','239400','190185','123885','45690',],
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
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 340230 | 16.54 | 17.65 | 13.68
| [baize](https://pypi.org/project/baize/) `0.20.1` | 330300 | 12.68 | 14.06 | 12.61
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 239400 | 20.42 | 21.8 | 17.07
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 190185 | 18.88 | 19.11 | 19.06
| [tornado](https://pypi.org/project/tornado/) `6.2` | 123885 | 24.02 | 24.14 | 24.11
| [django](https://pypi.org/project/django/) `4.2` | 45690 | 62.36 | 66.55 | 64.89


More details: [Results (2023-04-12)](_posts/2023-04-12-results.md)