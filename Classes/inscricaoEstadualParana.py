from .documento import Documento

class InscricaoEstadualParana(Documento):
    def __init__(self, numeroDoDocumento):
        super().__init__(numeroDoDocumento)
        self.Tipo = "InscricaoEstadualParana"
        self.TamanhoMaximo = 10
        self.digito1 = [3, 2, 7, 6, 5, 4, 3, 2]
        self.digito2 = [4, 3, 2, 7, 6, 5, 4, 3, 2]

    def ObterDocumentoFormatado(self):
        return "{:08d}-{:02d}".format(
            int(self.numeroDoDocumento[0:8]),
            int(self.numeroDoDocumento[8:10])
        )
