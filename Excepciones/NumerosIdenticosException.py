class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje  # En la clase padre tenemos un mensaje, y lo asigno al mensaje que paso por parametro
