def es_palindromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]

palabra_ejemplo = "reconocer"
if es_palindromo(palabra_ejemplo):
  print("Es un palíndromo.")
else:
  print("No es un palíndromo.")
