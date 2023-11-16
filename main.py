from Classes.documento import Documento
from Classes.cnpj import Cnpj
from Classes.cpf import Cpf
from Classes.inscricaoEstadualParana import InscricaoEstadualParana
from Classes.pis import Pis
from Classes.tituloEleitor import TituloEleitor
from typing import Callable
import re

class Main:

    @staticmethod
    def testar(numeroDoDocumento, tipoDocumento=None):
        numeroDoDocumento = re.sub(r'[./-]', '', numeroDoDocumento).strip()

        DocumentosValidados = {
            "9": lambda value: Cpf(value),
            "11": lambda value: Cpf(value),
            "Cpf": lambda value: Cpf(value),
            "12": lambda value: Cnpj(value),
            "14": lambda value: Cnpj(value),
            "Cnpj": lambda value: Cnpj(value),
            "8": lambda value: InscricaoEstadualParana(value),
            "10": lambda value: InscricaoEstadualParana(value),
            "InscricaoEstadualParana": lambda value: InscricaoEstadualParana(value),
            "Pis": lambda value: Pis(value),
            "Titulo": lambda value: TituloEleitor(value),
        }

        tipoDeBusca = str(len(numeroDoDocumento)) if tipoDocumento is None else tipoDocumento

        if tipoDeBusca in DocumentosValidados:
            documento: Callable[[str], Documento] = DocumentosValidados[tipoDeBusca]
            documento = documento(numeroDoDocumento)

            if len(documento.numeroDoDocumento) < documento.TamanhoMaximo:
                documento.CalcularDigitoVerificador()
            else:
                print(f"{documento.Tipo} válido: {documento.ValidarDocumento()}")

            print(f"{documento.Tipo}: {documento.ObterDocumentoCompleto()}")
            print(f"{documento.Tipo} formatado: {documento.ObterDocumentoFormatado()}")
        else:
            print(f"Não há classe associada ao tipo de documento {tipoDocumento}")

main_instance = Main()
main_instance.testar("568.894.680")
