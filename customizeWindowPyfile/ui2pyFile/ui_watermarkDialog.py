# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watermarkDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WatermarkDialog(object):
    def setupUi(self, WatermarkDialog):
        WatermarkDialog.setObjectName("WatermarkDialog")
        WatermarkDialog.resize(290, 235)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/watermark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WatermarkDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WatermarkDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(WatermarkDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.watermarkWord = QtWidgets.QLineEdit(WatermarkDialog)
        self.watermarkWord.setObjectName("watermarkWord")
        self.horizontalLayout_3.addWidget(self.watermarkWord)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(WatermarkDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.alpha = QtWidgets.QLineEdit(WatermarkDialog)
        self.alpha.setObjectName("alpha")
        self.horizontalLayout.addWidget(self.alpha)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(WatermarkDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.ankle = QtWidgets.QLineEdit(WatermarkDialog)
        self.ankle.setObjectName("ankle")
        self.horizontalLayout_5.addWidget(self.ankle)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(WatermarkDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.colorComboBox = QtWidgets.QComboBox(WatermarkDialog)
        self.colorComboBox.setObjectName("colorComboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resource/picture/红色.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorComboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resource/picture/蓝色.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorComboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resource/picture/绿色.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorComboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./resource/picture/灰色.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorComboBox.addItem(icon4, "")
        self.horizontalLayout_2.addWidget(self.colorComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.confirmButton = QtWidgets.QPushButton(WatermarkDialog)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_4.addWidget(self.confirmButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.cancleButton = QtWidgets.QPushButton(WatermarkDialog)
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout_4.addWidget(self.cancleButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(WatermarkDialog)
        QtCore.QMetaObject.connectSlotsByName(WatermarkDialog)

    def retranslateUi(self, WatermarkDialog):
        _translate = QtCore.QCoreApplication.translate
        WatermarkDialog.setWindowTitle(_translate("WatermarkDialog", "请输入水印内容"))
        self.label.setText(_translate("WatermarkDialog", "水印内容："))
        self.label_3.setText(_translate("WatermarkDialog", "透明度："))
        self.alpha.setText(_translate("WatermarkDialog", "0.5"))
        self.label_4.setText(_translate("WatermarkDialog", "倾斜角度："))
        self.ankle.setText(_translate("WatermarkDialog", "20"))
        self.label_2.setText(_translate("WatermarkDialog", "颜色："))
        self.colorComboBox.setItemText(0, _translate("WatermarkDialog", "红色"))
        self.colorComboBox.setItemText(1, _translate("WatermarkDialog", "蓝色"))
        self.colorComboBox.setItemText(2, _translate("WatermarkDialog", "绿色"))
        self.colorComboBox.setItemText(3, _translate("WatermarkDialog", "灰色"))
        self.confirmButton.setText(_translate("WatermarkDialog", "确定"))
        self.cancleButton.setText(_translate("WatermarkDialog", "取消"))
