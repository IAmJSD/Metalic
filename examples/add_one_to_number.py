from sanic import Sanic
from sanic.websocket import WebSocketProtocol
from metalic import Metalic

app = Sanic(__name__)


def add_one(this):
    """Adds one to the number."""
    this['number'] += 1


@app.route("/")
async def demo_route(*_):
    instance = Metalic(app, number=0, add_one=add_one)
    return await instance.render("./html/add_one.html")


app.run(protocol=WebSocketProtocol, port=8080)
