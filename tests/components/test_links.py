from src.flask_template_components.components import Link


def test_link(app):
    with app.app_context():
        link = Link("tardis.blue", "enter")
        assert link.path == "tardis.blue"
        assert link.value == "enter"
        assert link.render() == '<a href="tardis.blue">enter</a>'


def test_link_with_multiple_kwargs(app):
    with app.app_context():
        link = Link("tardis.blue", "enter", classes="btn btn-primary", data={"id": 1})
        assert link.path == "tardis.blue"
        assert link.value == "enter"
        assert (
            link.render()
            == '<a href="tardis.blue" class="btn btn-primary" data-id="1">enter</a>'
        )
