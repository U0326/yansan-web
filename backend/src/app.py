from flask import Flask
from backend.src.web.frontend_hosting import frontend_hosting
from backend.src.api.random import random
from backend.src.api.controller.tag import tag


app = Flask(
    __name__,
    template_folder='../../dist',
    static_folder='../../dist/static'
)
app.register_blueprint(frontend_hosting)
app.register_blueprint(random)
app.register_blueprint(tag)


if __name__ == '__main__':
    app.run(debug=True)
