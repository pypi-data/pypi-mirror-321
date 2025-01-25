from piecemeal.base import PieceMealPlugin


class MyPlugin(PieceMealPlugin):
    pass


def test_Plugin_HasNameProperty():
    plugin = MyPlugin()
    assert plugin.name == "MyPlugin"
