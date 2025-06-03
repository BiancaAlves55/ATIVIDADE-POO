from base import ProdutoNacional
from base import ProdutoInternacional, Funcionario_PJ, Funcionario_CLT


produto_1 = ProdutoNacional('Computador', 5000.00, 20)
produto_2 = ProdutoInternacional('Mouse', 30.00, 10, 0.5)
produto_3 = ProdutoNacional('Teclado', 100.00, 20)

produto_1.exibir_detalhes()
produto_1.preço_final()
produto_1.emitir_nota()
produto_1.repor_estoque(10)
produto_1.vender_estoque(2)

produto_2.exibir_detalhes()
produto_2.preço_final()
produto_2.emitir_nota()
produto_2.repor_estoque(0)
produto_2.vender_estoque(11)

produto_3.exibir_detalhes()
produto_3.preço_final()
produto_3.emitir_nota()
produto_3.repor_estoque(3)
produto_3.vender_estoque(17)

f_clt = Funcionario_CLT('Bianca', 3000)
print(f'\nPagamento CLT calculado para {f_clt.nome}, R$ {f_clt.calcular_pagamento():.2f}/mês')

f_pj = Funcionario_PJ('Gabriel', 220, 22.0)
print(f'Pagamento PJ calculado para {f_pj.nome}, R$ {f_pj.calcular_pagamento():.2f}/mês')

