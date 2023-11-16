from .documento import Documento
class TituloEleitor(Documento):
    def __init__(self, numeroDoDocumento):
        super().__init__(numeroDoDocumento)
        self.Tipo = "TituloEleitor"
        self.TamanhoMaximo = 12
        self.digito1 = [2, 3, 4, 5, 6, 7, 8, 9]
        self.digito2 = [7, 8, 9]

    def CalcularDigitoVerificador(self):
        if len(self.numeroDoDocumento) > self.TamanhoMaximo:
            raise ValueError(f"Documento deve conter {self.TamanhoMaximo} digitos.")

        uf = self.numeroDoDocumento[8:]
        documento = self.numeroDoDocumento
        soma = 0

        for i in range(len(self.digito1)):
            soma += int(documento[i]) * self.digito1[i]

        resto = soma % 11
        digito = "0" if resto == 10 else str(resto)

        documento += digito

        soma = 0
        ultimos_tres_digitos = documento[8:]

        for i in range(len(self.digito2)):
            soma += int(ultimos_tres_digitos[i]) * self.digito2[i]

        resto = soma % 11
        digito += "0" if resto == 10 else str(resto)
        self.numeroDoDocumento += digito
        return  self.numeroDoDocumento

    def ValidarDocumento(self):
        if len(self.numeroDoDocumento) > self.TamanhoMaximo:
            raise ValueError(f"Documento deve conter {self.TamanhoMaximo} digitos.")

        uf = self.numeroDoDocumento[8:]
        documento = self.numeroDoDocumento
        soma = 0

        for i in range(len(self.digito1)):
            soma += int(documento[i]) * self.digito1[i]

        resto = soma % 11
        digito = "0" if resto == 10 else str(resto)

        documento += digito

        soma = 0
        ultimos_tres_digitos = documento[8:]

        for i in range(len(self.digito2)):
            soma += int(ultimos_tres_digitos[i]) * self.digito2[i]

        resto = soma % 11
        digito += "0" if resto == 10 else str(resto)

        return self.numeroDoDocumento.endswith(digito)

    def ObterDocumentoFormatado(self):
        return "{:03d}.{:05d}.{:02d}-{:01d}".format(
            int(self.numeroDoDocumento[0:3]),
            int(self.numeroDoDocumento[3:8]),
            int(self.numeroDoDocumento[8:10]),
            int(self.numeroDoDocumento[10])
        )
