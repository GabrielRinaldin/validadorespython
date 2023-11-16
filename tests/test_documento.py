from Classes.documento import Documento;
from Classes.cpf import Cpf;
from Classes.cnpj import Cnpj;
from Classes.inscricaoEstadualParana import InscricaoEstadualParana;
from Classes.pis import Pis;
from Classes.tituloEleitor import TituloEleitor;
from typing import Callable, Dict
import re
import pytest

# //coverage run -m pytest
#coverage report -m

    # /*Testes De Validação Sucedido*/

def testPisValido():
    
    numeroDoDocumento = "711.46595.16-4"
    tipoDocumento = "Pis"
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
            assert documento.ValidarDocumento()

def testCpfValido():
    numeroDoDocumento = "568.894.680-66"
    tipoDocumento = None
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
            assert documento.ValidarDocumento()

def testCnpjValido():
    numeroDoDocumento = "01.072.596/0001-06"
    tipoDocumento = None
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
            assert documento.ValidarDocumento()

def testInscricaoEstadualValido():
    numeroDoDocumento = "285.93003-00";
    tipoDocumento = None
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
            assert documento.ValidarDocumento()

def testTituloValido():
    numeroDoDocumento = "287370331201"
    tipoDocumento =  "Titulo"
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
            assert documento.ValidarDocumento()

# /*Testes De Validação sem Sucesso*/

def testPisInvalido():
    
    numeroDoDocumento = "358.39010.84-6"
    tipoDocumento = "Pis"
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
            assert not documento.ValidarDocumento()

def testCpfInvalido():
    
    numeroDoDocumento = "511.830.300-99"
    tipoDocumento = None
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
            assert not documento.ValidarDocumento()

def testCnpjInvalido():
    
    numeroDoDocumento = "71.723.756/0001-01"
    tipoDocumento = None
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
            assert not documento.ValidarDocumento()

def testInscricaoEstadualInvalido():
    
    numeroDoDocumento = "852.30886-24"
    tipoDocumento = None
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
            assert not documento.ValidarDocumento()

def testTituloInvalido():
    
    numeroDoDocumento = "550681720189"
    tipoDocumento = "Titulo"
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
            assert not documento.ValidarDocumento()

#    /*Testes para Calcular Digito Verificador*/

def testCpfDigitoVerificador():
    
    numeroDoDocumento = "568.894.680"
    tipoDocumento = None
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
            assert len(documento.CalcularDigitoVerificador()) == documento.TamanhoMaximo
            assert documento.ObterDocumentoCompleto()
            assert documento.ObterDocumentoFormatado()
            assert documento.ObterDigitosVerificadores()

def testPisVerificador():
    
    numeroDoDocumento = "163.43757.13"
    tipoDocumento = "Pis"
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
            assert len(documento.CalcularDigitoVerificador()) == documento.TamanhoMaximo
            assert documento.ObterDocumentoCompleto()
            assert documento.ObterDocumentoFormatado()

def testCnpjVerificador():
    
    numeroDoDocumento = "96.875.226/0001"
    tipoDocumento = None
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
            assert len(documento.CalcularDigitoVerificador()) == documento.TamanhoMaximo
            assert documento.ObterDocumentoCompleto()
            assert documento.ObterDocumentoFormatado()

def testInscricaoEstadualVerificador():
    
    numeroDoDocumento = "862.02690"
    tipoDocumento = None
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
            assert len(documento.CalcularDigitoVerificador()) == documento.TamanhoMaximo
            assert documento.ObterDocumentoCompleto()
            assert documento.ObterDocumentoFormatado()

def testTituloVerificador():
    
    numeroDoDocumento = "1846567819"
    tipoDocumento = "Titulo"
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
            assert len(documento.CalcularDigitoVerificador()) == documento.TamanhoMaximo
            assert documento.ObterDocumentoCompleto()
            assert documento.ObterDocumentoFormatado()

# Lançar exception
def testTituloException():
    
    numeroDoDocumento = "6248634401162"
    tipoDocumento = "Titulo"
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
            with pytest.raises(ValueError, match=f"Documento deve conter {documento.TamanhoMaximo} digitos."):
                documento.CalcularDigitoVerificador()

def testTituloException2():
    
    numeroDoDocumento = "6248634401162"
    tipoDocumento = "Titulo"
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
            with pytest.raises(ValueError, match=f"Documento deve conter {documento.TamanhoMaximo} digitos."):
                documento.ValidarDocumento()

def testCpfException():
    
    numeroDoDocumento = "4334.672.050-11"
    tipoDocumento = None
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
            with pytest.raises(ValueError, match=f"Documento deve conter {documento.TamanhoMaximo} digitos."):
                documento.ValidarDocumento()

def testCnpjException():
    
    numeroDoDocumento = "049.904.354/0001-35"
    tipoDocumento = "Cnpj"
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
            with pytest.raises(ValueError, match=f"Documento deve conter {documento.TamanhoMaximo} digitos."):
                documento.CalcularDigitoVerificador()

def testClasseDocumento():
    numeroDoDocumento = "049.904.354/0001-35"
    tipoDocumento = "Cnpj"
    numeroDoDocumento = re.sub(r'[./-]', '', numeroDoDocumento).strip()

    documento = Documento(numeroDoDocumento)
    assert documento.ObterDocumentoFormatado()