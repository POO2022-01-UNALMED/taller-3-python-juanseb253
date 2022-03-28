class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1

    def getMarca(self):
        return self._marca
    def setMarca(self, mar):
        self._marca = mar

    def getCanal(self):
        return self._canal
    def setCanal(self, can):
        if self._estado == True and self._canal >= 1 and self._canal <= 120:
            self._canal = can
    def canalUp(self):
        if self._estado == True and self._canal != 120:
            self._canal += 1
    def canalDown(self):
        if self._estado == True and self._canal != 1:
            self._canal -= 1

    def getPrecio(self):
        return self._precio
    def setPrecio(self, pre):
        self._precio = pre

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, vol):
        if self._estado == True and self._volumen <= 7 and self._volumen >= 0:
            self._volumen = vol
    def volumenUp(self):
        if self._estado == True and self._volumen <=7:
            self._volumen += 1
    def volumenDown(self):
        if self._estado == True and self._volumen >= 0:
            self._volumen -= 1

    def getControl(self):
        return self._control
    def setControl(self, con):
        self._control = con
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num
    
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    def getEstado(self):
        return self._estado