# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mostrar_reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

from ..imagenes import imagenes_rc

class Ui_JTA_MostrarReservas(object):
    def setupUi(self, JTA_MostrarReservas):
        if not JTA_MostrarReservas.objectName():
            JTA_MostrarReservas.setObjectName(u"JTA_MostrarReservas")
        JTA_MostrarReservas.resize(1063, 766)
        JTA_MostrarReservas.setMinimumSize(QSize(1063, 766))
        JTA_MostrarReservas.setMaximumSize(QSize(1063, 766))
        icon = QIcon()
        icon.addFile(u":/imagenes/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        JTA_MostrarReservas.setWindowIcon(icon)
        self.JTA_centralwidget = QWidget(JTA_MostrarReservas)
        self.JTA_centralwidget.setObjectName(u"JTA_centralwidget")
        self.JTA_centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #f0dfc7;\n"
"}")
        self.JTA_pushButton_res = QPushButton(self.JTA_centralwidget)
        self.JTA_pushButton_res.setObjectName(u"JTA_pushButton_res")
        self.JTA_pushButton_res.setGeometry(QRect(800, 680, 231, 61))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(16)
        font.setBold(True)
        self.JTA_pushButton_res.setFont(font)
        self.JTA_pushButton_res.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #78ac75;\n"
"    border-radius: 25px;\n"
"    background-color: #9fd079;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a4c59d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #597354;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #7a8c68;\n"
"    color: #cccccc; \n"
"    border: 2px solid #667556; \n"
"}")
        self.JTA_tableWidget_res = QTableWidget(self.JTA_centralwidget)
        self.JTA_tableWidget_res.setObjectName(u"JTA_tableWidget_res")
        self.JTA_tableWidget_res.setGeometry(QRect(390, 120, 641, 531))
        self.JTA_tableWidget_res.setMaximumSize(QSize(641, 531))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.JTA_tableWidget_res.setFont(font1)
        self.JTA_tableWidget_res.setStyleSheet(u"border: 2px solid #78ac75;\n"
"background-color: #fefffd;")
        self.JTA_tableWidget_res.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.JTA_tableWidget_res.setAutoScroll(True)
        self.JTA_tableWidget_res.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.JTA_tableWidget_res.horizontalHeader().setVisible(False)
        self.JTA_tableWidget_res.verticalHeader().setVisible(False)
        self.JTA_listWidget_salones = QListWidget(self.JTA_centralwidget)
        self.JTA_listWidget_salones.setObjectName(u"JTA_listWidget_salones")
        self.JTA_listWidget_salones.setGeometry(QRect(30, 120, 341, 531))
        self.JTA_listWidget_salones.setFont(font1)
        self.JTA_listWidget_salones.setStyleSheet(u"border: 2px solid #78ac75;\n"
"background-color: #fefffd;\n"
"")
        self.JTA_pushButton_refr = QPushButton(self.JTA_centralwidget)
        self.JTA_pushButton_refr.setObjectName(u"JTA_pushButton_refr")
        self.JTA_pushButton_refr.setGeometry(QRect(950, 20, 71, 71))
        font2 = QFont()
        font2.setPointSize(12)
        self.JTA_pushButton_refr.setFont(font2)
        self.JTA_pushButton_refr.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/imagenes/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.JTA_pushButton_refr.setIcon(icon1)
        self.JTA_pushButton_refr.setIconSize(QSize(40, 40))
        self.JTA_label_1 = QLabel(self.JTA_centralwidget)
        self.JTA_label_1.setObjectName(u"JTA_label_1")
        self.JTA_label_1.setGeometry(QRect(300, -10, 511, 101))
        font3 = QFont()
        font3.setFamilies([u"Lucida Calligraphy"])
        font3.setPointSize(28)
        font3.setItalic(True)
        self.JTA_label_1.setFont(font3)
        self.JTA_label_1.setStyleSheet(u"")
        self.JTA_label_1.setScaledContents(False)
        self.JTA_label_2 = QLabel(self.JTA_centralwidget)
        self.JTA_label_2.setObjectName(u"JTA_label_2")
        self.JTA_label_2.setGeometry(QRect(30, 100, 171, 16))
        font4 = QFont()
        font4.setFamilies([u"Sitka"])
        font4.setPointSize(12)
        self.JTA_label_2.setFont(font4)
        self.JTA_label_3 = QLabel(self.JTA_centralwidget)
        self.JTA_label_3.setObjectName(u"JTA_label_3")
        self.JTA_label_3.setGeometry(QRect(390, 100, 181, 16))
        self.JTA_label_3.setFont(font4)
        JTA_MostrarReservas.setCentralWidget(self.JTA_centralwidget)

        self.retranslateUi(JTA_MostrarReservas)

        QMetaObject.connectSlotsByName(JTA_MostrarReservas)
    # setupUi

    def retranslateUi(self, JTA_MostrarReservas):
        JTA_MostrarReservas.setWindowTitle(QCoreApplication.translate("JTA_MostrarReservas", u"Gesti\u00f3n Hotelera - Hotel Brianda", None))
#if QT_CONFIG(tooltip)
        self.JTA_pushButton_res.setToolTip(QCoreApplication.translate("JTA_MostrarReservas", u"<html><head/><body><p>Crear o modificar reserva</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.JTA_pushButton_res.setText(QCoreApplication.translate("JTA_MostrarReservas", u"RESERVAR", None))
#if QT_CONFIG(tooltip)
        self.JTA_pushButton_refr.setToolTip(QCoreApplication.translate("JTA_MostrarReservas", u"<html><head/><body><p>Actualizar las reservas disponibles</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.JTA_pushButton_refr.setText("")
        self.JTA_label_1.setText(QCoreApplication.translate("JTA_MostrarReservas", u"<html><head/><body><p><img src=\":/imagenes/brianda.png\"/></p></body></html>", None))
        self.JTA_label_2.setText(QCoreApplication.translate("JTA_MostrarReservas", u"Salones disponibles", None))
        self.JTA_label_3.setText(QCoreApplication.translate("JTA_MostrarReservas", u"Reservas disponibles", None))
    # retranslateUi

