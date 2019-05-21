# -*- coding: utf-8 -*-

"""
Constantes pré definidas do python

Author: Alcindo Schleder
Website: https://www.vocatiotelecom.com.br
Last edited: April 14, 2018 
"""

"""
    Class that raises a exception to Abstract Methods - baseClass.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""

class NotImplementedError(Exception):
    def __init__(self, e: int = 404, msg: str = None):
        super(NotImplementedError, self).__init__()
        self._errorsList = errorCodes()
        self.error = 500
        if ((e) and (self._errorsList.isValid(e))):
            self.error = e
        self._errorDescr = self._errorsList.errorCodeDescr(self.error)
        self.message = 'Future not implemented yet! -> ({error:d}) - {descr}'
        if (msg):
            self.message = msg + "! -> ({error:d}) - {descr}"

    def __str__(self):
        return self.message.format(error=self.error, descr=self._errorDescr)

"""
    Class that inform a error code of http list - baseClass.py

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""

class errorCodes:
    def __init__(self):
        super(errorCodes, self).__init__()
        self._errorList = {
            "1xx": {
                "name": 'Information', 
                "code": {
                    100: 'Continue',
                    101: 'Switching Protocols',
                    102: 'Processing',
                    103: 'Early Hints'
                }
            },
            "2xx": {
                "name": 'Success',
                "code": {
                    200: 'OK',
                    201: 'Created',
                    202: 'Accepted',
                    203: 'Non-Authoritative Information',
                    204: 'No Content',
                    205: 'Reset Content',
                    206: 'Partial Content',
                    207: 'Multi-Status',
                    208: 'Already Reported',
                    226: 'IM Used'
                }
            },
            "3xx": {
                "name": 'Redirection',
                "code": {
                    300: 'Multiple Choices',
                    301: 'Moved Permanently',
                    302: 'Found',
                    303: 'See Other',
                    304: 'Not Modified',
                    305: 'Use Proxy',
                    306: 'Switch Proxy',
                    307: 'Temporary Redirect',
                    308: 'Permanent Redirect'
                }
            },
            "4xx": {
                "name": 'Client Errors',
                "code": {
                    400: 'Bad Request',
                    401: 'Unauthorized',
                    402: 'Payment Required',
                    403: 'Forbidden',
                    404: 'Not Found',
                    405: 'Method Not Allowed',
                    406: 'Not Acceptable',
                    407: 'Proxy Authentication Required',
                    408: 'Request Timeout',
                    409: 'Conflict',
                    410: 'Gone',
                    411: 'Length Required',
                    412: 'Precondition',
                    413: 'Payload Too Large',
                    414: 'URI Too Long',
                    415: 'Unsupported Media Type',
                    416: 'Range Not Satisfiable',
                    417: 'Expectation Failed',
                    418: 'I am a teapot',
                    421: 'Misdirected Request',
                    422: 'Unprocessable Entity',
                    423: 'Locked',
                    424: 'Failed Dependency',
                    425: 'Too Early',
                    426: 'Upgrade Required',
                    428: 'Precondition Required',
                    429: 'Too Many Requests',
                    431: 'Request Header Fields Too Large',
                    451: 'Unavailable For Legal Reasons'
                }
            },
            "5xx": {
                "name": 'Server errors',
                "code": {
                    500: 'Internal Server Error',
                    501: 'Not Implemented',
                    502: 'Bad Gateway',
                    503: 'Service Unavailable',
                    504: 'Gateway Timeout',
                    505: 'HTTP Version Not Supported',
                    506: 'Variant Also Negotiates',
                    507: 'Insufficient Storage',
                    508: 'Loop Detected',
                    510: 'Not Extended',
                    511: 'Network Authentication Required'
                }
            },
            "6xx": {
                "name": "Custom",
                "code": {
                    600: "Custom Error Message"
                }
            }
        }

    @property
    def errorList(self):
        return self._errorList

    @property
    def errorGroup(self, code: int = 200):
        grp = self.isValid(code)
        if (grp):
            return self._errorList[grp]["code"]
        else:
            raise NotImplementedError(404)
    
    @property
    def errorGroupAndCodeDescr(self, code: int = 200):
        grp = self.isValid(code)
        if (grp):
            return { 
                "groupName": self._errorList[grp]["name"],
                "codeDescr": self._errorList[grp]["code"][code]
            }
        else:
            raise NotImplementedError(404)

    @property
    def errorCodeDescr(self, code: int = 200):
        grp = self.isValid(code)
        if (grp):
            return self._errorList[grp]["code"][code]
        else:
            raise NotImplementedError(404)
    
    def isValid(self, code: int = 200):
        if (code > 99): 
            grp = code // 100 
        else: 
            grp = 4
        grp = str(grp) + 'xx'
        if ((self._errorList.get(grp)) and 
            (self._errorList[grp].get("code")) and 
            (self._errorList[grp]["code"].get(code))):
            return grp
        else:
            return False

"""
    Base class of project - screenState.py
    This class is a base class for all classes and provides
    a result object as descript below:

    data: stores all data of result of operations
    state: key of result state 
        sttCode: Stores de Code of error (!=200) or success (200) - based on http protocol codes
        sttMsgs: Store a error message or success message denpends on code

    All operation functions must to return the result dict 

    * @requires   python 3.+, PyQt5
    * @version    1.0.0
    * @package    pyCommom
    * @subpackage pyCommom
    * @author     Alcindo Schleder <alcindoschleder@gmail.com>
    * @copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""
class TBaseClass:
    
    def __init__(self):
        self._result = self._setDefault()
    
    def _setDefault(self):
        return {
            "data": {},
            "state": {
                "sttCode": 200,
                "sttMsgs": ''
            }
        }

    def _isValid(self, value: dict = None):
        return bool((value.get("data")) and 
            (value.get("state")) and 
            (value["state"].get(["sttCode"])) and 
            (value["state"].get(["sttMsgs"])))

    @property
    def result(self):
        return self._result
    
    @property
    def resultStatusCode(self):
        return self._result["state"]["sttCode"]

    @property
    def resultStatusMessage(self):
        return self._result["state"]["sttMsg"]

    @property
    def resultData(self):
        return self._result["data"]
        
    @result.setter
    def result(self, value: dict = None):
        if ((value) and (self._isValid(value))):
            self._result = value
        else:
            self._result = self._setDefault()

    @resultStatusCode.setter
    def resultStatusCode(self, value: int):
        self.result['state']['sttCode'] = value

    @resultStatusMessage.setter
    def resultStatusMessage(self, value: str):
        self.result['state']['sttMsgs'] = value

    @resultData.setter
    def resultData(self, value):
        self._result["data"] = value

