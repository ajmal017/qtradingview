# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dock_alarms.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockAlarms(object):
    def setupUi(self, DockAlarms):
        DockAlarms.setObjectName("DockAlarms")
        DockAlarms.resize(421, 300)
        DockAlarms.setToolTip("")
        DockAlarms.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        DockAlarms.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabla_alarms = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tabla_alarms.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla_alarms.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_alarms.setProperty("showDropIndicator", False)
        self.tabla_alarms.setDragDropOverwriteMode(False)
        self.tabla_alarms.setAlternatingRowColors(True)
        self.tabla_alarms.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabla_alarms.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_alarms.setObjectName("tabla_alarms")
        self.tabla_alarms.setColumnCount(5)
        self.tabla_alarms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_alarms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_alarms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_alarms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_alarms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_alarms.setHorizontalHeaderItem(4, item)
        self.tabla_alarms.horizontalHeader().setSortIndicatorShown(True)
        self.tabla_alarms.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tabla_alarms)
        self.btn_delete = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout.addWidget(self.btn_delete)
        DockAlarms.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockAlarms)
        QtCore.QMetaObject.connectSlotsByName(DockAlarms)

    def retranslateUi(self, DockAlarms):
        _translate = QtCore.QCoreApplication.translate
        DockAlarms.setWindowTitle(_translate("DockAlarms", "A&larmas"))
        item = self.tabla_alarms.horizontalHeaderItem(0)
        item.setText(_translate("DockAlarms", "ID"))
        item = self.tabla_alarms.horizontalHeaderItem(1)
        item.setText(_translate("DockAlarms", "Mercado"))
        item = self.tabla_alarms.horizontalHeaderItem(2)
        item.setText(_translate("DockAlarms", "Exchange"))
        item = self.tabla_alarms.horizontalHeaderItem(3)
        item.setText(_translate("DockAlarms", "Condicion"))
        item = self.tabla_alarms.horizontalHeaderItem(4)
        item.setText(_translate("DockAlarms", "Precio"))
        self.btn_delete.setText(_translate("DockAlarms", "Eliminar alarma"))
