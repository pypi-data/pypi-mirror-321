import pytest
from pathmonkey.pathmonkey import PathMonkey
from pathlib import Path, PureWindowsPath


def test_construct_path():
    # Basic path construction tests
    assert str(PathMonkey.construct_path(['~', 'projects', 'example'])) == str(Path.home() / "projects" / "example")
    assert str(PathMonkey.construct_path(['/', 'usr', 'bin'])) == "/usr/bin"
    assert str(PathMonkey.construct_path(['', 'usr', 'bin'])) == "/usr/bin"
    assert str(PathMonkey.construct_path(['C:', 'Users', 'example'])) == "C:\\Users\\example"
    assert str(PathMonkey.construct_path(['..', 'another_folder'])) == "../another_folder"
    assert str(PathMonkey.construct_path([])) == "."

    # Extra test cases
    assert str(PathMonkey.construct_path(['usr', 'bin', ''])) == "usr/bin"
    assert str(PathMonkey.construct_path(['usr\\bin'])) == "usr\\bin"
    assert str(PathMonkey.construct_path(['~', '.hidden', 'file'])) == str(Path.home() / ".hidden" / "file")
    assert str(PathMonkey.construct_path(['..', ''])) == ".."
    assert str(PathMonkey.construct_path(['/usr/bin/'])) == "/usr/bin"
    assert str(PathMonkey.construct_path(['C:'])) == "C:"
    assert str(PathMonkey.construct_path(['C:', 'Windows', 'System32'])) == "C:\\Windows\\System32"
    assert str(PathMonkey.construct_path(['C:', 'Program Files', 'MyApp'])) == "C:\\Program Files\\MyApp"
    assert str(PathMonkey.construct_path(['C:', 'Users', 'John', 'Documents'])) == "C:\\Users\\John\\Documents"
    assert str(PathMonkey.construct_path(['~', '..', 'projects'])) == str(Path.home().joinpath("..", "projects"))
    assert str(PathMonkey.construct_path(['.', 'relative_folder'])) == "relative_folder"


def test_deconstruct_path():
    # Basic deconstruction tests
    assert PathMonkey.deconstruct_path(Path.home().joinpath("projects", "example")) == ['', 'home', 'ubuntu', 'projects', 'example']
    assert PathMonkey.deconstruct_path(Path('/usr/bin')) == ['', 'usr', 'bin']
    assert PathMonkey.deconstruct_path(Path('usr/bin')) == ['usr', 'bin']
    assert PathMonkey.deconstruct_path(PureWindowsPath('C:\\Users\\example')) == ['C:', 'Users', 'example']
    assert PathMonkey.deconstruct_path(Path('../another_folder')) == ['..', 'another_folder']
    assert PathMonkey.deconstruct_path(Path.home()) == ['', 'home', 'ubuntu']
    assert PathMonkey.deconstruct_path(Path('/home/ubuntu/myrepos')) == ['', 'home', 'ubuntu', 'myrepos']

    # Extra test cases
    assert PathMonkey.deconstruct_path(Path('usr/bin/')) == ['usr', 'bin']
    assert PathMonkey.deconstruct_path(Path('usr\\bin')) == ['usr\\bin']
    assert PathMonkey.deconstruct_path(Path.home().joinpath('.hidden', 'file')) == ['', 'home', 'ubuntu', '.hidden', 'file']
    assert PathMonkey.deconstruct_path(Path('../')) == ['..']
    assert PathMonkey.deconstruct_path(Path()) == []
    assert PathMonkey.deconstruct_path(Path('/usr/bin/')) == ['', 'usr', 'bin']
    assert PathMonkey.deconstruct_path(Path.home().joinpath('..', 'projects')) == ['', 'home', 'ubuntu', '..', 'projects']
    assert PathMonkey.deconstruct_path(Path('.').joinpath('relative_folder')) == ['relative_folder']

