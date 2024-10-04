# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(853, 700)
        self.lineEditNb1 = QLineEdit(Form)
        self.lineEditNb1.setObjectName(u"lineEditNb1")
        self.lineEditNb1.setGeometry(QRect(270, 110, 113, 22))
        self.lineEditNb2 = QLineEdit(Form)
        self.lineEditNb2.setObjectName(u"lineEditNb2")
        self.lineEditNb2.setGeometry(QRect(270, 160, 113, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 120, 49, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 160, 49, 16))
        self.btnAddition = QPushButton(Form)
        self.btnAddition.setObjectName(u"btnAddition")
        self.btnAddition.setGeometry(QRect(290, 210, 75, 24))
        self.lblAddition = QLabel(Form)
        self.lblAddition.setObjectName(u"lblAddition")
        self.lblAddition.setGeometry(QRect(300, 280, 49, 16))
        self.champTexte = QPlainTextEdit(Form)
        self.champTexte.setObjectName(u"champTexte")
        self.champTexte.setGeometry(QRect(210, 360, 441, 181))
        self.btnLectureFichier = QPushButton(Form)
        self.btnLectureFichier.setObjectName(u"btnLectureFichier")
        self.btnLectureFichier.setGeometry(QRect(240, 570, 181, 24))
        self.btnEcritureFichier = QPushButton(Form)
        self.btnEcritureFichier.setObjectName(u"btnEcritureFichier")
        self.btnEcritureFichier.setGeometry(QRect(450, 570, 181, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre1:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre2:", None))
        self.btnAddition.setText(QCoreApplication.translate("Form", u"Additioner", None))
        self.lblAddition.setText("")
        self.btnLectureFichier.setText(QCoreApplication.translate("Form", u"Lecture fichier", None))
        self.btnEcritureFichier.setText(QCoreApplication.translate("Form", u"Ecriture Fichier", None))
    # retranslateUi

