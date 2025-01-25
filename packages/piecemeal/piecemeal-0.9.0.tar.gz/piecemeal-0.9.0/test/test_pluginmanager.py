import sys
import inspect

import pytest

from piecemeal import PluginManager, DependencyError, CyclicalDependencyError
from piecemeal.base import PieceMealPlugin
from test.data import bare_plugins
from test.data import busy_plugins
from test.data import no_plugins
from test.data import inherited_plugins
from test.data import base_import


@pytest.fixture
def add_to_path(request, DATA_DIR):
    """
    Temporarily add a path to syspath.

    The supplied path must be a child of DATA_DIR, and you must only pass the
    relative path portion. Due to pytest magic, `add_to_path` automatically
    prepends the given path with DATA_DIR's value.
    """
    sys.path.append(str(DATA_DIR / request.param))
    yield
    sys.path.pop()


@pytest.fixture
def plugins():
    return PluginManager()


def test_PluginManager_WhenLoadingModule_InitializesPluginObject():
    """
    This should be really obvious, and not an issue. But that wasn't the case
    early on, and I was having a lot of weird subtle errors because it
    turned out that I wasn't instantiating the plugins, so everything I was
    working with was a class instead of an instance.

    Now that it's fixed, I doubt it will regress to be a problem again, but
    better safe than sorry.
    """
    plugins = PluginManager()
    plugins.load_from_import(bare_plugins)
    plugin = plugins[0]
    assert not inspect.isclass(plugin)


class TestTypeTesting:
    """
    A group of tests for testing the type of plugin objects returned.

    Bundled here together to make scope of the `_assert_all_are_plugins` method
    local to only the tests that need it.
    """
    def _assert_all_are_plugins(self, plugin_list):
        for plugin in plugin_list:
            assert PieceMealPlugin in inspect.getmro(plugin.__class__)

    def test_LoadFromImport_GivenModule_LoadsPlugins(self, plugins):
        plugins.load_from_import(bare_plugins)
        assert len(plugins) == 2
        self._assert_all_are_plugins(plugins)

    def test_LoadFromImport_GivenBusyModule_OnlyLoadsPieceMealPluginDescendants(self, plugins):
        """
        Ensure that only plugins are loaded.

        When a module is imported, all imports, classes, and functions are
        available. Make sure that only classes that are defined within the
        module itself and are descended from `PieceMealPlugin` are loaded.
        """
        plugins.load_from_import(busy_plugins)
        assert len(plugins) == 2
        self._assert_all_are_plugins(plugins)

    def test_LoadFromImport_PluginsDecoratedAsBase_DoesNotImportBasePlugins(self, plugins):
        plugins.load_from_import(base_import)
        assert len(plugins) == 3
        self._assert_all_are_plugins(plugins)


def test_LoadFromImport_GivenEmptyModule_ReturnsEmptyList(plugins):
    plugins.load_from_import(no_plugins)
    assert len(plugins) == 0


@pytest.mark.parametrize('add_to_path', ["package_test"], indirect=True)
def test_LoadFromImport_GivenPackageWithSubdirectories_LoadsAllPlugins(plugins, add_to_path):
    # pkg is a test package, imported at runtime and located at
    # <test_root>/data/package_test/pkg
    import pkg  # type: ignore[import]
    plugins.load_from_import(pkg)
    assert len(plugins) == 3


def test_LoadFromPaths_GivenFilePath_LoadsPlugins(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'bare_plugins.py')
    assert len(plugins) == 2


def test_LoadFromPaths_GivenMultipleFiles_LoadsPlugins(plugins, DATA_DIR):
    paths = [DATA_DIR / 'bare_plugins.py', DATA_DIR / 'base_import.py']
    plugins.load_from_paths(paths)
    assert len(plugins) == 5


def test_LoadFromPaths_GivenStringPath_LoadsPlugins(plugins, DATA_DIR):
    plugins.load_from_paths(str(DATA_DIR / 'bare_plugins.py'))
    assert len(plugins) == 2


def test_LoadFromPaths_GivenMultipleStringPath_LoadsPlugins(plugins, DATA_DIR):
    paths = [str(DATA_DIR / 'bare_plugins.py'), str(DATA_DIR / 'base_import.py')]
    plugins.load_from_paths(paths)
    assert len(plugins) == 5


def test_LoadFromPaths_GivenFilePathWithRelativeImports_LoadsPluginsFromFile(plugins, DATA_DIR):
    module_path = DATA_DIR / "relative_import/single_level/plugins.py"
    plugins.load_from_paths(module_path)
    assert len(plugins) == 1


