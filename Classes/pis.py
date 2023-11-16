from .documento import Documento

class Pis(Documento):
    def __init__(self, numeroDoDocumento):
        super().__init__(numeroDoDocumento)
        self.Tipo = "Pis"
        self.TamanhoMaximo = 11
        self.digito1 = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def ObterDocumentoFormatado(self):
        return "{:03d}.{:05d}.{:02d}-{:01d}".format(
            int(self.numeroDoDocumento[0:3]),
            int(self.numeroDoDocumento[3:8]),
            int(self.numeroDoDocumento[8:10]),
            int(self.numeroDoDocumento[10])
        )
