from flask import Flask
from backend.src.web.frontend_hosting import frontend_hosting
from backend.src.api.controller.tag import tag
from backend.src.api.controller.video_list import video_info


app = Flask(
    __name__,
    template_folder='../../dist',
    static_folder='../../dist/static'
)
app.register_blueprint(frontend_hosting)
app.register_blueprint(video_info)
app.register_blueprint(tag)


if __name__ == '__main__':
    app.run(debug=True)
