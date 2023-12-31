class Aritmetica:
    """
    Doc-String -> Clase Aritmetica para realizar operaciones basicas
    """

    def __init__(self, numeroUno, numeroDos):
        self._numeroUno = numeroUno
        self._numeroDos = numeroDos

    @property
    def numeroUno(self):
        return self._numeroUno

    @numeroUno.setter
    def numeroUno(self, numeroUno):
        self._numeroUno = numeroUno

    @property
    def numeroDos(self):
        return self._numeroDos

    @numeroDos.setter
    def numeroDos(self, numeroDos):
        self._numeroDos = numeroDos

    # Metodos propios
    def sumar(self):
        return self.numeroUno + self._numeroDos

    def multiplicar(self):
        return self.numeroUno * self._numeroDos

    def restar(self):
        if self.numeroDos > self.numeroUno:
            return self.numeroDos - self.numeroUno
        else:
            return self.numeroUno - self.numeroDos

    def cociente(self):
        if self.numeroDos > self.numeroUno:
            return self.numeroDos / self.numeroUno
        else:
            return self.numeroUno / self.numeroDos


if __name__ == '__main__':
    # Instanciamos objetos de la clase Aritmetica
    ariUno = Aritmetica(1, 4)
    sum = ariUno.sumar()
    sus = ariUno.restar()
    prod = ariUno.multiplicar()
    coc = ariUno.cociente()
    print(f"El resultado de la suma es: {sum}, teniendo como operandos a {ariUno.numeroUno} y {ariUno.numeroDos}")
    print(f"El resultado de la resta es: {sus}, teniendo como operandos a {ariUno.numeroUno} y {ariUno.numeroDos}")
    print(f"El resultado de la multiplicacion es: {prod}, teniendo como operandos a {ariUno.numeroUno} y {ariUno.numeroDos}")
    print(f"El resultado de la division es: {coc}, teniendo como operandos a {ariUno.numeroUno} y {ariUno.numeroDos}")
