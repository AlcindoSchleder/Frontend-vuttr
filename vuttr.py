# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qtDesigner/frmVuttr.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, QLayout, QLabel,
                            QLineEdit, QTextEdit, QListWidget, QDateTimeEdit, 
                            QMessageBox)
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication
from commom.frmBase import TfrmBase
import sys

class TfrmVuttr(TfrmBase):
    def __init__(self):
        super(TfrmVuttr, self).__init__()
        self.setWindowIcon(self.getIcon("./resources/vuttr.ico", QSize(32, 32)))
        self._createFormWidgets()
        self.translateForm()
        self.activeState = self.ssSearch
    
    def _createFormWidgets(self):
        self.formLayoutWidget = QWidget(self.pgDetail)
        self.formLayoutWidget.setGeometry(QRect(-1, -1, 641, 370))
        self.formLayoutWidget.setMinimumSize(QSize(641, 370))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.frmLayout = QFormLayout(self.formLayoutWidget)
        self.frmLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.frmLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.frmLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.frmLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.frmLayout.setContentsMargins(5, 5, 5, 5)
        self.frmLayout.setSpacing(6)
        self.frmLayout.setObjectName("frmLayout")
        self.lbToolTitle = QLabel(self.formLayoutWidget)
        self.lbToolTitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbToolTitle.setObjectName("lbToolTitle")
        self.frmLayout.setWidget(0, QFormLayout.LabelRole, self.lbToolTitle)
        self.lbLink = QLabel(self.formLayoutWidget)
        self.lbLink.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbLink.setObjectName("lbLink")
        self.frmLayout.setWidget(1, QFormLayout.LabelRole, self.lbLink)
        self.eUrlTool = QLineEdit(self.formLayoutWidget)
        self.eUrlTool.setObjectName("eUrlTool")
        self.frmLayout.setWidget(1, QFormLayout.FieldRole, self.eUrlTool)
        self.lbDescription = QLabel(self.formLayoutWidget)
        self.lbDescription.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbDescription.setObjectName("lbDescription")
        self.frmLayout.setWidget(2, QFormLayout.LabelRole, self.lbDescription)
        self.eDscTool = QTextEdit(self.formLayoutWidget)
        self.eDscTool.setMinimumSize(QSize(0, 100))
        self.eDscTool.setMaximumSize(QSize(16777215, 100))
        self.eDscTool.setBaseSize(QSize(0, 100))
        self.eDscTool.setObjectName("eDscTool")
        self.frmLayout.setWidget(2, QFormLayout.FieldRole, self.eDscTool)
        self.lbTags = QLabel(self.formLayoutWidget)
        self.lbTags.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbTags.setObjectName("lbTags")
        self.frmLayout.setWidget(3, QFormLayout.LabelRole, self.lbTags)
        self.eToolTags = QListWidget(self.formLayoutWidget)
        self.eToolTags.setMinimumSize(QSize(0, 100))
        self.eToolTags.setMaximumSize(QSize(16777215, 100))
        self.eToolTags.setBaseSize(QSize(0, 100))
        self.eToolTags.setObjectName("eToolTags")
        self.frmLayout.setWidget(3, QFormLayout.FieldRole, self.eToolTags)
        self.lbInsertDate = QLabel(self.formLayoutWidget)
        self.lbInsertDate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbInsertDate.setObjectName("lbInsertDate")
        self.frmLayout.setWidget(4, QFormLayout.LabelRole, self.lbInsertDate)
        self.eInsertDate = QDateTimeEdit(self.formLayoutWidget)
        self.eInsertDate.setObjectName("eInsertDate")
        self.frmLayout.setWidget(4, QFormLayout.FieldRole, self.eInsertDate)
        self.eToolTitle = QLineEdit(self.formLayoutWidget)
        self.eToolTitle.setObjectName("eToolTitle")
        self.frmLayout.setWidget(0, QFormLayout.FieldRole, self.eToolTitle)
        self.eUpdateDate = QDateTimeEdit(self.formLayoutWidget)
        self.eUpdateDate.setObjectName("eUpdateDate")
        self.frmLayout.setWidget(5, QFormLayout.FieldRole, self.eUpdateDate)
        self.lbUpdateDate = QLabel(self.formLayoutWidget)
        self.lbUpdateDate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbUpdateDate.setObjectName("lbUpdateDate")
        self.frmLayout.setWidget(5, QFormLayout.LabelRole, self.lbUpdateDate)

    def translateForm(self):
        super(TfrmVuttr, self).translateForm()
        self.setWindowTitle(self._translate("TfrmVuttr", "VUTTR Application"))
        self.dcTitle.setText(self._translate("TfrmVuttr", "Ferramentas para Lembrar"))
        self.lbToolTitle.setText(self._translate("TfrmVuttr", "Título da Ferramenta: "))
        self.lbLink.setText(self._translate("TfrmVuttr", "Url da Ferramenta: "))
        self.lbDescription.setText(self._translate("TfrmVuttr", "Descrição: "))
        self.lbTags.setText(self._translate("TfrmVuttr", "Tags: "))
        self.lbInsertDate.setText(self._translate("TfrmVuttr", "Data de Inserção: "))
        self.lbUpdateDate.setText(self._translate("TfrmVuttr", "Data  da Última Edição: "))

    def filterRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'filtrando Registros')

    def getFirstRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Primeiro Registro')

    def getPriorRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Registro Anterior')

    def getNextRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Próximo Registro')

    def getLastRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Último Registro')

    def insertRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Inserir Registro')

    def deleteRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Excluindo Registro')

    def updateRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Editando Registro')

    def postRecord(self):
        QMessageBox.information(self, self.windowTitle(), 'Gravando Registro')

root = QApplication([])
app = TfrmVuttr()
app.show()
sys.exit(root.exec_())
