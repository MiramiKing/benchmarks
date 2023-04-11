import time
from uuid import uuid4

from baize.asgi import (HTMLResponse, JSONResponse, PlainTextResponse, Request, Response, Router,
                        request_response)
from baize.exceptions import HTTPException

routes = []

# добавим простые руты
for n in range(5):
    routes.append((f"/route-{n}", HTMLResponse("ok")))
    routes.append((f"/route-dyn-{n}/{{part}}", HTMLResponse("ok")))


@request_response
async def html(request: Request) -> Response:
    content = "<b>HTML OK</b>"
    headers = {"x-time": f"{time.time()}"}
    return HTMLResponse(content, headers=headers)


@request_response
async def upload(request: Request) -> Response:
    if request.method != "POST":
        return Response(405)

    try:
        formdata = await request.form
    except HTTPException as exc:
        return Response(exc.status_code, exc.headers)

    if "file" not in formdata:
        return PlainTextResponse("ERROR", status_code=400)

    filepath = f"/tmp/{uuid4().hex}"
    await formdata["file"].asave(filepath)

    return PlainTextResponse(filepath)


@request_response
async def api(request: Request) -> Response:
    if request.method != "PUT":
        return Response(405)

    if request.headers.get("authorization") is None:
        return PlainTextResponse("ERROR", status_code=401)

    return JSONResponse(
        {
            "params": request.path_params,
            "query": dict(request.query_params),
            "data": await request.json,
        }
    )


app = Router(
    ("/html", html),
    ("/upload", upload),
    ("/api/users/{user:int}/records/{record:int}", api),
    *routes,
)
