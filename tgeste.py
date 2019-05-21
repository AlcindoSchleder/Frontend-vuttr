class moeda:

    def __init__(self):
        self._symbol = 'R$'
        self._valor = 0


class moeda10(moeda):
    def _init__(self):
        super(moeda10, self).__init__(self)
        self._valor = 10

    @property
    def valor(self):
        return self._valor

    @property
    def symbol(self):
        return self._symbol

    @valor.setter
    def valor(self, value):
        self._valor = value
