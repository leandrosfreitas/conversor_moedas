### Escreva uma sequência de operações em python que converta um valor em real para dólar -> 1 dol = 4,75 real
valor_real = float(input("Digite um valor em R$: "))

moeda = 0
while moeda <= 0 or moeda > 3:
  moeda = int(input('''
Escolha um número que corresponda o tipo da moeda para conversão:
(1) - DOLAR [USD]
(2) - EURO [EUR]
(3) - LIBRA [GBP]
'''))


valor_dolar = 4.95
valor_euro = 5.28
valor_libra = 6.19

def realpdolar(valor_real, valor_dolar):
  return valor_real * valor_dolar
def realpeuro(valor_real, valor_euro):
  return valor_real * valor_euro
def realplibra(valor_real, valor_libra):
  return valor_real * valor_libra

if moeda == 1:
  resultado_dolar = realpdolar(valor_real, valor_dolar)
  print(f"O valor em dolar é US {resultado_dolar:.2f}")
elif moeda == 2:
  resultado_euro = realpeuro(valor_real, valor_euro)
  print(f"O valor em euro é € {resultado_euro:.2f}")
elif moeda == 3:
  resultado_libra = realplibra(valor_real, valor_libra)
  print(f"O valor em libra é £ {resultado_libra:.2f}")