from flask import Blueprint

bp = Blueprint("template_components", __name__, template_folder="templates")


class TemplateComponents:
    """Flask extension object

    Adds the following template functions via context_processor:
        * `render_class` for rendering css class string in templates
        * `render_data` for rendering data attributes in templates

    Usage:

    .. code-block:: python

        # app/__init__.py
        from flask import Flask
        from flask_template_component import TemplateComponents

        components = TemplateComponents()


        def create_app():
            application = Flask()
            # (...)
            components.init_app(application)
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(bp)

        @app.context_processor
        def utility_processor():
            from markupsafe import Markup

            def render_class(classes: str) -> Markup:
                """helper for rendering class string

                :param classes: string of css classes
                :type classes: str
                :returns: markup string to use inside HTML
                :rtype: {Markup}
                """
                if not classes or len(str(classes)) == 0:
                    return ""

                return Markup(f'class="{classes}"')

            def render_data(data: dict) -> Markup:
                """helper for rendering data attributes

                :param data: dictionary of data attributes
                :type data: dict
                :returns: markup string to use inside HTML
                :rtype: {Markup}
                """
                if not data:
                    return ""

                return Markup(" ".join([f"data-{k}='{v}'" for k, v in data.items()]))

            return dict(render_class=render_class, render_data=render_data)