def test_LoadFromPaths_GivenDirectoryWithRelativeImports_LoadsPluginsFromAllFiles(plugins, DATA_DIR):
    module_path = DATA_DIR / "relative_import/single_level"
    plugins.load_from_paths(module_path)
    assert len(plugins) == 2


def test_LoadFromPaths_GivenDeeplyNestedFileWithRelativeImports_LoadsPluginsFromFile(plugins, DATA_DIR):
    module_path = DATA_DIR / "relative_import/with_subdirs/subdir/leaf/plugins.py"
    plugins.load_from_paths(module_path)
    assert len(plugins) == 1


def test_LoadFromPaths_GivenRelativeImportsWithoutInitFile_ThrowsError(plugins, DATA_DIR):
    module_path = DATA_DIR / "relative_import/without_init/plugins.py"
    with pytest.raises(ImportError):
        plugins.load_from_paths(module_path)


def test_LoadFromPaths_GivenDirectoryPath_LoadsAllPluginsInDirectory(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'dir_test')
    assert len(plugins) == 4


def test_LoadFromPaths_GivenNonExistentPath_ThrowsError(plugins, DATA_DIR):
    with pytest.raises(FileNotFoundError):
        plugins.load_from_paths(DATA_DIR / 'no_exist')


def test_LoadFromPaths_DirectoryWithRecursiveTrue_LoadsAllPluginsInDirectory(plugins, DATA_DIR):
    test_dir = DATA_DIR / 'dir_test'
    plugins.load_from_paths(test_dir, recursive=True)
    assert len(plugins) == 6


def test_LoadFromPaths_FileWithRecursiveTrue_IgnoresRecursiveFlag(plugins, DATA_DIR):
    test_path = DATA_DIR / 'bare_plugins.py'
    plugins.load_from_paths(test_path, recursive=True)
    assert len(plugins) == 2


def test_LoadFromPaths_DirectoryWithOverlappingNameAsExistingPackage_ReturnsNoPlugins(plugins, DATA_DIR):
    # It could be common for users with custom plugins to put them in a
    # directory with the same name as the calling application. This would
    # not work, though, as piecemeal builds a package structure for import
    # and you cannot have two packages with the same name. Any attempted
    # imports of plugins from those modules will fail silently.
    test_path = DATA_DIR / "relative_import/duplicate_pkg_name"
    plugins.load_from_paths(test_path)
    assert len(plugins) == 0


# Filtering
###############################################################################

def test_DisabledPlugins_AllDisabled_ReturnsDisabledPlugins(plugins):
    plugins.load_from_import(bare_plugins)
    assert len(plugins) > 0
    for plugin in plugins:
        plugin.disable()
    assert len(plugins.disabled_plugins) == 2


def test_EnabledPlugins_OneDisabled_ReturnsOneLess(plugins):
    plugins.load_from_import(bare_plugins)
    all_count = len(plugins)
    plugins[0].disable()
    assert len(plugins.enabled_plugins) == all_count - 1


def test_GetAll_AllDisabledIncludeDisabledTrue_ReturnsAllPlugins(plugins):
    plugins.load_from_import(bare_plugins)
    all_count = len(plugins)
    for plugin in plugins:
        plugin.disable()
    assert len(plugins) == all_count


def test_FilterByCategories_CategoryDefinedInPlugin_ReturnsFilteredPlugins(plugins):
    plugins.load_from_import(inherited_plugins)
    text_filters = plugins.filter_by_categories('markdown')
    assert len(text_filters) == 2


def test_FilterByCategories_CategoryDefinedInSuperClass_ReturnsAllSubclassPlugins(plugins):
    plugins.load_from_import(inherited_plugins)
    text_filters = plugins.filter_by_categories('text_filter')
    assert len(text_filters) == 3


def test_FilterByCategories_CategoryDoesntExist_ReturnsEmptyList(plugins):
    plugins.load_from_import(inherited_plugins)
    text_filters = plugins.filter_by_categories('non-existent category')
    assert len(text_filters) == 0


def test_FilterByCategories_GivenMultipleCategories_ReturnsFilteredPlugins(plugins):
    plugins.load_from_import(inherited_plugins)
    text_filters = plugins.filter_by_categories(['file_locator', 'markdown'])
    assert len(text_filters) == 1


def test_FilterByCategories_OneCategoryExistsButOneDoesnt_ReturnsFilteredByExisting(plugins):
    plugins.load_from_import(inherited_plugins)
    text_filters = plugins.filter_by_categories(['non-existent category', 'markdown'])
    assert len(text_filters) == 2


