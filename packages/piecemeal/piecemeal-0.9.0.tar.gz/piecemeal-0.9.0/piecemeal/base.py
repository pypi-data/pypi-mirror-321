"""Base class which libraries should inherit from."""


class PieceMealPlugin:
    # Guard against accidental import
    __is_base: bool = True
    categories: list[str] = []
    dependencies: list[str] = []

    def __init__(self):
        self.enabled = True
        self.name = type(self).__name__

    @property
    def is_base(self) -> bool:
        """
        Returns whether or not the plugin should be considered base or concrete.

        Return value is dependent on whether or not the `__is_base` attribute
        of the plugin is True or False. This is a name mangled property that
        will not propagate to subclasses. It must be either set directly in the
        Plugin class definition as a class attribute, or preferably, using the
        @piecemeal.BasePlugin decorator.

        Returns:
            bool
        """
        return getattr(self, f"_{type(self).__name__}__is_base", False)

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False
