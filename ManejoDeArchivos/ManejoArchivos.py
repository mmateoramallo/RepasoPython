class ManejoArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def __enter__(self):
        print('Entrando al recurso'.center(50, '-'))
        self.nombreArchivo = open(self.nombreArchivo, 'r', encoding='utf8')
        return self.nombreArchivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombreArchivo: #Si se apunta a algun objeto de tipo archivo
            self.nombreArchivo.close()

