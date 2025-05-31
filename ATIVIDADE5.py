from base import ProdutoNacional
from base import ProdutoInternacional

produto_1 = ProdutoNacional('Computador', 5000.00, 20)
produto_2 = ProdutoInternacional('Mouse', 30.00, 10, 0.5)
produto_3 = ProdutoNacional('Teclado', 100.00, 20)

produto_1.exibir_detalhes()
produto_1.preço_final()
produto_1.emitir_nota()
produto_1.repor_estoque()
produto_1.vender_estoque()

produto_2.exibir_detalhes()
produto_2.preço_final()
produto_2.emitir_nota()
produto_2.repor_estoque()
produto_2.vender_estoque()

produto_3.exibir_detalhes()
produto_3.preço_final()
produto_3.emitir_nota()
produto_3.repor_estoque()
produto_3.vender_estoque()

