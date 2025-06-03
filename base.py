
from abc import ABC, abstractmethod


class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
        self.preco_final = preço
  
    def exibir_detalhes(self):
        print(f'\n{self.nome}, R$ {self.preço:.2f}, {self.estoque} unidades em estoque')

    def preço_final(self):
        print(f'Preço Final= R$ {self.preco_final:.2f}')

    def emitir_nota(self):
        print("Nota Fiscal gerada para", self.nome)

    def repor_estoque(self, quantidade):
       self.estoque += quantidade
       print('Repor estoque em ', quantidade, 'unidades')

    def vender_estoque(self, quantidade):
        if quantidade > self.estoque:
            print('Venda indisponivel. Quantidade em estoque insuficiente')
        else:
            self.estoque -= quantidade
            print(f'Venda realizada de {quantidade} unidades. Estoque Atual:{self.estoque}')

        
class ProdutoNacional(Produto):
    def emitir_nota(self):
        print("Nota fiscal Nacional gerada.")

class ProdutoInternacional(Produto):
    def __init__(self, nome, preço, estoque, taxa_de_importacao):
        super().__init__(nome, preço, estoque)
        self.taxa_de_importacao = taxa_de_importacao
        self.preco_final = preço + (preço * taxa_de_importacao)


    def exibir_detalhes(self):
       print(f"\n{self.nome}, R$ {self.preço:.2f}, {self.estoque} un em estoque, aplicada a taxa de importação de {self.taxa_de_importacao}%")

    def preço_final(self):
        print(f'Preço Final= R$ {self.preco_final:.2F}')
    
    def emitir_nota(self):
        print("Nota fiscal de importação gerada com taxa aplicada.")

        
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_pagamento(self):
        pass

    
class Funcionario_CLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
    def calcular_pagamento(self):
        return self.salario
    
class Funcionario_PJ(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora
    
    

