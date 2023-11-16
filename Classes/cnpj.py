from .documento import Documento

class Cnpj(Documento):
    def __init__(self, numeroDoDocumento):
        
        super().__init__(numeroDoDocumento)
        self.Tipo = "Cnpj"
        self.TamanhoMaximo = 14
        self.digito1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self.digito2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def ObterDocumentoFormatado(self):
        return "{:02d}.{:03d}.{:03d}/{:04d}-{:02d}".format(
            int(self.numeroDoDocumento[0:2]),
            int(self.numeroDoDocumento[2:5]),
            int(self.numeroDoDocumento[5:8]),
            int(self.numeroDoDocumento[8:12]),
            int(self.numeroDoDocumento[12:14])
        )
