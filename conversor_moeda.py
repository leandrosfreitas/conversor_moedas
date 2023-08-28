from forex_python.converter import CurrencyRates

def converter_moeda(valor, moeda_origem, moeda_destino):
    c = CurrencyRates()
    resultado = c.convert(moeda_origem, moeda_destino, valor)
    return resultado

valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (código da moeda): ").upper()
moeda_destino = input("Digite a moeda de destino (código da moeda): ").upper()

resultado = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"{valor} {moeda_origem} equivalem a {resultado} {moeda_destino}")