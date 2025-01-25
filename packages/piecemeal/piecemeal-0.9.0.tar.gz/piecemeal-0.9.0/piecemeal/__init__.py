"""A dead simple plugin library for creating extendable applications."""

__author__ = "Darrick Herwehe"
__email__ = "darrick@exitcodeone.com"
__version__ = "0.9.0"

from .manager import PluginManager, DependencyError, CyclicalDependencyError
from .base import PieceMealPlugin
from .decorators import BasePlugin


__all__ = [
    "PluginManager",
    "DependencyError",
    "CyclicalDependencyError",
    "PieceMealPlugin",
    "BasePlugin",
]
