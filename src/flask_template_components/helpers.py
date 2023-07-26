class ComponentHelperMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        @classmethod
        def helper_method(cls, *args, **kwargs):
            return cls(*args, **kwargs).render()

        setattr(cls, "helper", helper_method)

        @classmethod
        def register_helper_method(cls, application, name: str = None):
            """creates `register_helper` method on class, which registers helper method on application

            [description]
            :param application: [description]
            :type application: Flask
            :param name: name of helper, called from jinja template, defaults to None
            :type name: str, optional
            """
            if name is None:
                name = camelcase_to_snakecase(cls.__name__)

            application.add_template_global(cls.helper, name=name)

        setattr(cls, "register_helper", register_helper_method)


def register_helpers(
    application,
    package_name="flask_template_components.components",
):
    import importlib
    import inspect

    # Import the package dynamically
    package = importlib.import_module(package_name)

    # Get all classes defined in the package
    classes = inspect.getmembers(package, inspect.isclass)

    for klassname, klass in classes:
        klass.register_helper(application)
        application.add_template_global(
            klass.helper, name=camelcase_to_snakecase(klassname)
        )
