
from enum import Enum
import re


class Pessoa:
    def __init__(self, nome, renda):
        self.nome = nome
        self.renda = renda

    # Abstract Method...
    def calcular_imposto():
        pass

class TipoPessoa(Enum):
    PF = 1
    PJ = 2
   

class PessoaFactory:
    @staticmethod
    def create(tipo_pessoa):
        if tipo_pessoa == TipoPessoa.PF:
            return PessoaFisica('Lucas Bogo', 1500)

        if tipo_pessoa == TipoPessoa.PJ:
            return PessoaJuridica('Elon Musk', 2010)

class PessoaFisica(Pessoa):
    # Tentativa definir dados cpf só para PF
    """ def __init__(self, cpf): 
        self.cpf = cpf """

    def calcular_imposto(self):
         return 0.25 * self.renda 
         
 
class PessoaJuridica(Pessoa):
    # Tentativa definir dados cnpj só para PJ
    """ def __init__(self, cnpj):
        self.cnpj = cnpj """

    def calcular_imposto(self):
       return 0.15 * self.renda 
       


if __name__ == '__main__':

    pf = PessoaFactory.create(TipoPessoa.PF)
    pj = PessoaFactory.create(TipoPessoa.PJ)

    pf.calcular_imposto()
    pj.calcular_imposto() 

    print(f'{pf.nome} Deve pagar ao governo: ', pf.calcular_imposto())
    print(f'{pj.nome} Deve pagar ao governo: ', pj.calcular_imposto())