class ComponentHelperMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        @classmethod
        def helper_method(cls, *args, **kwargs):
            return cls(*args, **kwargs).render()

        setattr(cls, "helper", helper_method)

        @classmethod
        def register_helper_method(cls, application, name: str = None):
            """registers helper method on application

            [description]

            :param application: Flask appplication object
            :type application: Flask
            :param name: name of helper, called from jinja template, defaults to None
            :type name: str, optional
            """
            if name is None:
                name = camelcase_to_snakecase(cls.__name__)

            application.add_template_global(cls.helper, name=name)

        setattr(cls, "register_helper", register_helper_method)


def register_helpers(application):
    """register all helpers in a package

    [description]
    :param application: Flask application object
    :type application: Flask
    """
    import importlib
    import inspect

    # Import the package dynamically
    package = importlib.import_module("flask_template_components.components")

    # Get all classes defined in the package
    classes = inspect.getmembers(package, inspect.isclass)

    for klassname, klass in classes:
        klass.register_helper(application)
        application.add_template_global(
            klass.helper, name=camelcase_to_snakecase(klassname)
        )
