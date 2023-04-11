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
* Check complete results for the latest benchmark here: [Results ({{ now.strftime('%Y-%m-%d') }})](_posts/{{ now.strftime('%Y-%m-%d') }}-results.md)

## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    let ctx = document.getElementById('chart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [{% for res in results %}'{{res.name}}',{% endfor %}],
            datasets: [
                {
                    label: '# of requests',
                    data: [{% for res in results %}'{{res.req}}',{% endfor %}],
                    backgroundColor: [
                        '#4E79A7', '#A0CBE8', '#F28E2B', '#FFBE7D', '#59A14F', '#8CD17D', '#B6992D', '#F1CE63', '#499894', '#86BCB6', '#E15759', '#FF9D9A', '#79706E', '#BAB0AC', '#D37295', '#FABFD2', '#B07AA1', '#D4A6C8', '#9D7660', '#D7B5A6',
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
| [{{res.name }}](https://pypi.org/project/{{ res.name }}/) `{{versions[res.name] }}` | {{  res.req  }} | {{ res.lt50|round(2) }} |
{{ res.lt75|round(2)  }} | {{res.lt_avg|round(2) }}
{% endfor %}

More details: [Results ({{ now.strftime('%Y-%m-%d') }})](_posts/{{ now.strftime('%Y-%m-%d') }}-results.md)