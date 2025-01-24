from minecraft_data import __version__


def test_version():
    cleaned_version = __version__.split("rc")[0]
    assert cleaned_version == "3.83.1"
