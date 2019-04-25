# -*- coding: utf-8 -*-

"""
    Class to provide a CRUD form with all controls - frmBase.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""

from baseClass import BaseClass
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                            QHBoxLayout, QVBoxLayout, QMenuBar,QMenu, QToolBar,
                            QAction, QTabWidget, QTreeWidget, QFormLayout, QFrame,
                            QStatusBar, QProgressBar, QPushButton, QMessageBox,
                            QLayout, QSizePolicy, QLabel)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize, QRect, QObject, QCoreApplication, pyqtSignal, pyqtSlot
from screenState import TScreenStates

class TfrmBase(QMainWindow, BaseClass):
    def __init__(self, parent=None):
        super(TfrmBase, self).__init__()
        self.recordCount = 0
        self._screenState = TScreenStates(self.onStateChange)
        self.activeState = self._screenState.ssInactive
        self._defaultSettings()
        self._createWidgets()
        self._setEvents()
        self.translateForm()

    def _defaultSettings(self):
        self.setObjectName("frmBase")
        self.resize(640, 480)
        self.setMinimumSize(QSize(640, 480))
    
    def _createWidgets(self):
        self._createLayout()
        self._createMenus()
        self._createToolBar()
        self._createStatusBar()
        self._createPages()
        self._setLayouts()
    
    def _createLayout(self):
        self.clientArea = QWidget()
        self.clientArea.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.clientArea.setMinimumSize(QSize(640, 400))
        self.clientArea.setBaseSize(QSize(640, 400))
        self.clientArea.setLayoutDirection(Qt.LeftToRight)
        self.clientArea.setObjectName("clientArea")
        self.gridLayout = QGridLayout(self.clientArea)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

    def _createMenus(self):
        # Create a Menu Bar
        self.mnMenu = self.menuBar()
        self.mnMenu.setObjectName("mnMenu")
        # Create all Top Menus
        self.mnApp = QMenu('&Aplicação')
        self.mnApp.setObjectName('mnApp')
        self.mnOpe = QMenu('&Operação')
        self.mnOpe.setObjectName("mnOperations")
        self.mnNav = QMenu('&Navegação')
        self.mnNav.setObjectName("mnNav")
        # Set Menus to MenuBar
        self.mnMenu.addMenu(self.mnNav)
        self.mnMenu.addMenu(self.mnOpe)
        self.mnMenu.addMenu(self.mnApp)
        # Crealte all Actions to Application Menu
        self._createAppActions()
        self._createOpeActions()
        self._setMenuActions()
        self.mnMenu.addAction(self.mnApp.menuAction())
        self.mnMenu.addAction(self.mnOpe.menuAction())
        self.mnMenu.addAction(self.mnNav.menuAction())
        self._settingActionsEvents()

    def _createAppActions(self):
        # Exit Program Action
        self.acExit = QAction(self.getIcon("../resources/exit.ico", QSize(32, 32)), '&Sair')
        self.acExit.setObjectName("acExit")
        self.acExit.setShortcut('Ctrl+Q')
        self.acExit.setStatusTip('Finalizar o Programa')
        self.acExit.triggered.connect(self.closeApp)
    
    def _createOpeActions(self):
        # Search Action
        self.acSearch = QAction(self.getIcon("../resources/Search.ico", QSize(32, 32)), '&Pesquisar')
        self.acSearch.setObjectName("acSearch")
        self.acSearch.setShortcut('F5,Ctrl+P')
        self.acSearch.setStatusTip('Preenche o Filtro para Selecionar Registros')
        # List Action
        self.acList = QAction(self.getIcon("../resources/list.ico", QSize(32, 32)), '&Listar')
        self.acList.setShortcut('Ctrl+L')
        self.acList.setStatusTip('Listar todos os Registros')
        self.acList.setObjectName("acList")
        # Insert Action
        self.acInsert = QAction(self.getIcon("../resources/db_add.ico", QSize(32, 32)), '&Inserir')
        self.acInsert.setShortcut('F2,Ins')
        self.acInsert.setStatusTip('Incluir Novo Registros')
        self.acInsert.setObjectName("acInsert")
        # Update Action
        self.acUpdate = QAction(self.getIcon("../resources/db_update.ico", QSize(32, 32)), '&Editar')
        self.acUpdate.setShortcut('Ctrl+U')
        self.acUpdate.setStatusTip('Editar o Registro Atual')
        self.acUpdate.setObjectName("acUpdate")
        # Delete Action
        self.acDelete = QAction(self.getIcon("../resources/db_remove.ico", QSize(32, 32)), '&Excluir')
        self.acDelete.setShortcut('Ctrl+Del')
        self.acDelete.setStatusTip('Exclui o Registro Atual')
        self.acDelete.setObjectName("acDelete")
        # Save Action
        self.acSave = QAction(self.getIcon("../resources/db_commit.ico", QSize(32, 32)), '&Salvar')
        self.acSave.setShortcut('F10,Ctrl+S')
        self.acSave.setStatusTip('Salva as Alterações do Registro')
        self.acSave.setObjectName("acSave")
        # Cancel Action
        self.acCancel = QAction(self.getIcon("../resources/cancel.ico", QSize(32, 32)), '&Cancelar')
        self.acCancel.setShortcut('Esc')
        self.acCancel.setStatusTip('Cancela as Alterações do Registro')
        self.acCancel.setObjectName("acCancel")
        # First Action
        self.acFirst = QAction(self.getIcon("../resources/start.ico", QSize(32, 32)), '&Início')
        self.acFirst.setShortcut('Ctrl+Left')
        self.acFirst.setStatusTip('Vai para o Primeiro Registro')
        self.acFirst.setObjectName("acFirst")
        # Prior Action
        self.acPrior = QAction(self.getIcon("../resources/left.ico", QSize(32, 32)), '&Anterior')
        self.acPrior.setShortcut('Left')
        self.acPrior.setStatusTip('Vai para o Registro Anterior')
        self.acPrior.setObjectName("acPrior")
        # Next Action
        self.acNext = QAction(self.getIcon("../resources/right.ico", QSize(32, 32)), '&Próximo')
        self.acNext.setShortcut('Right')
        self.acNext.setStatusTip('Vai para o Próximo Registro')
        self.acNext.setObjectName("acNext")
        # Last Action
        self.acLast = QAction(self.getIcon("../resources/end.ico", QSize(32, 32)), '&Último')
        self.acLast.setShortcut('Ctrl+Right')
        self.acLast.setStatusTip('Vai para o Último Registro')
        self.acLast.setObjectName("acLast")
        # Form Title Action
        self.dcTitle = QAction()
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dcTitle.setFont(font)
        self.dcTitle.setObjectName("dcTitle")

    def getIcon(self, res: str, size: QSize) -> QIcon:
        icon = QIcon()
        icon.addPixmap(QPixmap(res).scaled(size.width(), size.height(), Qt.KeepAspectRatio), QIcon.Active, QIcon.On)
        return icon

    def _setMenuActions(self):
        # Set Menu Application Actions
        self.mnApp.addAction(self.acExit)
        # Set Menu Operations Actions
        self.mnOpe.addAction(self.acSearch)
        self.mnOpe.addAction(self.acList)
        self.mnOpe.addSeparator()
        self.mnOpe.addAction(self.acInsert)
        self.mnOpe.addAction(self.acUpdate)
        self.mnOpe.addAction(self.acDelete)
        self.mnOpe.addSeparator()
        self.mnOpe.addAction(self.acSave)
        self.mnOpe.addAction(self.acCancel)
        # Set Menu Navigation Actions
        self.mnNav.addAction(self.acFirst)
        self.mnNav.addAction(self.acPrior)
        self.mnNav.addAction(self.acNext)
        self.mnNav.addAction(self.acLast)
    
    def _settingActionsEvents(self):
        # Set Menu Operations Trigger onClick
        self.acSearch.triggered.connect(lambda: self.setFormStatus(self._screenState.ssSearch))
        self.acList.triggered.connect(lambda: self.setFormStatus(self._screenState.ssSearchAll))
        self.acInsert.triggered.connect(lambda: self.setFormStatus(self._screenState.ssInsert))
        self.acUpdate.triggered.connect(lambda: self.setFormStatus(self._screenState.ssUpdate))
        self.acDelete.triggered.connect(lambda: self.setFormStatus(self._screenState.ssDelete))
        self.acSave.triggered.connect(lambda: self.setFormStatus(self._screenState.ssPost))
        self.acCancel.triggered.connect(lambda: self.setFormStatus(self._screenState.ssCancel))
        # Set Menu Navigation Trigger onClick
        self.acFirst.triggered.connect(lambda: self.setFormStatus(self._screenState.ssFirst))
        self.acPrior.triggered.connect(lambda: self.setFormStatus(self._screenState.ssPrior))
        self.acNext.triggered.connect(lambda: self.setFormStatus(self._screenState.ssNext))
        self.acLast.triggered.connect(lambda: self.setFormStatus(self._screenState.ssLast))

    def _createToolBar(self):
        # Create a tbActions ToolBar
        self.tbActions = QToolBar()
        self.tbActions.setMinimumSize(QSize(300, 34))
        self.tbActions.setMaximumSize(QSize(16777215, 34))
        self.tbActions.setBaseSize(QSize(300, 34))
        self.tbActions.setAcceptDrops(False)
        self.tbActions.setToolTipDuration(3)
        self.tbActions.setAllowedAreas(Qt.TopToolBarArea)
        self.tbActions.setObjectName("tbActions")
        self.addToolBar(Qt.TopToolBarArea, self.tbActions)
        # Create a tbTitle ToolBar
        self.tbTitle = QToolBar()
        self.tbTitle.setMinimumSize(QSize(340, 34))
        self.tbTitle.setMaximumSize(QSize(16777215, 34))
        self.tbTitle.setBaseSize(QSize(341, 34))
        self.tbTitle.setAllowedAreas(Qt.TopToolBarArea)
        self.tbTitle.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tbTitle.setFloatable(False)
        self.tbTitle.setObjectName("tbTitle")
        # self.tbTitle.setLabelAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.addToolBar(Qt.TopToolBarArea, self.tbTitle)
        # Call Add Actions to ToolBar
        self._setToolBarActions()

    def _setToolBarActions(self):
        # Set ToolBar Actions
        self.tbActions.addAction(self.acSearch)
        self.tbActions.addAction(self.acInsert)
        self.tbActions.addAction(self.acUpdate)
        self.tbActions.addAction(self.acDelete)
        self.tbActions.addSeparator()
        self.tbActions.addAction(self.acSave)
        self.tbActions.addAction(self.acExit)
        self.tbTitle.addAction(self.dcTitle)

    def _createStatusBar(self):
        self.sbStatus = QStatusBar()
        self.sbStatus.setMaximumHeight(24)
        self.sbStatus.setObjectName("sbStatus")
        self.sbStatus.setStyleSheet("""
            .QLabel {
                background-color: #FFFFFF;
                color: #000000;
            }
        """)
        self.lbStatus = QLabel(self.sbStatus)
        self.lbStatus.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lbStatus.setText('Inactive')
        self.lbStatus.setMinimumSize(QSize(130, 15))
        self.lbStatus.setFrameShape(QFrame.Panel)
        self.lbStatus.setFrameShadow(QFrame.Sunken)
        self.sbStatus.addPermanentWidget(self.lbStatus)
        self.setStatusBar(self.sbStatus)

    def _createPages(self):
        self.tabMain = QTabWidget(self.clientArea)
        self.tabMain.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.tabMain.setTabPosition(QTabWidget.South)
        self.tabMain.setObjectName("tabMain")
        self.pgList = QWidget(self.tabMain)
        self.pgList.setObjectName("pgList")
        self.pgDetail = QWidget(self.tabMain)
        self.pgDetail.setObjectName("pgDetail")
        self.tabMain.addTab(self.pgList, "")
        self.tabMain.addTab(self.pgDetail, "")
        self._createPageListContent()

    def _createPageListContent(self):
        self.treeWidget = QTreeWidget(self.pgList)
        self.treeWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.treeWidget.setFrameShape(QFrame.NoFrame)
        self.treeWidget.setFrameShadow(QFrame.Plain)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Campo")
        self.treeWidget.headerItem().setText(1, "Campo")
        self.treeWidget.headerItem().setText(2, "Campo")
        self.treeWidget.setGeometry(QRect(0, 0, 640, 370))
        self.treeWidget.setMinimumSize(QSize(640, 370))
        self.tabMain.setCurrentIndex(0)

    def _setLayouts(self):
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
        self.gridLayout.addWidget(self.tabMain, 0, Qt.AlignBottom | Qt.AlignRight, 1, 1)
        self.setCentralWidget(self.clientArea)

    def translateForm(self): 
        self._translate = QCoreApplication.translate
        self.setWindowTitle(self._translate("TfrmBase", "Tela de Básica de Cadastros"))
        self.mnApp.setTitle(self._translate("TfrmBase", "Aplicação"))
        self.mnOpe.setTitle(self._translate("TfrmBase", "Operações"))
        self.mnNav.setTitle(self._translate("TfrmBase", "Navegação"))
        self.sbStatus.setToolTip(self._translate("TfrmBase", "Barra de Status"))
        self.tbActions.setWindowTitle(self._translate("TfrmBase", "Ferramentas"))
        self.tbActions.setToolTip(self._translate("TfrmBase", "Barra de Ferramentas"))
        self.tbTitle.setWindowTitle(self._translate("TfrmBase", "Descrição"))
        self.acExit.setText(self._translate("TfrmBase", "&Sair"))
        self.acExit.setToolTip(self._translate("TfrmBase", "Sair do Programa"))
        self.acSearch.setText(self._translate("TfrmBase", "&Pesquisar"))
        self.acSearch.setStatusTip(self._translate("TfrmBase", "Procurar Por um Registro"))
        self.acList.setText(self._translate("TfrmBase", "&Listar Todos"))
        self.acList.setStatusTip(self._translate("TfrmBase", "Lista todos os Registros"))
        self.acInsert.setText(self._translate("TfrmBase", "&Inserir"))
        self.acInsert.setStatusTip(self._translate("TfrmBase", "Adicionar Registro"))
        self.acUpdate.setText(self._translate("TfrmBase", "&Editar"))
        self.acUpdate.setStatusTip(self._translate("TfrmBase", "Editar Registro"))
        self.acDelete.setText(self._translate("TfrmBase", "E&xcluir"))
        self.acDelete.setStatusTip(self._translate("TfrmBase", "Excluir Registro"))
        self.acSave.setText(self._translate("TfrmBase", "&Salvar"))
        self.acSave.setToolTip(self._translate("TfrmBase", "Salvar Registro"))
        self.acCancel.setText(self._translate("TfrmBase", "&Cancelar"))
        self.acCancel.setToolTip(self._translate("TfrmBase", "Cencelar Alterações"))
        self.dcTitle.setText(self._translate("TfrmBase", "Título da Tela de Cadastros"))
        self.dcTitle.setToolTip(self._translate("TfrmBase", "Título da Tela de Cadastros"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pgList), self._translate("TfrmBase", "Lista dos Registros"))
        self.tabMain.setTabToolTip(self.tabMain.indexOf(self.pgList), self._translate("TfrmBase", "Listagem das Ferramentas"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pgDetail), self._translate("TfrmBase", "Detalhes do Registro Selecionando"))

    @property
    def activeState(self):
        return self._screenState._activeValue

    @property
    def activeStateColor(self):
        return self._screenState.activeValue['FG']

    @property
    def activeStateBackgroud(self):
        return self._screenState.activeValue['BG']

    @activeState.setter # Seta a Propriedade _activeState
    def activeState(self, value: int):
        self._screenState.workValue = value
        self._activeState = value

    def setScreenState(self, stt: int):
        self.acExit.setEnabled(self._screenState.inBrowse(stt))
        # Set Menu Operations Actions
        self.acSearch.setEnabled((self._screenState.inBrowse(stt) or (self.recordCount == 0)))
        self.acList.setEnabled((self._screenState.inBrowse(stt) or (self.recordCount == 0)))
        self.acInsert.setEnabled(self._screenState.inBrowse(stt))
        self.acUpdate.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        self.acDelete.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        self.acSave.setEnabled(self._screenState.inUpdate(stt))
        self.acCancel.setEnabled(self._screenState.inUpdate(stt))
        # Set Menu Navigation Actions
        self.acFirst.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        self.acPrior.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        self.acNext.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        self.acLast.setEnabled((self._screenState.inBrowse(stt) and (self.recordCount > 0)))
        # Set tab Main if state in Browse enabled
        self.tabMain.setEnabled(self._screenState.inBrowse(stt))

    def _layoutWidgets(self):
        return (self.frmLayout.itemAt(i) for i in range(self.frmLayout.count()))

    def _getAllFields(self):
        arrFields = []
        for w in self._layoutWidgets():
            if (not(isinstance(w, QLabel))):
                arrFields.append(w)
        return arrFields

    def setEnableFields(self, enable: bool = True):
        # Enable All Fields
        for controls in self._layoutWidgets():
            QWidget(controls).setEnabled(enable)

    def clearFields(self):
        # cliar content of all fileds
        for controls in self._getAllFields():
            QWidget(controls).setText('')

    def setColorFields(self):
        # cliar content of all fileds
        style = ".QWidget { backgroud-color: " + self.activeStateBackgroud + "; }"
        for controls in self._getAllFields():
            QWidget(controls).setStyle(style)
        

    def showDataDetails(self):
        # move data of selected record to fileds
        if (self.tabMain.currentIndex() == 0):
            self.tabMain.setCurrentIndex(1)
        
    def filterRecord(self):
        raise NotImplementedError(500)

    def getFirstRecord(self):
        raise NotImplementedError(500)

    def getPriorRecord(self):
        raise NotImplementedError(500)

    def getNextRecord(self):
        raise NotImplementedError(500)

    def getLastRecord(self):
        raise NotImplementedError(500)

    def insertRecord(self):
        raise NotImplementedError(500)

    def deleteRecord(self):
        raise NotImplementedError(500)

    def updateRecord(self):
        raise NotImplementedError(500)

    def postRecord(self):
        raise NotImplementedError(500)

    def execOpertations(self, state: int):
        if ((state == self._screenState.ssFilter) or (state == self._screenState.ssSearchAll)):
            self.filterRecord()
        elif (state == self._screenState.ssFirst):
            self.getFirstRecord()
        elif (state == self._screenState.ssPrior):
            self.getPriorRecord()
        elif (state == self._screenState.ssNext):
            self.getNextRecord()
        elif (state == self._screenState.ssLast):
            self.getLastRecord()
        elif (state == self._screenState.ssInsert):
            self.insertRecord()
        elif (state == self._screenState.ssDelete):
            self.deleteRecord()
        elif (state == self._screenState.ssUpdate):
            self.updateRecord()
        elif (state == self._screenState.ssPost):
            self.postRecord()
        else:
            raise NotImplementedError(401, 'Operação não suportada')
    
    @pyqtSlot(int)
    def setFormStatus(self, state: int):
        if ((state == self._screenState.ssSearch) and (self.activeState != state)):
            self.clearFields()
            self.setColorFields()
            self.showDataDetails()

        if (self.activeState != state):
            self.activeState = state
            if (state == self._screenState.ssCancel):
                self.activeState = self._screenState.ssBrowse


    @pyqtSlot(int, int, dict, str)
    def onStateChange(self, NewState: int, OldState: int, Result:dict = {}, Err:str = ''):
        try:
            # show screen state on status bar
            state = self._screenState.getStateProperties(NewState)
            style = '.QLabel { background-color: ' + state['BG'] + '; color: ' + state['FG'] + '; }'
            self.sbStatus.setStyleSheet(style)
            self.lbStatus.setText(state['Descr'])

            # change buttons states
            self.setScreenState(NewState)
            # call operation into child screen
            self.execOperation(NewState)
            # set result status code and result satatus Message
            self.setResultStatusCode = 200
            self.setResultStatusMessage = ''
        except Exception as e:
            self.ResultStatusCode = 200
            self.ResultStatusMessage = str(e)
            QMessageBox.critical(self, self.windowTitle(), self.ResultStatusMessage)
        return self.result

    @pyqtSlot()
    def tabMainChanged(self):
        self.sbStatus.showMessage('TabMain change tabIndex to (' + str(self.tabMain.currentIndex()) + ')!')
        if (self.tabMain.currentIndex() == 1):
            self.showDataDetails()
        
    @pyqtSlot()
    def InsertData(self):
        # self.sbStatus.showMessage('Prepare to insert data....')
        pass

    def _setEvents(self):
        self.tabMain.blockSignals(True) # just for not showing the initial message
        self.tabMain.currentChanged.connect(self.tabMainChanged) # changed!
        self.tabMain.blockSignals(False) # wait signals now

    @pyqtSlot()
    def closeApp(self):
        self.close()

root = QApplication([])
app = TfrmBase()
app.show()
import sys
sys.exit(root.exec_())
