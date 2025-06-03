


from base import Funcionario_CLT, Funcionario_PJ, ProdutoInternacional, ProdutoNacional


produto_1 = ProdutoNacional('Computador', 5000.0, 20)
produto_2 = ProdutoInternacional('Mouse', 30.00, 10, 0.5)
produto_3 = ProdutoNacional('Teclado', 100.00, 20)
produto_4 = ProdutoNacional('Cadeira Gamer', 1000.0, 20)
produto_5 = ProdutoInternacional('Monitor Duplo', 3000.0, 10, 0.9)
produto_6 = ProdutoNacional('Headset', 450.0, 20)

produto_1.exibir_detalhes()
produto_1.preço_final()
produto_1.emitir_nota()
produto_1.repor_estoque(8)
produto_1.vender_estoque(12)

produto_2.exibir_detalhes()
produto_2.preço_final()
produto_2.emitir_nota()
produto_2.repor_estoque(10)
produto_2.vender_estoque(2)

produto_3.exibir_detalhes()
produto_3.preço_final()
produto_3.emitir_nota()
produto_3.repor_estoque(5)
produto_3.vender_estoque(7)

produto_4.exibir_detalhes()
produto_4.preço_final()
produto_4.emitir_nota()
produto_4.repor_estoque(100)
produto_4.vender_estoque(20)

produto_5.exibir_detalhes()
produto_5.preço_final()
produto_5.emitir_nota()
produto_5.repor_estoque(9)
produto_5.vender_estoque(3)

produto_6.exibir_detalhes()
produto_6.preço_final()
produto_6.emitir_nota()
produto_6.repor_estoque(1)
produto_6.vender_estoque(24)

print('\n' + '-'*50)
print('FOLHA DE PAGAMENTO'.center(50))
print('-'*50)

f1_clt = Funcionario_CLT('Bianca', 3000)
print(f'\nPagamento CLT calculado para {f1_clt.nome}, R$ {f1_clt.calcular_pagamento():.2f}/mês')
f2_pj = Funcionario_PJ('Gabriel', 220, 22.0)
print(f'Pagamento PJ calculado para {f2_pj.nome}, R$ {f2_pj.calcular_pagamento():.2f}/mês')
f3_clt = Funcionario_CLT('Maylla', 2000)
print(f'Pagamento CLT calculado para {f3_clt.nome}, R$ {f3_clt.calcular_pagamento():.2f}/mês')
f4_pj = Funcionario_PJ('Beatriz', 220, 32.0)
print(f'Pagamento PJ calculado para {f4_pj.nome}, R$ {f4_pj.calcular_pagamento():.2f}/mês')