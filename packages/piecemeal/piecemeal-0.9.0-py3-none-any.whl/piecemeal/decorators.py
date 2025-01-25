from .base import PieceMealPlugin


def BasePlugin(plugin) -> PieceMealPlugin:
    """
    Mark a plugin as a Non-concrete implementation to avoid loading it.

    This decorator adds a name mangled property to the plugin to ensure that it
    is not propagated to any Subclasses.
    """
    basekey = f"_{plugin.__name__}__is_base"
    setattr(plugin, basekey, True)
    return plugin
