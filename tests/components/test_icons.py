from src.flask_template_components.components import BaseIcon


def test_icon(app):
    with app.app_context():
        icon = BaseIcon()
        assert icon.render() == '<i class="cursor-default"></i>'
