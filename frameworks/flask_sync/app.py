import time
from uuid import uuid4

from asgiref.wsgi import WsgiToAsgi
from flask import Flask, redirect, url_for, request, make_response, Response, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


def ok(part=None):
    return Response("ok")


# добавим простые руты
for n in range(5):
    app.add_url_rule(f"/route-{n}", view_func=ok)
    app.add_url_rule(f"/route-dyn-{n}/<int:part>", view_func=ok)


@app.route("/html", methods=HTTP_METHODS)
def html():
    content = "<b>HTML OK</b>"
    r = make_response(content)
    r.headers.set("x-time", f"{time.time()}")
    return r


@app.route("/upload", methods=HTTP_METHODS)
def upload():
    if request.method != "POST":
        return Response(status=405)

    formdata = request.files
    if len(formdata) == 0:
        return Response(status=400)

    if "file" not in formdata:
        return Response("ERROR", status=400)
    try:
        with open(f"/tmp/{uuid4().hex}", 'wb') as target:
            target.writelines(formdata.get('file'))
    except Exception as e:
        print(e)

    return Response(target.name, content_type="text/plain")


@app.route("/api/users/<int:user>/records/<int:record>", methods=HTTP_METHODS)
def api(user, record):
    if request.method != "PUT":
        return Response(status=405)

    if request.headers.get("authorization") is None:
        return Response("ERROR", status=401)

    return jsonify(
        {
            "params": {'user': user, 'record': record},
            "query": dict(request.args.to_dict()),
            "data": request.json,
        }
    )


app = WsgiToAsgi(app)
#app.run(host='0.0.0.0', port=8080)
