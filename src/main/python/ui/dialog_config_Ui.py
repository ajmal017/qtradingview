# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogConfig(object):
    def setupUi(self, DialogConfig):
        DialogConfig.setObjectName("DialogConfig")
        DialogConfig.setWindowModality(QtCore.Qt.WindowModal)
        DialogConfig.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogConfig.sizePolicy().hasHeightForWidth())
        DialogConfig.setSizePolicy(sizePolicy)
        DialogConfig.setMinimumSize(QtCore.QSize(400, 300))
        DialogConfig.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogConfig.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DialogConfig)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.layoutWidget = QtWidgets.QWidget(self.tab_general)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 71))
        self.layoutWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.combo_languages = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_languages.sizePolicy().hasHeightForWidth())
        self.combo_languages.setSizePolicy(sizePolicy)
        self.combo_languages.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_languages.setObjectName("combo_languages")
        self.combo_languages.addItem("")
        self.combo_languages.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_languages)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_exchanges = QtWidgets.QWidget()
        self.tab_exchanges.setObjectName("tab_exchanges")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_exchanges)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 371, 151))
        self.verticalLayoutWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.list_exchanges = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_exchanges.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.list_exchanges.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_exchanges.setAlternatingRowColors(True)
        self.list_exchanges.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_exchanges.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.list_exchanges.setObjectName("list_exchanges")
        self.verticalLayout_2.addWidget(self.list_exchanges)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_exchanges)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.horizontalLayoutWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.combo_initial_exchange = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_initial_exchange.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_initial_exchange.setObjectName("combo_initial_exchange")
        self.horizontalLayout.addWidget(self.combo_initial_exchange)
        self.combo_initial_market = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_initial_market.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_initial_market.setObjectName("combo_initial_market")
        self.horizontalLayout.addWidget(self.combo_initial_market)
        self.tabWidget.addTab(self.tab_exchanges, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogConfig)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogConfig)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(DialogConfig.accept)
        self.buttonBox.rejected.connect(DialogConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogConfig)

    def retranslateUi(self, DialogConfig):
        _translate = QtCore.QCoreApplication.translate
        DialogConfig.setWindowTitle(_translate("DialogConfig", "Settings"))
        self.label.setText(_translate("DialogConfig", "Language:"))
        self.combo_languages.setItemText(0, _translate("DialogConfig", "es_ES"))
        self.combo_languages.setItemText(1, _translate("DialogConfig", "en_EN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("DialogConfig", "General"))
        self.label_3.setText(_translate("DialogConfig", "Active exchanges:"))
        self.label_2.setText(_translate("DialogConfig", "Load on boot:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exchanges), _translate("DialogConfig", "Exchanges"))
import iconos_rc
