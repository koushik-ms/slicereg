from unittest.mock import Mock

import pytest
import numpy as np
import numpy.testing as npt

from slicereg.commands.utils import Signal
from slicereg.gui.app_model import AppModel
from slicereg.gui.commands import CommandProvider
from slicereg.gui.view_models.atlas_section import AtlasSectionViewModel


@pytest.fixture
def view_model() -> AtlasSectionViewModel:
    MockCommandProvider = Mock(CommandProvider)
    MockSignal = Mock(Signal)
    model = AppModel(MockCommandProvider())
    updated = MockSignal()
    view_model = AtlasSectionViewModel(axis=0, _model=model, updated=updated)
    return view_model


def test_update_atlas_volume(view_model: AtlasSectionViewModel):
    app_model = view_model._model
    app_model.atlas_volume = np.random.randint(0, 100, (10, 10, 10), np.uint16)
    expected = view_model._model.atlas_volume[app_model.atlas_section_coords[0], :, :]

    args, kwargs = view_model.updated.emit.call_args
    result = kwargs['dto'].section_image
    npt.assert_equal(result, expected)


def test_update_atlas_volume_axis_2():
    MockCommandProvider = Mock(CommandProvider)
    MockSignal = Mock(Signal)
    model = AppModel(MockCommandProvider())
    updated = MockSignal()
    view_model = AtlasSectionViewModel(axis=2, _model=model, updated=updated)

    model.atlas_volume = np.random.randint(0, 100, (10, 10, 10), np.uint16)
    expected = view_model._model.atlas_volume[:, :, model.atlas_section_coords[0]]

    args, kwargs = view_model.updated.emit.call_args
    result = kwargs['dto'].section_image
    npt.assert_equal(result, expected)


def test_update_coords(view_model: AtlasSectionViewModel):
    app_model = view_model._model
    app_model.atlas_volume = np.random.randint(0, 100, (10, 10, 10), np.uint16)
    app_model.atlas_section_coords = (1, 2, 3)
    expected = (2, 3)

    args, kwargs = view_model.updated.emit.call_args
    result = kwargs['dto'].coords
    npt.assert_equal(result, expected)