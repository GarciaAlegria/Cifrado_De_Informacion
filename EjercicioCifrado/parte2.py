# 1. Conversión de Palabras en Texto ASCII a Binario
def texto_a_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)



# 1. Conversión de texto a binario
texto = "Hola"
binario = texto_a_binario(texto)
print(f"Texto a Binario: {binario}")

