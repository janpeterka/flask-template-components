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
