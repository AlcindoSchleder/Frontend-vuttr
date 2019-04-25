# -*- coding: utf-8 -*-

"""
Programa de estudos de eventos, timer, progressbar e messagebox 

Author: Alcindo Schleder
Website: https://www.vocatiotelecom.com.br
Last edited: April 14, 2018 
"""
from inspect import signature
import re
from commom.baseClass import *

"""
    Class that raises a exception on validade the StateChange CallBack - screenState.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""
class InvalidCallback(Exception):
    def __init__(self, e: int):
        super(InvalidCallback, self).__init__()
        self.message = """
            A função de Callback não é do tipo StateChange.
            Esta função deve conter 2 argumentos do tipo inteiro,
            Um Argumento do tipo array associativo = None e
            Um argumento do tipo string = None!!!
            {errMsg}
        """
        # Call the base class constructor with the parameters it needs
        self.error = e
        
    def __str__(self):
        argTypes = ['int', 'int', 'dict', 'str']
        argPos = ['primeiro', 'segundo', 'terceiro', 'quarto']
        qtdInv = 'Quantidade de argumentos é inválida'
        eMsg = 'O {pos} Argumento da função de callback devem ser do tipo "{type}"'
        self.message = self.message.format(errMsg=qtdInv) if self.error > 4 else self.message.format(errMsg=eMsg.format(pos=argPos[self.error], type=argTypes[self.error]))
        return self.message

"""
    Class that raises a exception on call StateChange CallBack - screenState.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""
class ExceptionChangeState(Exception):
    def __init__(self, oper: int, dscr: str, error: int, errMsg: str):
        # Call the base class constructor with the parameters it needs
        super(ExceptionChangeState, self).__init__(errMsg)
        self.oper = oper
        self.dscr = dscr
        self.error = error
        self.errMsg = errMsg
        self.message = "Um Erro ocorreu ao tentar executar a operação '{oper}:{dscr}'!!\n    {error:%d}:{errMsg}"
        self.message.format(oper=self.oper, dscr=self.dscr, error=self.error, errMsg=self.errMsg)

    def __str__(self):
        return str(self.message)

