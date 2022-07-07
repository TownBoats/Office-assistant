# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passworddialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_passwordDialog(object):
    def setupUi(self, passwordDialog):
        passwordDialog.setObjectName("passwordDialog")
        passwordDialog.resize(609, 104)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        passwordDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(passwordDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(passwordDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.password = QtWidgets.QLineEdit(passwordDialog)
        self.password.setObjectName("password")
        self.horizontalLayout.addWidget(self.password)
        self.confirmButton = QtWidgets.QPushButton(passwordDialog)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.cancleButton = QtWidgets.QPushButton(passwordDialog)
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout.addWidget(self.cancleButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(passwordDialog)
        self.cancleButton.clicked.connect(passwordDialog.close) # type: ignore
        self.confirmButton.clicked.connect(passwordDialog.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(passwordDialog)

    def retranslateUi(self, passwordDialog):
        _translate = QtCore.QCoreApplication.translate
        passwordDialog.setWindowTitle(_translate("passwordDialog", "请输入密码"))
        self.label.setText(_translate("passwordDialog", "请输入密码"))
        self.confirmButton.setText(_translate("passwordDialog", "确定"))
        self.cancleButton.setText(_translate("passwordDialog", "取消"))
