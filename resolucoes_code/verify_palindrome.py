# 6 - Verificando Palíndromos 🔄

palavra = input("Digite uma palavra: ").strip()
palavra_normalizada = palavra.casefold()

if palavra_normalizada == palavra_normalizada[::-1]:
	print("É um palíndromo.")
else:
	print("Não é um palíndromo.")