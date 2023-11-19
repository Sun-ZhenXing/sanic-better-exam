from sanic import Sanic

from src.core import api

app = Sanic(__name__)
app.static("/", "./static")
app.blueprint(api)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, fast=True)
