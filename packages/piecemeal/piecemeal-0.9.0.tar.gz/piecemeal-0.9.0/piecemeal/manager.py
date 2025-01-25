from __future__ import annotations

import sys
import importlib
import inspect
import pkgutil
from pathlib import Path
from collections import UserList
from graphlib import TopologicalSorter, CycleError
from types import ModuleType
from typing import Sequence

from piecemeal.base import PieceMealPlugin


class DependencyError(Exception):
    pass


class CyclicalDependencyError(Exception):
    pass


class PluginManager(UserList):
    def __init__(self, existing_plugins: list[PieceMealPlugin] | None = None):
        """
        Manage the loading, storing and querying of all plugins.

        The `PluginManager` is the main entry point into PieceMeal. It
        provides several methods for loading plugins and retrieving them back.
        You are able to get all plugins available, filter by category, or
        select single plugins by name. The only prerequisite for loading a
        plugin is that it is a class that inherits from `PieceMealPlugin` and
        it resides in an importable module.

        `PluginManager` does not guarantee an order that plugins will be
        returned except that any dependencies will come before the plugin that
        depends on them.

        Kwargs:
            existing_plugins (list[PieceMealPlugin]): A list of plugins to
                prepopulated the manager. This is mostly for internal use by
                the `PluginManager` so that a new `PluginManager` can be
                returned when filtering lists of plugins (e.g. from the
                `filter_by_categories` method). Typically the user will
                instantiate a blank PluginManager.
        """
        super().__init__()
        self._plugins_by_name: dict[str, PieceMealPlugin] = dict()
        self._plugins_by_category: dict[str, list[PieceMealPlugin]] = dict()
        self._plugin_tree = dict()  # type: ignore[var-annotated]
        if existing_plugins is None:
            existing_plugins = list()
        for plugin in existing_plugins:
            self._save_plugin(plugin)

    def clear(self) -> None:
        """
        Clear the PluginManager of all plugins.

        Acts the same as list.clear(), but also clears the PluginManager's
        internal cache.
        """
        super().clear()
        self._plugins_by_name = dict()
        self._plugins_by_category = dict()
        self._plugin_tree = dict()

    def load_from_import(
        self, module: ModuleType, as_categories: Sequence[str] | str | None = None
    ) -> PluginManager:
        """
        Load plugins located within the given Module or Package.

        When loading, only classes who have `PieceMealPlugin` somewhere in
        their inheritance heirarchy will be loaded as a plugin. Any helper
        classes and functions will be ignored. Additionally, any
        `PieceMealPlugin` subclasses decorated with
        `@piecemeal.BasePlugin` will also be ignored.

        Args:
            module (module): An already imported python module object. If the
                module is a package, PieceMeal will recursively search inside
                the package for plugins.
        Kwargs:
            as_categories (list,str): Apply categories to all plugins found
                in the module at load time. `as_categories` can be a single
                string, or a list of strings. See `apply_categories` for
                more information.

                `as_categories` is basically a shortcut for:

                ```python
                plugins = plugin_manager.load_from_import(module)
                for plugin in plugins:
                        plugin_manager.apply_categories(category_name, plugin)
                ```
        Returns:
            PluginManager

            A new `PluginManager` object containing only plugins loaded during
            this call. All newly loaded plugins are also added to the original
            `PluginManager`.
        """
        plugins = self._load_from_import(module, as_categories=as_categories)
        return PluginManager(plugins)

    def load_from_paths(
        self,
        fp: str | Path | Sequence[str | Path],
        recursive: bool = False,
        as_categories: list | str | None = None,
    ) -> PluginManager:
        """
        Load plugins from one or more files or directories.

        Due to Python's import rules, any plugin files must be a valid python
        module (i.e. ending with `.py`). See `PluginManager.load_from_import`
        for more details on how plugins are loaded.

        If `fp` is a directory, PieceMeal will _non-recursively_ search all
        `.py` files within the directory for plugins unless `recursive` is set
        to True.

        Args:
            fp (str,Path,Sequence): A list of `Path` objects or absolute
                paths in `str` form. As a convenience, a single `Path` or `str`
                can be passed as well.
        Kwargs:
            recursive (bool): Whether or not directories should be searched
                recursively. If `fp` is a file, this option is ignored.
                Default is `False`
            as_categories (list,str): Apply categories to all plugins found in
                the module at load time. `as_categories` can be a single `str`,
                or a list of `str`. See `apply_categories` for more information.

                `as_categories` is basically a shortcut for:

                ```python
                plugins = plugin_manager.load_from_paths("/path/to/plugins.py")
                for plugin in plugins:
                        plugin_manager.apply_categories(category_name, plugin)
                ```
        Returns:
            PluginManager

            A new `PluginManager` object containing only plugins loaded during
            this call. All newly loaded plugins are also added to the original
            `PluginManager`.
        """
        # Convert convenience args to expected list type
        if isinstance(fp, str | Path):
            fp = [fp]
        all_paths = [Path(f) for f in fp]

        plugins = []
        for pth in all_paths:
            if pth.is_dir():
                loaded = self._load_directory(
                    pth, recursive=recursive, as_categories=as_categories
                )
                plugins.extend(loaded)
            elif pth.exists():
                plugins.extend(self._load_from_file(pth, as_categories=as_categories))
            else:
                raise FileNotFoundError(f"Error loading plugins from: '{pth}'")
        return PluginManager(plugins)

    def resolve_dependencies(self) -> None:
        try:
            self.data = self._order_by_dependency(self.data)
            self._plugins_by_category = {
                category: self._order_by_dependency(plugins)
                for category, plugins in self._plugins_by_category.items()
            }
        except CycleError as e:
            cycle = " -> ".join([plugin.name for plugin in e.args[1]])
            msg = f"Cyclical dependencies found among plugins: [{cycle}]"
            raise CyclicalDependencyError(msg)
        # also do categories

    def filter_by_categories(
        self, categories: str | Sequence[str], include_disabled: bool = False
    ) -> PluginManager:
        """
        Retrieve only plugins that are defined as one of the given categories.

        Categories are defined by the `categories` attribute on the plugin or
        any of its superclasses.

        Args:
            categories (str,Sequence): The categories to filter by. Plugins will
                be filtered against _all_ of the items of the list, which act as
                an `and` clause. For convenience, a `str` can be passed as the
                `categories` argument to filter by a single category.
            include_disabled (bool): If True, return plugins even if their
                `enabled` status is False. Default `False`
        Returns:
            PluginManager

            A new `PluginManager` object containing only plugins matching the
            given categories. If the `PluginManager` finds no matches, an empty
            `PluginManager` will be returned.
        """
        if isinstance(categories, str):
            categories = [categories]
        matched = [
            plugin
            for plugin in (self._plugins_by_category.get(c, []) for c in categories)
            if plugin
        ]
        try:
            first, *rest = matched
            unique_list = set(first).intersection(*rest)
            filtered = [
                plugin for plugin in unique_list if plugin.enabled or include_disabled
            ]
            return PluginManager(self._order_by_dependency(filtered))
        except ValueError:
            # not enough values to unpack (`matched` is an empty list)
            return PluginManager()

    def filter_by_name(self, plugin_name: str) -> PluginManager:
        """
        Filter plugins using a period-separated import/module heirarchy.

        This is similar to how Python's [logging
        module](https://docs.python.org/3/library/logging.html#logger-objects)
        works. Given a top level package name, all plugins within that package
        will be returned. Or, given a full path to a plugin, only that plugin
        will be returned in a single item list.

        Args:
            plugin_name (str): A fully namespaced path to the top level of
                plugins you want to filter
        Returns:
            PluginManager

            A new `PluginManager` object containing only plugins matching the
            given name. If the `PluginManager` finds no matches, an empty
            `PluginManager` will be returned.
        """
        return PluginManager(self._find_plugins_in_tree(plugin_name, self._plugin_tree))

    def _find_plugins_in_tree(
        self, namespace: str, tree: dict
    ) -> list[PieceMealPlugin]:
        node = tree
        plugins = []
        for nodename in namespace.split("."):
            try:
                node = node[nodename]
            except KeyError:
                return []
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, dict):
                    plugins.extend(self._find_plugins_in_tree(k, node))
                else:
                    plugins.append(node[k])
        else:
            plugins.append(node)
        return plugins

    def get_plugin(self, plugin_name: str) -> PieceMealPlugin:
        """
        Retrieve a single plugin.

        As long as it exists, the plugin will always be returned, even if it is
        disabled. It is the responsibility of the calling code to determine
        whether or not to use the plugin, based on its `enabled` status.

        Args:
            plugin_name (str): The name of the plugin. This can be the value
                returned by `plugin.name`, which is typically the Class name of
                the plugin, or the path as a period-separated heirarchy like
                what is used in `filter_by_name`
        Returns:
            PieceMealPlugin
        Raises:
            NameError: In the case that no plugin can be found by that name.
        """
        try:
            return self._plugins_by_name[plugin_name]
        except KeyError:
            matching_plugins = self._find_plugins_in_tree(
                plugin_name, self._plugin_tree
            )
            if len(matching_plugins) == 0:
                raise NameError(f"No plugins loaded named '{plugin_name}'")
            elif len(matching_plugins) > 1:
                msg = f"Too many matching plugins for name '{plugin_name}'."
                msg += f" Expected 1, found {len(matching_plugins)}."
                raise ValueError(msg)
            else:
                return matching_plugins[0]

    def apply_categories(
        self, categories: str | Sequence[str], to: PieceMealPlugin | None = None
    ) -> None:
        """
        Apply categories to a plugin at runtime.

        In addition to defining categories as part of a plugin class,
        categories can be defined at runtime by calling `apply_categories` on
        a plugin. This allows plugins loaded from one module to belong to one
        category, but another module to belong to another, even if they have
        the same base class.

        As a convenience, `apply_categories` also accepts a single string for
        the `categories` argument, if only one category should be applied.

        Args:
            categories (list,str): A list of category names.

                As a convenience, `apply_categories` also accepts a single
                string for categories, if only one category should be applied.
        Kwargs:
            to (PieceMealPlugin): The plugin to which the categories should be
                applied. The `to=` can be omitted and the plugin supplied
                positionally, but it is mandatory. The `to` keyword argument is
                simply supplied for api clarity.
        Returns:
            None
        Raises:
            TypeError

            In the case that no plugin is supplied either positionally or using
            the keyword argument `to`.
        """
        if to is None:
            raise TypeError("missing required argument: 'to'")
        plugin = to
        if isinstance(categories, str):
            categories = [categories]
        for c in categories:
            if not self._plugins_by_category.get(c, False):
                self._plugins_by_category[c] = []
            self._plugins_by_category[c].append(plugin)

    @property
    def enabled_plugins(self) -> PluginManager:
        """
        Get all plugins whose `enabled` status is True.

        This is something that can easily be done by the code:
        `[p for p in plugins if p.enabled]`

        However using this property has two advantages:

        1. It's a little bit shorter and readable.
        2. It returns a new `PluginManager` instead of a list, so you still
        maintain the power of a `PluginManager` with the results

        Returns:
            PluginManager
        """
        return PluginManager([p for p in self.data if p.enabled])

    @property
    def disabled_plugins(self) -> PluginManager:
        """
        Get all plugins whose `enabled` status is False.

        This is something that can easily be done by the code:
        `[p for p in plugins if not p.enabled]`

        However using this property has two advantages:

        1. It's a little bit shorter and readable.
        2. It returns a new `PluginManager` instead of a list, so you still
        maintain the power of a `PluginManager` with the results

        Returns:
            PluginManager
        """
        return PluginManager([p for p in self.data if not p.enabled])

    @property
    def categories(self) -> list[str]:
        """
        List the categories recognized by the PluginManager

        Returns:
                list

                All categories that have been assigned to plugins, either through
                the `categories` attribute of the plugins themselves, during load
                through the `as_categories` argument, or applied through
                `apply_categories`
        """
        return list(self._plugins_by_category.keys())

    def _load_from_import(
        self, module: ModuleType, as_categories: str | Sequence[str] | None = None
    ) -> list[PieceMealPlugin]:
        # > https://docs.python.org/3/reference/import.html#packages
        # >
        # > It’s important to keep in mind that all packages are modules, but
        # > not all modules are packages. Or put another way, packages are just
        # > a special kind of module. Specifically, any module that contains a
        # > __path__ attribute is considered a package.
        #
        # Because it is explicit, we can rely on testing for a __path__
        # attribute to differentiate the two.
        plugins = []
        if hasattr(module, "__path__"):
            # Packages are denoted by __init__ files, which can contain plugins,
            # so do not skip loading them as a module as well.
            plugins.extend(self._load_from_module(module, as_categories=as_categories))
            prefix = module.__name__ + "."
            for submodule in pkgutil.iter_modules(module.__path__, prefix):
                module_obj = importlib.import_module(submodule.name)
                plugins.extend(
                    self._load_from_import(module_obj, as_categories=as_categories)
                )
        else:
            plugins.extend(self._load_from_module(module, as_categories=as_categories))
        return plugins

    def _should_load(self, obj: object, expected_module: ModuleType) -> bool:
        # Only get classes defined inside the expected module. Imported classes
        # show up in `getmembers` too, but they should not be loaded with the
        # rest. They should be loaded through the module in which they are
        # defined.
        return (
            inspect.isclass(obj)
            and obj.__module__ == expected_module.__name__
            and PieceMealPlugin in inspect.getmro(obj)
        )

    def _load_from_module(
        self, module: ModuleType, as_categories: str | Sequence[str] | None = None
    ) -> list[PieceMealPlugin]:
        """
        Load plugins located within the given module.

        Args:
            module (module): An already imported python module object.
        Kwargs:
            as_categories (list,str): Apply categories to all plugins found in
                the module at load time. `as_categories` can be a single `str`,
                or a list of `str`. See `apply_categories` for more information.
        Returns:
            list

            A list of all plugins loaded during the method's run. All plugins
            are also added to any existing plugins in the original
            PluginManager.
        """
        if not as_categories:
            as_categories = []
        found_plugins = [
            obj()
            for name, obj in inspect.getmembers(module)
            if self._should_load(obj, module)
        ]
        loaded_plugins = []
        for plugin in found_plugins:
            # Have to wait until we have a concrete object to test for base classes
            if not plugin.is_base:
                loaded_plugins.append(plugin)
                self._save_plugin(plugin)
                self.apply_categories(as_categories, plugin)
        return loaded_plugins

    def _find_package_root_for_file(self, pth: Path) -> Path:
        for pardir in pth.parents:
            initfile = pardir / "__init__.py"
            if not initfile.exists():
                return pardir
        return pth

    def _load_from_file(
        self, fp: Path, as_categories: str | Sequence[str] | None = None
    ) -> list[PieceMealPlugin]:
        pkg_root = self._find_package_root_for_file(fp)
        if pkg_root and str(pkg_root) not in sys.path:
            sys.path.append(str(pkg_root))

        module_parents = fp.relative_to(pkg_root).parent.parts
        module_name = fp.stem
        import_string = ".".join([*module_parents, module_name])
        module_obj = importlib.import_module(import_string)
        return self._load_from_module(module_obj, as_categories=as_categories)

    def _load_directory(
        self,
        dirpath: Path,
        recursive: bool = False,
        as_categories: str | Sequence[str] | None = None,
    ) -> list[PieceMealPlugin]:
        module_pattern = "**/*.py" if recursive else "*.py"
        loaded = []
        for fp in dirpath.glob(module_pattern):
            found = self._load_from_file(fp, as_categories=as_categories)
            loaded.extend(found)
        return loaded

    def _collect_inherited_categories(self, plugin: PieceMealPlugin) -> list[str]:
        inherited_categories = []
        ancestors = inspect.getmro(plugin.__class__)
        for plugin_class in ancestors:
            if plugin_class == PieceMealPlugin:
                break
            unique_categories = [
                c
                for c in plugin_class.categories  # type: ignore[attr-defined]
                if c not in inherited_categories
            ]
            inherited_categories.extend(unique_categories)
        return inherited_categories

    def _add_to_tree(self, plugin: PieceMealPlugin, namespace: str) -> None:
        node = self._plugin_tree
        for nodename in namespace.split("."):
            node = node.setdefault(nodename, dict())
        node[type(plugin).__name__] = plugin

    def _order_by_dependency(
        self, plugins: list[PieceMealPlugin]
    ) -> list[PieceMealPlugin]:
        graph: TopologicalSorter = TopologicalSorter()
        for plugin in plugins:
            if plugin.dependencies:
                errors = []
                for dependency in plugin.dependencies:
                    try:
                        graph.add(plugin, self.get_plugin(dependency))
                    except NameError:
                        errors.append(dependency)
                if errors:
                    missing = ", ".join([dependency_name for dependency_name in errors])
                    msg = f"Failed to load plugin: {plugin.name}. "
                    msg += f"Missing {len(errors)} dependencies [{missing}]"
                    raise DependencyError(msg)
            else:
                graph.add(plugin)
        return list(graph.static_order())

    def _save_plugin(self, plugin: PieceMealPlugin) -> None:
        self.data.append(plugin)
        plugin_name = type(plugin).__name__
        namespace = plugin.__module__
        self._add_to_tree(plugin, namespace)
        self._plugins_by_name[plugin_name] = plugin
        for category in self._collect_inherited_categories(plugin):
            self.apply_categories(category, plugin)
