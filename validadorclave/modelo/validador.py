from abc import ABC,abstractmethod
from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, \
    NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada:int):
        self.longitud_esperada=longitud_esperada

    @abstractmethod
    def es_valida(self,clave:str)->bool:
        self.clave:clave

    def validar_longitud(self, clave:str)->bool:
        self.clave=clave
        if self.longitud_esperada>=self.clave:
            raise NoCumpleLongitudMinimaError(clave)

    def contiene_mayuscula(self, clave:str)->bool:
        self.clave=clave
        for i in self.clave:
            if not any (i.isupper()):
                raise NoTieneLetraMayusculaError(clave)

    def contiene_minuscula(self, clave:str)->bool:
        self.clave=clave
        for i in self.clave:
            if not any (i.islower()):
                raise NoTieneLetraMinusculaError(clave)

    def contiene_numero(self, clave:str)->bool:
        self.clave=clave
        for i in self.clave:
            if not any (i.isdigit()):
                raise NoTieneNumeroError(clave)

    def es_valida(self, clave:str)->bool:
        self.clave=clave

class Validador:
    def __init__(self, regla:ReglaValidacion):
        self.regla=regla

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self,clave:str)->bool:
        self.clave=clave
        if not any("@","_","#","$","%") in self.clave:
                raise NoTieneCaracterEspecialError(clave)
        
    def es_valida(self, clave: str) -> bool:
        super().es_valida(clave)
        self.validar_longitud(clave)
        self.contiene_mayuscula(clave)
        self.contiene_minuscula(clave)
        self.contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self,clave:str)->bool:
        self.clave=clave
        for i in self.clave:
            if not i.find("calisto"):
                if i.isupper<2:
                    raise NoTienePalabraSecretaError(clave)
                
    def es_valida(self, clave: str) -> bool:
        super().es_valida(clave)
        self.validar_longitud(clave)
        self.contiene_numero(clave)
        self.contiene_calisto(clave)