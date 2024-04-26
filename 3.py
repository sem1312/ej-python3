def contador(texto):
  palabras = texto.split()
  cant = len(palabras)
  return cant


texto = "Es confuso verdad? Sin embargo skibidi sigma toilet pomni"
resultado = contador(texto)
print("El texto tiene", resultado, "palabras.")
