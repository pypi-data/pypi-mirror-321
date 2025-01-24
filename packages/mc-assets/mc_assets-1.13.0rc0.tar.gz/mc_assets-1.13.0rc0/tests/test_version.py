from minecraft_assets import __version__


def test_version():
    cleaned_version = __version__.split("rc")[0]
    assert cleaned_version == "1.13.0"
