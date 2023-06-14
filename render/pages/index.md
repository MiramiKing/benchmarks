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
* Check complete results for the latest benchmark here: [Results ({{ now.strftime('%Y-%m-%d') }})](_posts/{{ now.strftime('%Y-%m-%d') }}-results.md)


## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [{% for res in results %}'{{res.name}}',{% endfor %}],
            datasets: [
                {
                    label: '# of requests',
                    data: [{% for res in results %}'{{res.req}}',{% endfor %}],
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
{% for res in results -%}
| [{{ res.name }}](https://pypi.org/project/{{ res.name }}/) `{{ versions[res.name] }}` | {{ res.req }} | {{ res.lt50|round(2) }} | {{ res.lt75|round(2) }} | {{ res.lt_avg|round(2) }}
{% endfor %}

More details: [Results ({{ now.strftime('%Y-%m-%d') }})](_posts/{{ now.strftime('%Y-%m-%d') }}-results.md)