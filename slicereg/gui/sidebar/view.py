from __future__ import annotations

from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLineEdit, QHBoxLayout, QLabel

from slicereg.gui.base import BaseQtWidget
from slicereg.gui.sidebar.model import SidebarViewModel
from slicereg.gui.sidebar.slider_widget import LabelledSliderWidget
from vendor.napari_qrange_slider.qt_range_slider import QHRangeSlider


class SidebarView(BaseQtWidget):

    def __init__(self, _model: SidebarViewModel):

        self._model = _model
        self._model.updated.connect(self.update)

        self.widget = QWidget()

        layout = QVBoxLayout()
        self.widget.setLayout(layout)

        # Load atlas controls
        load_atlas_layout = QHBoxLayout()
        load_atlas_layout.addWidget(QLabel(text='Res (μm):'))

        self.resolution_textbox = QLineEdit()
        load_atlas_layout.addWidget(self.resolution_textbox)
        # self.resolution_textbox.textEdited.connect(self._model.update_resolution_textbox)

        self.load_atlas_from_file_button = QPushButton("Load Atlas File")
        load_atlas_layout.addWidget(self.load_atlas_from_file_button)
        # self.load_atlas_from_file_button.clicked.connect(self.show_load_atlas_dialog)

        layout.addLayout(load_atlas_layout)

        self.update_bgatlas_button = QPushButton("Update Brainglobe Atlases")
        layout.addWidget(self.update_bgatlas_button)
        # self.update_bgatlas_button.clicked.connect(self._model.click_update_bgatlas_list_button)

        self.list_atlas_dropdown = QComboBox()
        layout.addWidget(self.list_atlas_dropdown)
        # self.list_atlas_dropdown.currentTextChanged.connect(self._model.change_bgatlas_selection_dropdown)

        self.load_atlas_button = QPushButton("Load Atlas")
        layout.addWidget(self.load_atlas_button)
        # self.load_atlas_button.clicked.connect(self._model.click_load_bgatlas_button)

        # Load atlas controls
        load_section_layout = QHBoxLayout()
        load_section_layout.addWidget(QLabel(text='Res (μm):'))

        self.section_resolution_textbox = QLineEdit()
        load_section_layout.addWidget(self.section_resolution_textbox)
        # self.section_resolution_textbox.textEdited.connect(self._model.update_section_resolution_textbox)

        # Load Section Buttons
        self.load_image_button = QPushButton("Load Section")
        load_section_layout.addWidget(self.load_image_button)
        # self.load_image_button.clicked.connect(self.show_load_image_dialog)

        layout.addLayout(load_section_layout)

        self.quick_load_section_button = QPushButton("Quick Load Section")
        layout.addWidget(self.quick_load_section_button)
        # self.quick_load_section_button.clicked.connect(self._model.click_quick_load_section_button)

        # Scale Sliders (Set Section Resolution)
        self.resample_widget = LabelledSliderWidget(min=15, max=200, label="Resample")
        layout.addLayout(self.resample_widget.layout)
        # self.resample_widget.connect(self._model.slide_resample_slider)

        self.resolution_widget = LabelledSliderWidget(min=1, max=100, label="Resolution")
        layout.addLayout(self.resolution_widget.layout)
        # self.resolution_widget.connect(self._model.slide_resolution_slider)

        # Movement Sliders
        self.x_slider = LabelledSliderWidget(min=-10000, max=10000, label='x')
        layout.addLayout(self.x_slider.layout)
        # self.x_slider.connect(self._model.change_x_slider)

        self.y_slider = LabelledSliderWidget(min=-10000, max=10000, label='y')
        layout.addLayout(self.y_slider.layout)
        # self.y_slider.connect(self._model.change_y_slider)

        self.z_slider = LabelledSliderWidget(min=-10000, max=10000, label='z')
        layout.addLayout(self.z_slider.layout)
        # self.z_slider.connect(self._model.change_z_slider)

        self.rotx_slider = LabelledSliderWidget(min=-180, max=180, label='rotx')
        layout.addLayout(self.rotx_slider.layout)
        # self.rotx_slider.connect(self._model.change_rotx_slider)

        self.roty_slider = LabelledSliderWidget(min=-180, max=180, label='roty')
        layout.addLayout(self.roty_slider.layout)
        # self.roty_slider.connect(self._model.change_roty_slider)

        self.rotz_slider = LabelledSliderWidget(min=-180, max=180, label='rotz')
        layout.addLayout(self.rotz_slider.layout)
        # self.rotz_slider.connect(self._model.change_rotz_slider)

        # Quick-rotation buttons
        buttons_layout = QHBoxLayout()

        self.coronal_button = QPushButton("Coronal")
        buttons_layout.addWidget(self.coronal_button)
        # self.coronal_button.clicked.connect(self._model.click_coronal_button)

        self.annotation_atlas_button = QPushButton("Sagittal")
        buttons_layout.addWidget(self.annotation_atlas_button)
        # self.annotation_atlas_button.clicked.connect(self._model.click_sagittal_button)

        self.axial_button = QPushButton("Axial")
        buttons_layout.addWidget(self.axial_button)
        # self.axial_button.clicked.connect(self._model.click_axial_button)

        layout.addLayout(buttons_layout)

        # clim sliders
        self.slice_clim_slider = QHRangeSlider(initial_values=(0., 1.), data_range=(0., 1.), step_size=0.01)
        layout.addWidget(self.slice_clim_slider)
        # self.slice_clim_slider.valuesChanged.connect(self._model.move_clim_slice_slider)

        self.volume_slice_clim_slider = QHRangeSlider(initial_values=(0., 1.), data_range=(0., 1.), step_size=0.01)
        layout.addWidget(self.volume_slice_clim_slider)
        # self.volume_slice_clim_slider.valuesChanged.connect(self._model.move_clim_volume_slider)

        # Atlas Type Buttons
        buttons_layout = QHBoxLayout()

        self.registration_atlas_button = QPushButton("Registration")
        buttons_layout.addWidget(self.registration_atlas_button)
        # self.registration_atlas_button.clicked.connect(self._model.click_registration_atlas_selector_button)

        self.annotation_atlas_button = QPushButton("Annotation")
        buttons_layout.addWidget(self.annotation_atlas_button)
        # self.annotation_atlas_button.clicked.connect(self._model.click_annotation_atlas_selector_button)

        layout.addLayout(buttons_layout)

    def show_load_image_dialog(self):
        filename, filetype = QFileDialog.getOpenFileName(
            parent=self.qt_widget,
            caption="Load Image",
            dir="../../../data/RA_10X_scans/MeA",
            filter="OME-TIFF (*.ome.tiff) ;;TIFF (*.tif *.tiff)"
        )
        if not filename:
            return
        self._model.submit_load_section_from_file(filename=filename)

    def show_load_atlas_dialog(self):
        filename, filetype = QFileDialog.getOpenFileName(
            parent=self.qt_widget,
            caption="Load Atlas from File",
            dir="..",
            filter="Image Files (*.tif *.tiff *.nii *.nii.gz)"
        )
        if not filename:
            return
        self._model.submit_load_atlas_from_file(filename=filename)

    @property
    def qt_widget(self) -> QWidget:
        return self.widget

    def update(self, changed: str) -> None:
        print('changed', changed)
        render_funs = {
            'bgatlas_names': self._render_bgatlas_list_dropdown
        }
        render_funs[changed]()

    def _render_bgatlas_list_dropdown(self):
        self.list_atlas_dropdown.clear()
        self.list_atlas_dropdown.addItems(self.bgatlas_names)
