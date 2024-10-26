# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_chat.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Ui(object):
    def setupUi(self, Ui):
        if not Ui.objectName():
            Ui.setObjectName(u"Ui")
        Ui.resize(1070, 540)
        Ui.setAutoFillBackground(False)
        self.textEdit = QTextEdit(Ui)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 831, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setReadOnly(True)
        self.plainTextEdit = QPlainTextEdit(Ui)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 360, 831, 141))
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.tableWidget = QTableWidget(Ui)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(855, 10, 211, 491))
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.layoutWidget = QWidget(Ui)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(690, 500, 151, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ClearButton = QPushButton(self.layoutWidget)
        self.ClearButton.setObjectName(u"ClearButton")

        self.horizontalLayout.addWidget(self.ClearButton)

        self.SendButton = QPushButton(self.layoutWidget)
        self.SendButton.setObjectName(u"SendButton")

        self.horizontalLayout.addWidget(self.SendButton)

        self.line = QFrame(Ui)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 336, 841, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Ui)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(840, 10, 20, 491))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Ui)

        QMetaObject.connectSlotsByName(Ui)
    # setupUi

    def retranslateUi(self, Ui):
        Ui.setWindowTitle(QCoreApplication.translate("Ui", u"Form", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Ui", u"\u6587\u672c\u8f93\u5165\u6846", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ui", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ui", u"IP", None));
        self.ClearButton.setText(QCoreApplication.translate("Ui", u"\u6e05\u7a7a", None))
        self.SendButton.setText(QCoreApplication.translate("Ui", u"\u53d1\u9001", None))
    # retranslateUi

