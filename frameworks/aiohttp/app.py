import time
from uuid import uuid4

from aiohttp.web import (RouteTableDef, Application, Response, json_response, HTTPBadRequest, HTTPUnauthorized)

routes = RouteTableDef()


# добавим маршруты

async def req_ok(request):
    return Response(text="ok")


for n in range(5):
    routes.get(f"/route-{n}")(req_ok)
    routes.get(f"/route-dyn-{n}/{{part}}")(req_ok)


# точки для бенчмарков
@routes.get('/html')
async def html(request):
    content = "<b>HTML OK</b>"
    headers = {'x-time': f"{time.time()}"}
    return Response(text=content, content_type="text/html", headers=headers)


@routes.post('/upload')
async def upload(request):
    if not request.headers['content-type'].startswith('multipart/form-data'):
        raise HTTPBadRequest()

    reader = await request.multipart()
    data = await reader.next()
    if data.name != 'file':
        raise HTTPBadRequest()

    try:
        with open(f"/tmp/{uuid4().hex}", 'wb') as target:
            target.write(await data.read())
    except Exception as e:
        print(e)


    return Response(text=target.name, content_type="text/plain")


@routes.put(r'/api/users/{user:\d+}/records/{record:\d+}')
async def api(request):
    if not request.headers.get('authorization'):
        raise HTTPUnauthorized()

    return json_response({
        'params': {
            'user': int(request.match_info['user']),
            'record': int(request.match_info['record']),
        },
        'query': dict(request.query),
        'data': await request.json(),
    })


app = Application()
app.add_routes(routes)
