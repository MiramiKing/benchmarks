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
            labels: ['blacksheep','starlette','baize','fastapi','aiohttp','tornado','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['494445','342015','330450','234780','191400','122220','44580',],
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
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.12` | 494445 | 6.61 |
9.29 | 7.09
| [starlette](https://pypi.org/project/starlette/) `0.26.1` | 342015 | 15.97 |
18.14 | 13.97
| [baize](https://pypi.org/project/baize/) `0.20.1` | 330450 | 12.76 |
14.34 | 12.78
| [fastapi](https://pypi.org/project/fastapi/) `0.95.0` | 234780 | 18.36 |
22.71 | 17.55
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.4` | 191400 | 18.88 |
19.06 | 19.0
| [tornado](https://pypi.org/project/tornado/) `6.2` | 122220 | 24.54 |
24.75 | 24.59
| [django](https://pypi.org/project/django/) `4.2` | 44580 | 63.65 |
70.58 | 66.34


More details: [Results (2023-04-12)](_posts/2023-04-12-results.md)