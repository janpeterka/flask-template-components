from src.flask_template_components import BaseComponent


def test_base_component(app):
    with app.app_context():
        component = BaseComponent()
