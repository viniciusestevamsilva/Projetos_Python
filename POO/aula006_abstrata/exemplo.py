import os
from abc import ABC, abstractmethod

# Classe abstarata
class MetodoDePagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self, valor):
        # Processa um pagamento qualquer
        pass

# Subclasse concreta
class CartaoDeCredito(MetodoDePagamento):
    
    def processar_pagamento(self, valor):
        print(f'Pagamento com cartão de crédito.')
        print(f'Valor Pago: R${valor}')

# Subclasse concreta
class Boleto(MetodoDePagamento):
    
    def processar_pagamento(self, valor):
        print(f'Emissão de boleto')
        print(f'Pgamento de R${valor}.')


os.system('cls')
# instanciando as classes filhas
pagamento_cartao = CartaoDeCredito()
pagamento_cartao.processar_pagamento(5000.00)

pagamento_boleto = Boleto()
pagamento_boleto.processar_pagamento(500.00)