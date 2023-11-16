from .documento import Documento

class Cpf(Documento):
    
    def __init__(self, numeroDoDocumento):
        super().__init__(numeroDoDocumento)
        self.Tipo = "Cpf"
        self.TamanhoMaximo = 11
        self.digito1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.digito2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def ObterDocumentoFormatado(self):
        return "{:03d}.{:03d}.{:03d}-{:02d}".format(
            int(self.numeroDoDocumento[0:3]),
            int(self.numeroDoDocumento[3:6]),
            int(self.numeroDoDocumento[6:9]),
            int(self.numeroDoDocumento[9:11])
        )
