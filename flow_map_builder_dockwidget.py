# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FlowMapBuilderDockWidget
                                 A QGIS plugin
 This plugin builds flow maps
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-23
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Gleb Pinigin
        email                : pinigin1514@live.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

from qgis.utils import iface

from .fm_template_models import SpiralTreeContext

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'flow_map_builder_dockwidget_base.ui'))


class FlowMapBuilderDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(FlowMapBuilderDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.add_tree.clicked.connect(self.addTree)
        self.contexts = []


    def editingFinished(self, text):
        self.path = text

    def addTree(self):
        dlg = AddDialogWidget(dock=self)
        if dlg.exec():
            self.tab_widget.setEnabled(True)
            self.currentContext = SpiralTreeContext(namestring=dlg.namestring)
            self.contexts.append(self.currentContext)
            self.context_hub.addItem(str(self.currentContext))
        else:
            pass
    
    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

FORM_CLASS2, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'flow_map_builder_dockwidget_base.ui'))

class AddDialogWidget(QtWidgets.QDialog, FORM_CLASS2):

    def __init__(self, parent=None, dock=None):
        super(AddDialogWidget, self).__init__(parent)
        self.dock = dock
        self.setupUi(self)
        self.name_area.textChanged[str].connect(self.setName)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    
    def setName(self, name):
        self.namestring=name