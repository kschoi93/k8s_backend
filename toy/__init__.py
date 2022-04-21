from flask import Flask


def create_app():
    app = Flask(__name__)

    # routes list
    from .routes import routes_list
    routes_list(app)

    @app.route('/')
    def hello_world():
        return 'hello world!'

    return app