def test_FilterByCategories_PluginsAreDisabled_ReturnsEmptyList(plugins):
    plugins.load_from_import(inherited_plugins)
    for plugin in plugins:
        plugin.disable()
    text_filters = plugins.filter_by_categories('text_filter')
    assert len(text_filters) == 0


def test_FilterByCategories_PluginsAreDisabledButIncludeDisabledIsTrue_ReturnsEmptyList(plugins):
    plugins.load_from_import(inherited_plugins)
    for plugin in plugins:
        plugin.disable()
    text_filters = plugins.filter_by_categories('text_filter', include_disabled=True)
    assert len(text_filters) == 3


def test_GetPluginByName_GivenName_ReturnsPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    plugin = plugins.get_plugin('BarePlugin1')
    assert isinstance(plugin, bare_plugins.BarePlugin1)


def test_GetPluginByName_NameDoesntExist_ThrowsError(plugins):
    plugins.load_from_import(bare_plugins)
    with pytest.raises(NameError):
        plugins.get_plugin('BarePluginX')


def test_GetPluginByName_PluginDisabled_ReturnsPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    for plugin in plugins:
        plugin.disable()
    plugin = plugins.get_plugin('BarePlugin1')
    assert isinstance(plugin, bare_plugins.BarePlugin1)


def test_GetPluginByName_NamespacedName_ReturnsPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    for plugin in plugins:
        plugin.disable()
    plugin = plugins.get_plugin('test.data.bare_plugins.BarePlugin1')
    assert isinstance(plugin, bare_plugins.BarePlugin1)


def test_GetPluginByName_NamespacedNameWithMultipleMatches_ThrowsError(plugins):
    plugins.load_from_import(bare_plugins)
    for plugin in plugins:
        plugin.disable()
    with pytest.raises(ValueError):
        plugins.get_plugin('test.data.bare_plugins')


def test_FilterByName_GivenFullyQualifiedName_ReturnsSinglePlugin(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / "package_test", recursive=True)
    filtered = plugins.filter_by_name("pkg.subdir.base.ConcretePlugin2")
    assert len(filtered) == 1


def test_FilterByName_GivenModuleWithSinglePlugin_ReturnsSinglePlugin(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / "package_test", recursive=True)
    filtered = plugins.filter_by_name("pkg.subdir.base")
    assert len(filtered) == 1


def test_FilterByName_GivenPackageWithMultiplePlugins_ReturnsAllPlugins(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / "package_test", recursive=True)
    filtered = plugins.filter_by_name("pkg")
    assert len(filtered) == 3


# Categories
###############################################################################

def test_GetCategories_NoCategories_ReturnsEmptyList(plugins):
    categories = plugins.categories
    assert len(categories) == 0


def test_GetCategories_CategoryDefinedAtLoad_ReturnsCategories(plugins):
    plugins.load_from_import(bare_plugins, as_categories='bare')
    categories = plugins.categories
    assert len(categories) == 1


def test_GetCategories_CategoriesDefinedInClass_ReturnsCategories(plugins):
    plugins.load_from_import(inherited_plugins)
    categories = plugins.categories
    assert len(categories) == 3


def test_ApplyCategory_ArbitraryCategory_AppliesCategoryToPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    plugin = plugins[0]
    plugins.apply_categories('category_name', plugin)
    assert len(plugins.filter_by_categories('category_name')) == 1


def test_ApplyCategory_UsingToKwarg_AppliesCategoryToPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    plugin = plugins[0]
    plugins.apply_categories('category_name', to=plugin)
    assert len(plugins.filter_by_categories('category_name')) == 1


def test_ApplyCategory_CalledWithOnlyPositionalArguments_AppliesCategoryToPlugin(plugins):
    plugins.load_from_import(bare_plugins)
    plugin = plugins[0]
    plugins.apply_categories('category_name', plugin)
    assert len(plugins.filter_by_categories('category_name')) == 1


def test_ApplyCategory_GivingNoPlugin_ThrowsError(plugins):
    plugins.load_from_import(bare_plugins)
    with pytest.raises(TypeError):
        plugins.apply_categories('category_name')


def test_LoadFromImport_ApplyingSingleCategoryToSingleModule_AppliesCategory(plugins):
    plugins.load_from_import(bare_plugins, as_categories='no-inheritance')
    plugins.load_from_import(inherited_plugins)
    plugins = plugins.filter_by_categories('no-inheritance')
    assert len(plugins) == 2


