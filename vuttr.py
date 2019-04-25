# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qtDesigner/frmVuttr.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication
from commom.frmBase import TfrmBase
import sys

class TfrmVuttr(TfrmBase):
    def __init__(self):
        super(TfrmVuttr, self).__init__()
        # self.setWindowIcon(self.getIcon("../resources/vuttr.ico", QSize(32, 32)))

    def translateForm(self, AForm):
        AForm.setWindowTitle(self._translate("TfrmVuttr", "VUTTR Application"))
        self.dcTitle.setText(self._translate("TfrmVuttr", "Cadastro de Ferramentas para Lembrar"))

root = QApplication([])
app = TfrmVuttr()
app.show()
sys.exit(root.exec_())
