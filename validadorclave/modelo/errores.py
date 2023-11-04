class ValidadorError(Exception):
    def __init__(self, clave:str):
        self.clave=clave

class NoCumpleLongitudMinimaError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no cumple con la longitud minima"

class NoTieneLetraMayusculaError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no tiene letra mayuscula"

class NoTieneLetraMinusculaError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no tiene letra minuscula"

class NoTieneNumeroError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no tiene numero"

class NoTieneCaracterEspecialError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no tiene caracteres especiales"

class NoTienePalabraSecretaError(ValidadorError):
    def __init__(self,clave):
        super().__init__(clave)

    def __str__(self):
        return f"La clave {self.clave} no tiene la palabra secreta correcta"