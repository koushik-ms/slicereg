from unittest.mock import Mock

import pytest
from numpy import random
from pytest_bdd import scenario, given, when, then

from slicereg.commands.load_atlas import LoadBrainglobeAtlasCommand
from slicereg.commands.utils import Signal
from slicereg.io.bg_atlasapi import BrainglobeAtlasReader
from slicereg.models.atlas import Atlas
from slicereg.repos.atlas_repo import AtlasRepo


@pytest.fixture
def command():
    repo = Mock(AtlasRepo)
    reader = Mock(BrainglobeAtlasReader)
    reader.list_available.return_value = ['allen_mouse_25um']
    reader.read.return_value = Atlas(volume=random.normal(size=(4, 4, 4)), resolution_um=25)
    return LoadBrainglobeAtlasCommand(_repo=repo, _reader=reader, atlas_updated=Mock(Signal))


@scenario("load_atlas.feature", "Load Atlas")
def test_outlined():
    ...


@given("the 25um atlas is already on my computer")
def check_atlas_exists(command):
    # Already set.
    pass


@when("I ask for a 25um atlas")
def load_atlas(command):
    command(bgatlas_name="allen_mouse_25um")


@then("a 3D volume of the 25um allen reference atlas appears onscreen.")
def check_3d_atlas_data_shown(command):
    output = command.atlas_updated.emit.call_args[1]
    assert output['volume'].ndim == 3
    assert output['transform'].shape == (4, 4)
    command._reader.read.assert_called_with(path="allen_mouse_25um")


@then("it is set as the current atlas for the session.")
def check_atlas_set_in_repo(command):
    assert command._repo.set_atlas.call_count == 1