"""
    Class that manage a database Form - screenState.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""
STT_NAME = 0
STT_DSCR = 1
STT_BG   = 2
STT_FG   = 3

class TScreenStates(TBaseClass):
    # Class constructor: this class receive a callback function that must follow this format:
    # def name_of_function(OldState: int, NewState: int):
    def __init__(self, callback):
        self._OnStateChange = None
        self._activeValue    = self.ssInactive # Property that represents the Work State of Form
        # This propert is screenstate transition... 
        # change it then call callback function if result is ok
        # set active State to Browse else return work state to active state before call
        self._workValue      = self.ssInactive 
        # Property that store a callback function of the StateChange
        # then is called each _workState changes
        # its your setter test callback function
        self.OnStateChange = callback
    @property
    def ssInactive(self):
        return 0

    @property
    def ssInsert(self):
        return 1

    @property
    def ssUpdate(self):
        return 2

    @property
    def ssDelete(self):
        return 4

    @property
    def ssBrowse(self):
        return 8

    @property
    def ssClose(self):
        return 16

    @property
    def ssCancel(self):
        return 32

    @property
    def ssPost(self):
        return 64

    @property
    def ssCommit(self):
        return 128

    @property
    def ssStartTr(self):
        return 256

    @property
    def ssRollback(self):
        return 512

    @property
    def ssFirst(self):
        return 1024

    @property
    def ssPrior(self):
        return 2048

    @property
    def ssNext(self):
        return 4096

    @property
    def ssLast(self):
        return 8192

    @property
    def ssRefresh(self):
        return 16384

    @property
    def ssOpen(self):
        return 32768

    @property
    def ssSearch(self):
        return 65536

    @property
    def ssExecute(self):
        return 131072

    @property
    def ssValidate(self):
        return 262144

    @property
    def ssSearchAll(self):
        return 524288

    @property
    def ssFilter(self):
        return 1048576

    @property
    def UPDATE_STATE(self):
        # set states to format Form at update mode
        return (self.ssInsert  | self.ssUpdate  | self.ssDelete   | self.ssPost    | self.ssValidate )

    @property
    def BROWSE_STATE(self):
        # set states to format Form at browse mode
        return (self.ssBrowse  | self.ssFirst   | self.ssPrior    | self.ssNext    | self.ssRefresh  | self.ssLast | self.ssCancel)

    @property
    def DATABASE_STATE(self):
        # set states to format Form at Database manager mode
        return (self.ssCommit  | self.ssStartTr | self.ssRollback | self.ssValidate)

    @property
    def LOADING_STATE(self):
        # set states to format Form at Loading Data mode
        return (self.ssSearch  | self.ssExecute | self.ssClose    | self.ssOpen    | self.ssSearchAll | self.ssFilter)
 
    def getStateProperties(self, stt: int):
        res = False
        if (stt in self.states):
            res = {
                "Name": self.states[stt][STT_NAME],
                "Descr": self.states[stt][STT_DSCR],
                "Value": stt,
                "BG": self.states[stt][STT_BG],
                "FG": self.states[stt][STT_FG]
            }
        return res
    
    @property
    def states(self):
        # Dictionary of all states that defines description, backgroud and font color to 
        # display in status bar of Form
        return {
            #    key             name            descr          BG         FG
            self.ssInactive : ['ssInactive'  , 'Inativo'    , 'black'  , 'white' ], 
            self.ssInsert   : ['ssInsert'    , 'Inserindo'  , 'orange' , 'red'   ], 
            self.ssUpdate   : ['ssUpdate'    , 'Editando'   , 'green'  , 'lime'  ],
            self.ssDelete   : ['ssDelete'    , 'Excluindo'  , 'red'    , 'yellow'], 
            self.ssBrowse   : ['ssBrowse'    , 'Navegando'  , 'skyblue', 'blue' ],
            self.ssClose    : ['ssClose'     , 'Fechado'    , 'black'  , 'white' ],
            self.ssCancel   : ['ssCancel'    , 'Cancelando' , 'aqua'   , 'blue'  ],
            self.ssPost     : ['ssPost'      , 'Gravando'   , 'black'  , 'white' ], 
            self.ssCommit   : ['ssCommit'    , 'Atualizando', 'green'  , 'yellow'],
            self.ssStartTr  : ['ssStartTr'   , 'Iniciando'  , 'green'  , 'yellow'],
            self.ssRollback : ['ssRollback'  , 'Retornando' , 'red'    , 'black' ],
            self.ssPrior    : ['ssPrior'     , 'Início'     , 'black'  , 'white' ],
            self.ssPrior    : ['ssPrior'     , 'Anterior'   , 'black'  , 'white' ],
            self.ssNext     : ['ssNext'      , 'Próximo'    , 'black'  , 'white' ], 
            self.ssLast     : ['ssLast'      , 'Último'     , 'black'  , 'white' ], 
            self.ssRefresh  : ['ssRefresh'   , 'Recarregar' , 'green'  , 'black' ],
            self.ssOpen     : ['ssOpen'      , 'Conectando' , 'blue'   , 'white' ],
            self.ssSearch   : ['ssSearch'    , 'Pesquisando', 'info'   , 'orange'],
            self.ssExecute  : ['ssExecute'   , 'Coletando'  , 'red'    , 'yellow'], 
            self.ssValidate : ['ssValidate'  , 'Validando'  , 'white'  , 'orange'],
            self.ssSearchAll: ['ssSearchAll' , 'Listando'   , 'info'   , 'orange']
        }

    @property # get workValue  Name
    def activeValue(self):
        res = self.getStateProperties(self._activeValue)
        if (res):
            return res
        else:
            raise NotImplementedError(404, 'Código do Status (' + str(self._activeValue) + ') não existe')

    @property # get workValue  Name
    def workValue(self):
        res = self.getStateProperties(self._workValue)
        if (res):
            return res
        else:
            raise NotImplementedError(404, 'Código do Status (' + str(self._workValue) + ') não existe')

    @property
    def OnStateChange(self):
        return self._OnStateChange

    def inUpdate(self, stt: int):
        return bool(self.UPDATE_STATE & stt)
        
    def inBrowse(self, stt: int):
        return bool(self.BROWSE_STATE & stt)

    def inLoading(self, stt: int):
        return bool(self.LOADING_STATE & stt)

    def inDatabase(self, stt: int):
        return bool(self.DATABASE_STATE & stt)

    @workValue.setter # sets the value to _workValue and triggered _onStateChange event
    def workValue(self, value: int):
        if ((self._OnStateChange) and (value in self.states) and (self._workValue != value)):
            self._workValue = value
            try:
                self.result = self._OnStateChange(self._workValue, self.activeValue)
                if (self.resultStatusCode != 200):
                    raise ExceptionChangeState(self._workValue, self.states[self._workValue][STT_DSCR], self.resultStatusCode, self.resultStatusMessage)
            except ExceptionChangeState as e:
                self._workValue = self._activeValue
                # call a event callback
                self._OnStateChange(self._workValue, self.activeValue, self.result, e)

    @OnStateChange.setter
    def OnStateChange(self, callback):
        hasErr = False
        params = ['int', 'int', 'dict', 'str']
        sig = signature(callback)
        if (len(sig.parameters) == 4):
            idx = 0
            for param in sig.parameters:
                s = str(sig.parameters[param])
                regex = "^({S}:\s)".format(S=param) + "|(\s=).*"
                s = re.sub(regex, '', s)
                if (s != params[idx]):
                    hasErr = idx
                    break
                idx += 1
        else:
            hasErr = 5
        if (hasErr != False):
            raise InvalidCallback(hasErr)
        if (callback != self._OnStateChange):
            self._OnStateChange = callback
    
"""
To check the existence of a global variable:
if 'myVar' in locals():
  # myVar exists.

To check the existence of a global variable:
if 'myVar' in globals():
  # myVar exists.

To check if an object has an attribute:
if hasattr(obj, 'attr_name'):
  # obj.attr_name exists.
"""