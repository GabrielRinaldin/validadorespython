class Documento:
    Tipo = "Documento"
    numeroDoDocumento = ""
    digito1 = []
    digito2 = []
    TamanhoMaximo = 0
    digitosValidados = ""

    def __init__(self, numeroDoDocumento):
        self.numeroDoDocumento = numeroDoDocumento
        self.digitosValidados = ""
        self.digito1 = []
        self.digito2 = []

    def CalcularDigitoVerificador(self):
        if len(self.numeroDoDocumento) > self.TamanhoMaximo:
            raise ValueError(f"Documento deve conter {self.TamanhoMaximo} digitos.")

        documento = self.numeroDoDocumento

        soma = 0

        for i in range(len(self.digito1)):
            soma += int(documento[i]) * self.digito1[i]

        resto = soma % 11

        digito = "0" if resto < 2 else str(11 - resto)

        documento += str(digito)

        if len(self.digito2) > 0:
            soma = 0

            for i in range(len(self.digito2)):
                soma += int(documento[i]) * self.digito2[i]

            resto = soma % 11
            digito += "0" if resto < 2 else str(11 - resto)

        self.numeroDoDocumento += str(digito)
        self.digitosValidados = digito;
        return self.numeroDoDocumento

    def ValidarDocumento(self):
        if len(self.numeroDoDocumento) != self.TamanhoMaximo:
            raise ValueError(f"Documento deve conter {self.TamanhoMaximo} digitos.")

        soma = 0

        for i in range(len(self.digito1)):
            soma += int(self.numeroDoDocumento[i]) * self.digito1[i]

        resto = soma % 11
        digito = "0" if resto < 2 else str(11 - resto)

        if len(self.digito2) > 0:
            soma = 0

            for i in range(len(self.digito2)):
                soma += int(self.numeroDoDocumento[i]) * self.digito2[i]

            resto = soma % 11
            digito += "0" if resto < 2 else str(11 - resto)

        return self.numeroDoDocumento.endswith(digito)

    def ObterDocumentoCompleto(self):
        return self.numeroDoDocumento

    def ObterDocumentoFormatado(self):
        return self.numeroDoDocumento

    def ObterDigitosVerificadores(self):
        return self.digitosValidados
