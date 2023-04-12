---
layout: home
list_title: Archive
description:  Python webframeworks benchmarks
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>

This is a simple benchmark for python async webframeworks. Almost all of the
frameworks are ASGI-compatible. 

The objective of the benchmark is not testing deployment (like uvicorn vs
hypercorn and etc) or database (ORM, drivers) but instead test the frameworks
itself. The benchmark checks request parsing (body, headers, formdata,
queries), routing, responses.

* Read about the benchmark: [The Methodic](methodic.md)
* Check complete results for the latest benchmark here: [Results (2023-04-12)](_posts/2023-04-12-results.md)

## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    let ctx = document.getElementById('chart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['blacksheep','blacksheep','baize','starlette','baize','blacksheep','fastapi','starlette','baize','aiohttp','aiohttp','fastapi','tornado','aiohttp','flask_sync','django_sync','tornado','django','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['506010','505020','358755','352125','340680','299235','224565','215310','199815','181980','173640','145410','122565','114615','94950','77430','74175','40260','26880',],
                    backgroundColor: [
                        '#4E79A7', '#A0CBE8', '#F28E2B', '#FFBE7D', '#59A14F', '#8CD17D', '#B6992D', '#F1CE63',
                    ]
                },
            ]
        }
    });
</script>

Sorted by sum of completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 506010 | 9.51 |
9.9 | 9.82
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 505020 | 9.47 |
9.75 | 9.72
| [baize](https://pypi.org/project/baize/) `0.20.1` | 358755 | 15.0 |
16.1 | 15.22
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 352125 | 12.62 |
13.06 | 13.11
| [baize](https://pypi.org/project/baize/) `0.20.1` | 340680 | 15.61 |
16.98 | 16.0
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 299235 | 9.79 |
15.85 | 11.88
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 224565 | 21.58 |
22.28 | 22.41
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 215310 | 17.19 |
28.5 | 21.14
| [baize](https://pypi.org/project/baize/) `0.20.1` | 199815 | 20.26 |
23.95 | 21.12
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 181980 | 18.24 |
18.74 | 18.46
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 173640 | 18.77 |
19.64 | 19.3
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 145410 | 21.21 |
35.8 | 26.78
| [tornado](https://pypi.org/project/tornado/) `6.2` | 122565 | 23.17 |
24.09 | 24.03
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 114615 | 29.36 |
30.51 | 29.81
| [flask_sync](https://pypi.org/project/flask_sync/) `` | 94950 | 30.1 |
30.75 | 30.93
| [django_sync](https://pypi.org/project/django_sync/) `` | 77430 | 37.24 |
38.4 | 38.64
| [tornado](https://pypi.org/project/tornado/) `6.2` | 74175 | 39.52 |
40.85 | 39.94
| [django](https://pypi.org/project/django/) `4.2` | 40260 | 66.31 |
75.68 | 72.54
| [django](https://pypi.org/project/django/) `4.2` | 26880 | 107.71 |
115.25 | 109.62


More details: [Results (2023-04-12)](_posts/2023-04-12-results.md)