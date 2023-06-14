---
layout: post
title: Results ({{ now.strftime('%Y-%m-%d') }})
description: Python Web-frameworks Benchmark Results ({{ now.strftime('%Y-%m-%d') }})
date:   ({{ now.strftime('%Y-%m-%d') }})
categories: results
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>

> This benchmark provides a straightforward evaluation of Python async web-frameworks,
> with the majority of frameworks being compatible with ASGI.
> 
> While the benchmark does not assess deployment 
> (such as uvicorn versus hypercorn, etc.) or databases (ORMs, drivers),
> it seeks to evaluate the strength of the frameworks themselves. 
> The benchmark analyzes request parsing (including body, headers, formdata, and queries), routing, and responses.

Read more about the benchmark: [The Methodic](/py-frameworks-bench/about/)

# Table of contents

* [Accept a request and return HTML response with a custom dynamic header](#html)
* [Parse path params, query string, JSON body and return a json response](#api)
* [Parse uploaded file, store it on disk and return a text response](#upload)
* [Composite stats ](#composite)

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    let ctx = document.getElementById('chart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [{% for res in results %}'{{res.name}}',{% endfor %}],
            datasets: [
                {
                    label: 'Single HTML response (req/s)',
                    data: [{% for res in results_html %}'{{res.req}}',{% endfor %}],
                    backgroundColor: [
                        '#b9ddf1', '#afd6ed', '#a5cfe9', '#9bc7e4', '#92c0df', '#89b8da', '#80b0d5',
                    ].reverse()
                },
                {
                    label: 'Work with JSON (req/s)',
                    data: [{% for res in results_api %}'{{res.req}}',{% endfor %}],
                    backgroundColor: [
                        '#b3e0a6', '#a5db96', '#98d687', '#8ed07f', '#85ca77', '#7dc370', '#75bc69',
                    ].reverse()
                },
                {
                    label: 'Upload file (req/s)',
                    data: [{% for res in results_upload %}'{{res.req}}',{% endfor %}],
                    backgroundColor: [
                        '#ffc685', '#fcbe75', '#f9b665', '#f7ae54', '#f5a645', '#f59c3c', '#f49234', 
                    ].reverse()
                },
            ]
        }
    });
</script>

##  Accept a request and return HTML response with a custom dynamic header {{'{#html}'}}

The test simulates just a single HTML response.

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
{% for res in results_html -%}
| [{{ res.name }}](https://pypi.org/project/{{ res.name }}/) `{{ versions[res.name] }}` | {{ res.req }} | {{ res.lt50 }} | {{ res.lt75 }} | {{ res.lt_avg }}
{% endfor %}

## Parse path params, query string, JSON body and return a json response  {{'{#api}'}}
The test simulates a simple JSON REST API endpoint.  

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
{% for res in results_api -%}
| [{{ res.name }}](https://pypi.org/project/{{ res.name }}/) `{{ versions[res.name] }}` | {{ res.req }} | {{ res.lt50 }} | {{ res.lt75 }} | {{ res.lt_avg }}
{% endfor %}

## Parse uploaded file, store it on disk and return a text response  {{'{#upload}'}}
The test simulates multipart formdata processing and work with files.  

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
{% for res in results_upload -%}
| [{{ res.name }}](https://pypi.org/project/{{ res.name }}/) `{{ versions[res.name] }}` | {{ res.req }} | {{ res.lt50 }} | {{ res.lt75 }} | {{ res.lt_avg }}
{% endfor %}

## Composite stats {{'{#composite}'}}
Combined benchmarks results

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
{% for res in results -%}
| [{{ res.name }}](https://pypi.org/project/{{ res.name }}/) `{{ versions[res.name] }}` | {{ res.req }} | {{ res.lt50|round(2) }} | {{ res.lt75|round(2) }} | {{ res.lt_avg|round(2) }}
{% endfor %}