def test_LoadFromImport_ApplyingListOfCategoriesToSingleModule_AppliesCategories(plugins):
    plugins.load_from_import(bare_plugins, as_categories=['no-inheritance', 'versatile'])
    plugins.load_from_import(inherited_plugins)
    non_inheritance_plugins = plugins.filter_by_categories('no-inheritance')
    versatile_plugins = plugins.filter_by_categories('versatile')
    assert len(non_inheritance_plugins) == 2
    assert non_inheritance_plugins == versatile_plugins


def test_LoadFromPaths_ApplyingSingleCategoryToSingleModule_AppliesCategory(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'bare_plugins.py', as_categories='no-inheritance')
    plugins.load_from_paths(DATA_DIR / 'inherited_plugins.py')
    plugins = plugins.filter_by_categories('no-inheritance')
    assert len(plugins) == 2


def test_LoadFromPaths_ApplyingListOfCategoriesToSingleModule_AppliesCategory(plugins, DATA_DIR):
    bare_path = DATA_DIR / 'bare_plugins.py'
    inherited_path = DATA_DIR / 'inherited_plugins.py'
    plugins.load_from_paths(bare_path, as_categories=['no-inheritance', 'versatile'])
    plugins.load_from_paths(inherited_path)
    plugins = plugins.filter_by_categories('no-inheritance')
    assert len(plugins) == 2


# Dependency Resolution
###############################################################################

# Because order is not guaranteed, it is a good idea to run ordering tests
# multiple times. The order can change on subsequent runs, and with such a
# small test sample size, running multiple times better guarantees the expected
# behavior.
def test_LoadFromPaths_PluginWithDependencyLoadedAfterDependency_ComesAfterDependencyInList(plugins, DATA_DIR):
    for _ in range(5):
        plugins.load_from_paths(DATA_DIR / "dependencies/dependency.py")
        plugins.load_from_paths(DATA_DIR / "dependencies/dependent.py")
        plugins.resolve_dependencies()
        assert plugins[0].name == "DependencyPlugin"
        assert plugins[1].name == "DependentPlugin"
        plugins.clear()  # reset for next iteration


def test_LoadFromPaths_PluginWithDependencyLoadedBeforeDependency_ComesAfterDependencyInList(plugins, DATA_DIR):
    for _ in range(5):
        plugins.load_from_paths(DATA_DIR / "dependencies/dependent.py")
        plugins.load_from_paths(DATA_DIR / "dependencies/dependency.py")
        plugins.resolve_dependencies()
        assert plugins[0].name == "DependencyPlugin"
        assert plugins[1].name == "DependentPlugin"
        plugins.clear()  # reset for next iteration


def test_LoadFromPaths_CategorizedPluginWithDependencyLoadedBeforeDependency_ComesAfterDependencyInCategoryList(plugins, DATA_DIR):
    for _ in range(5):
        plugins.load_from_paths(DATA_DIR / "dependencies/dependent.py", as_categories="dependency_test")
        plugins.load_from_paths(DATA_DIR / "dependencies/dependency.py", as_categories="dependency_test")
        plugins.resolve_dependencies()
        print()
        print(plugins._plugins_by_category)
        categorized_plugins = plugins.filter_by_categories("dependency_test")
        print(categorized_plugins._plugins_by_category)
        assert categorized_plugins[0].name == "DependencyPlugin"
        assert categorized_plugins[1].name == "DependentPlugin"
        plugins.clear()  # reset for next iteration


def test_LoadFromPaths_PluginWithDependencyMissingDependency_ThrowsError(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / "dependencies/missing_dependency.py")
    with pytest.raises(DependencyError):
        plugins.resolve_dependencies()


def test_LoadFromPaths_CyclicalDependencies_ThrowsError(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / "dependencies/cyclical.py")
    with pytest.raises(CyclicalDependencyError):
        plugins.resolve_dependencies()


# List-like behavior
###############################################################################

def test_PluginManager_Len_CountsLoadedPlugins(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'bare_plugins.py')
    assert isinstance(plugins, PluginManager)
    assert len(plugins) == 2


def test_PluginManager_ForLoop_RepeatsInPlugins(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'bare_plugins.py')
    for i, _ in enumerate(plugins):
        pass
    assert i == 1  # zero indexing means i == len(ls) - 1


def test_PluginManager_WhenFiltering_ReturnsNewPluginManager(plugins, DATA_DIR):
    plugins.load_from_paths(DATA_DIR / 'inherited_plugins.py')
    filtered = plugins.filter_by_categories("text_filter")
    assert len(filtered) == 3
    assert isinstance(filtered, PluginManager)
