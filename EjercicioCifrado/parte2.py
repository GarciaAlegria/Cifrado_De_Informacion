# 1. Conversión de Palabras en Texto ASCII a Binario
def ascii_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# 2. BASE64 a BINARIO
def base64_a_binario(texto):
  """Convierte texto BASE64 a binario."""
  base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  binario = ""
  for caracter in texto:
    if caracter in base64_chars:
      indice = base64_chars.index(caracter)
      binario += bin(indice)[2:].zfill(6)  # Convertir a binario y rellenar con ceros
  return binario

# 3. # BINARIO a BASE64
def binario_a_base64(binario):
  """Convierte binario a BASE64."""
  base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  base64 = ""
  for i in range(0, len(binario), 6):
    bloque = binario[i:i+6]
    if len(bloque) < 6:
      bloque += "0" * (6 - len(bloque))  # Rellenar con ceros si es necesario
    indice = int(bloque, 2)
    base64 += base64_chars[indice]
  return base64

# 4. Convertir BINARIO a ASCII
def binary_to_ascii(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)

# 5. BASE64 a ASCII (pasando por binario)
def base64_a_ascii(texto):
  """Convierte BASE64 a ASCII pasando por binario."""
  binario = base64_a_binario(texto)
  ascii = binary_to_ascii(binario)
  return ascii

# 6. XOR a un BINARIO
def xor_binario(binario1, binario2):
  """Aplica XOR a dos cadenas binarias."""
  resultado = ""
  for i in range(len(binario1)):
    if binario1[i] == binario2[i]:
      resultado += "0"
    else:
      resultado += "1"
  return resultado

  # 7. # Generar llaves dinámicas (utilizar ASCII)
def generar_llave_dinamica(longitud):
  """Genera una llave dinámica de la longitud especificada utilizando caracteres ASCII."""
  import random
  llave = ''.join(chr(random.randint(33, 126)) for _ in range(longitud))
  return llave

# 8. # Generar un nuevo cypher en ASCII con una llave k de tamaño fijo
def cifrar_ascii_fijo(texto, llave):
  """Cifra un texto ASCII con una llave de tamaño fijo."""
  texto_binario = ascii_to_binary(texto)
  llave_binario = ascii_to_binary(llave)
  longitud_llave = len(llave_binario)
  cifrado_binario = ""
  for i in range(0, len(texto_binario), longitud_llave):
    bloque = texto_binario[i:i+longitud_llave]
    cifrado_binario += xor_binario(bloque, llave_binario)
  return binary_to_ascii(cifrado_binario)


# Ejemplo de uso
if __name__ == "__main__":
    text = "si"
    llave_fija = "CLAVE"
    llave_dinamica = generar_llave_dinamica(len(text))


    print("********************** PARTE 2 ***********************")
    print("-------------------------------------------------------")
    print("ASCII a BINARIO:", ascii_to_binary(text))
    print("-------------------------------------------------------")
    print("BASE64 a BINARIO:", base64_a_binario("SGVsbG8="))
    print("-------------------------------------------------------")
    print("BINARIO a BASE64:", binario_a_base64("0111001101101001"))
    print("-------------------------------------------------------")
    print("BINARIO a ASCII:", binary_to_ascii("0111001101101001"))
    print("-------------------------------------------------------")
    print("BASE64 a ASCII:", base64_a_ascii("SGVsbG8="))
    print("-------------------------------------------------------")
    print("XOR binario:", xor_binario("101010", "010101"))
    print("-------------------------------------------------------")
    print("Llave dinámica:", generar_llave_dinamica(8))
    print("-------------------------------------------------------")
    print("Cifrado ASCII fijo:", cifrar_ascii_fijo(text, llave_fija))
    print("-------------------------------------------------------")


