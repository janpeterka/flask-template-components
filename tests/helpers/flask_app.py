from flask import Flask, request, render_template_string
from markupsafe import Markup

from src.flask_template_components import TemplateComponents


def create_app():
    app = Flask(__name__)

    tc = TemplateComponents()
    tc.init_app(app)
    tc.register_helpers()

    @app.route("/")
    def index():
        return "Hello, World!"

    @app.route("/link-component")
    def link_component():
        from src.flask_template_components.components import Link

        path = request.args.get("path")
        value = request.args.get("value")

        link = Link(path, value)
        return Markup(link.render())

    @app.route("/link-helper")
    def link_helper():
        path = request.args.get("path")
        value = request.args.get("value")

        return render_template_string("{{ link(path, value) }}")

    return app
