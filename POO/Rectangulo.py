class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def calcArea(self):
        return self._base * self._altura

    def __str__(self):
        return f"Rectangulo \n" \
               f"Altura: {self._altura} \n" \
               f"Base: {self._base} \n" \
               f"Area: {self.calcArea()} metros cuadrados"


if __name__ == '__main__':
    recUno = Rectangulo(4, 2)
    print(recUno.__str__())
