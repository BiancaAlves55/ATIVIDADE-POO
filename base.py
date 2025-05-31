
class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
        self.preco_final = preço
  
    def exibir_detalhes(self):
        print(self.nome, self.preço, self.estoque)

    def preço_final(self):
        print('Preço Final=', self.preco_final)

    def emitir_nota(self):
        print("Nota gerada para", self.nome)

    def repor_estoque(self, repor):
       self.estoque = self.estoque + repor

    def vender_estoque(self, vender):
        self.estoque = self.estoque - vender
    
class ProdutoNacional(Produto):
    def emitir_nota(self):
        print("Nota fiscal nacional para", self.nome)

class ProdutoInternacional(Produto):
    def __init__(self, nome, preço, estoque, taxa_de_importacao):
        super().__init__(nome, preço, estoque)
        self.taxa_de_importacao = taxa_de_importacao
        self.preco_final = preço + (preço * taxa_de_importacao)


    def exibir_detalhes(self):
       print(self.nome, self.preço, self.estoque, self.taxa_de_importacao)

    def preço_final(self):
        print('Preço Final=', self.preco_final)
    
    def emitir_nota(self):
        print("Nota fiscal de importação para", self.nome, "com taxa aplicada.")

        

