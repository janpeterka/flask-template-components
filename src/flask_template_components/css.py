from typing import Union


class CSSClasses:
    """Allows simpler management of css classes for Components

    Every component has `css_classes` attribute which is an instance of this class.
    This simplifies adding css classes to components.

    FUTURE: It will be enabled to subclass this class to add custom functionality.
    """

    def __init__(self, initial_classes: Union[str, list[str]] = None):
        self.css_classes = ""
        self.append(initial_classes)

    def __str__(self):
        return self.css_classes

    def append(self, new_classes: Union[str, list[str]]):
        """Add css classes to class list

        Used for adding css classes to component dynamically, without having to manage correct spaces and all.

        Examples:
        >> self.css_classes.append("btn")
        >> self.css_classes.append("btn btn-primary")
        >> self.css_classes.append(["btn", "btn-primary"])

        :param new_classes: css classes to add
        :type new_classes: Union[str, list[str]]
        :raises: TypeError
        """
        if isinstance(new_classes, list):
            new_classes = " ".join(new_classes)
        elif isinstance(new_classes, str):
            new_classes = new_classes.strip()
        else:
            raise TypeError("New classes must be a string.")

        if self.css_classes:
            self.css_classes += f" {new_classes}"
        else:
            self.css_classes = new_classes
