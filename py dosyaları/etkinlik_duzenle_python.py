# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'etkinlik_duzenle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 353)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 20, 781, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 10, 711, 101))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.id_label = QtWidgets.QLabel(self.widget)
        self.id_label.setObjectName("id_label")
        self.gridLayout_2.addWidget(self.id_label, 0, 0, 1, 1)
        self.id_line_edit = QtWidgets.QLineEdit(self.widget)
        self.id_line_edit.setObjectName("id_line_edit")
        self.gridLayout_2.addWidget(self.id_line_edit, 0, 1, 1, 1)
        self.mekan_label = QtWidgets.QLabel(self.widget)
        self.mekan_label.setObjectName("mekan_label")
        self.gridLayout_2.addWidget(self.mekan_label, 0, 2, 1, 1)
        self.mekan_line_edit = QtWidgets.QLineEdit(self.widget)
        self.mekan_line_edit.setObjectName("mekan_line_edit")
        self.gridLayout_2.addWidget(self.mekan_line_edit, 0, 3, 1, 1)
        self.bilet_fiyat_label = QtWidgets.QLabel(self.widget)
        self.bilet_fiyat_label.setObjectName("bilet_fiyat_label")
        self.gridLayout_2.addWidget(self.bilet_fiyat_label, 0, 4, 1, 1)
        self.bilet_fiyat_line_edit = QtWidgets.QLineEdit(self.widget)
        self.bilet_fiyat_line_edit.setObjectName("bilet_fiyat_line_edit")
        self.gridLayout_2.addWidget(self.bilet_fiyat_line_edit, 0, 5, 1, 1)
        self.etkinlik_adi_label = QtWidgets.QLabel(self.widget)
        self.etkinlik_adi_label.setObjectName("etkinlik_adi_label")
        self.gridLayout_2.addWidget(self.etkinlik_adi_label, 1, 0, 1, 1)
        self.etkinlik_adi_line_Edit = QtWidgets.QLineEdit(self.widget)
        self.etkinlik_adi_line_Edit.setObjectName("etkinlik_adi_line_Edit")
        self.gridLayout_2.addWidget(self.etkinlik_adi_line_Edit, 1, 1, 1, 1)
        self.bilet_sayisi_label = QtWidgets.QLabel(self.widget)
        self.bilet_sayisi_label.setObjectName("bilet_sayisi_label")
        self.gridLayout_2.addWidget(self.bilet_sayisi_label, 1, 2, 1, 1)
        self.bilet_sayisi_line_edit = QtWidgets.QLineEdit(self.widget)
        self.bilet_sayisi_line_edit.setObjectName("bilet_sayisi_line_edit")
        self.gridLayout_2.addWidget(self.bilet_sayisi_line_edit, 1, 3, 1, 1)
        self.tarih_label = QtWidgets.QLabel(self.widget)
        self.tarih_label.setObjectName("tarih_label")
        self.gridLayout_2.addWidget(self.tarih_label, 1, 4, 1, 1)
        self.tarih_line_Edit = QtWidgets.QLineEdit(self.widget)
        self.tarih_line_Edit.setObjectName("tarih_line_Edit")
        self.gridLayout_2.addWidget(self.tarih_line_Edit, 1, 5, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(140, 190, 541, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(50, 30, 431, 25))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ekle_buton = QtWidgets.QPushButton(self.widget1)
        self.ekle_buton.setObjectName("ekle_buton")
        self.gridLayout.addWidget(self.ekle_buton, 0, 0, 1, 1)
        self.guncelle_buton = QtWidgets.QPushButton(self.widget1)
        self.guncelle_buton.setObjectName("guncelle_buton")
        self.gridLayout.addWidget(self.guncelle_buton, 0, 1, 1, 1)
        self.sil_buton = QtWidgets.QPushButton(self.widget1)
        self.sil_buton.setObjectName("sil_buton")
        self.gridLayout.addWidget(self.sil_buton, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id_label.setText(_translate("Form", "ID"))
        self.mekan_label.setText(_translate("Form", "Mekan"))
        self.bilet_fiyat_label.setText(_translate("Form", "Bilet Fiyatı"))
        self.etkinlik_adi_label.setText(_translate("Form", "Etkinlik Adı"))
        self.bilet_sayisi_label.setText(_translate("Form", "Bilet Sayısı"))
        self.tarih_label.setText(_translate("Form", "Tarih"))
        self.ekle_buton.setText(_translate("Form", "Ekle"))
        self.guncelle_buton.setText(_translate("Form", "Güncelle"))
        self.sil_buton.setText(_translate("Form", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
