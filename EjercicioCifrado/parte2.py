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



# Ejemplo de uso
if __name__ == "__main__":
    text = "si"


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


