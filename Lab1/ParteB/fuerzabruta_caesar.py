# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/04/02
# Descripción: Laboratorio 1 parte B - fuerza bruta cesar
# Universidad del Valle de Guatemala
# Cifrados de Información

import math
import collections

alphabet = "abcdefghijklmnñopqrstuvwxyz" # Se añade la letra ñ al alfabeto

def clean_text(text): # Reemplaza caracteres acentuados por sus equivalentes sin acento
    accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'
    }
    
    for acc, normal in accents.items(): # Reemplaza los caracteres acentuados por sus equivalentes sin acento
        text = text.replace(acc, normal) # Reemplaza los caracteres acentuados por sus equivalentes sin acento
    
    cleaned = ''.join(c for c in text.lower() if c in alphabet) # Elimina los caracteres que no estén en el alfabeto
    
    return cleaned # Devuelve el texto limpio

def desencriptar_caesar(cipher, key): # Descifra un texto cifrado con el cifrado César usando el desplazamiento dado
    result = ""
    m = len(alphabet) # Longitud del alfabeto

    for char in cipher: # Itera sobre cada caracter del texto cifrado
        if char in alphabet: # Si el caracter está en el alfabeto
            position = alphabet.index(char) # Obtiene la posición del caracter en el alfabeto
            result += alphabet[(position - key) % m] # Obtiene el caracter descifrado y lo añade al resultado
        else:
            result += char # Si el caracter no está en el alfabeto, lo añade tal cual al resultado

    return result   

def caesar_bruteforce(cipher, k): # Realiza un ataque de fuerza bruta para descifrar un texto cifrado con el cifrado César
    results = []
    ciphertext = cipher.lower() # Convierte el texto cifrado a minúsculas

    for key in range(len(alphabet)): # Itera sobre cada posible desplazamiento
        result = desencriptar_caesar(ciphertext, key) # Descifra el texto cifrado con el desplazamiento actual
        metric = calc_metrics(result) # Calcula la métrica de distancia euclidiana
        results.append((metric, result, key)) # Añade el resultado a la lista de resultados

    results.sort(key=lambda x: x[0]) # Ordena los resultados por la métrica de distancia euclidiana

    return results[:k]

def calc_metrics(texto): # Calcula la métrica de distancia euclidiana
    frecuencias_castellano = {
        'a': 0.11525,
        'b': 0.02215,
        'c': 0.04019,
        'd': 0.05010,
        'e': 0.12181,
        'f': 0.00692,
        'g': 0.01768,
        'h': 0.00703,
        'i': 0.06247,
        'j': 0.00493,
        'k': 0.00011,
        'l': 0.04967,
        'm': 0.03157,
        'n': 0.06712,
        'ñ': 0.00311,
        'o': 0.08683,
        'p': 0.02510,
        'q': 0.00877,
        'r': 0.06871,
        's': 0.07977,
        't': 0.04632,
        'u': 0.02927,
        'v': 0.01138,
        'w': 0.00017,
        'x': 0.00215,
        'y': 0.01008,
        'z': 0.00467
    }

    texto = clean_text(texto) # Limpia el texto de caracteres no deseados
    frecuencias_texto = calc_frequency(texto) # Calcula las frecuencias de los caracteres en el texto
    distance = calc_euclidian_distance(frecuencias_texto, frecuencias_castellano) # Calcula la distancia euclidiana entre las frecuencias del texto y las del castellano

    return distance

def calc_frequency(texto): # Calcula las frecuencias de los caracteres en el texto
    total_chars = sum(1 for c in texto if c in alphabet) # Cuenta el total de caracteres en el texto
    if total_chars == 0: # Si no hay caracteres en el texto
        return collections.Counter() # Devuelve un contador vacío
        
    frecuencias = collections.Counter(c for c in texto if c in alphabet) # Cuenta las ocurrencias de cada caracter en el texto
    for char in frecuencias: # Itera sobre cada caracter en las frecuencias
        frecuencias[char] = frecuencias[char] / total_chars # Calcula la frecuencia de cada caracter
        
    return frecuencias

def calc_euclidian_distance(frecuencias_texto, frecuencias_castellano): # Calcula la distancia euclidiana entre las frecuencias del texto y las del castellano
    distance = math.sqrt(sum((frecuencias_texto.get(letra, 0) - frecuencias_castellano.get(letra, 0))**2 for letra in set(frecuencias_texto) | set(frecuencias_castellano))) # Calcula la distancia euclidiana entre las frecuencias del texto y las del castellano
    return distance # Devuelve la distancia euclidiana

def main(): # Función principal
    with open("ceasar.txt", "r", encoding='utf-8') as file: # Abre el archivo con el texto cifrado
        cipher = file.read() # Lee el texto cifrado
    
    cipher = clean_text(cipher) # Limpia el texto cifrado de caracteres no deseados
    results = caesar_bruteforce(cipher, 5) # Realiza un ataque de fuerza bruta para descifrar el texto cifrado

    # Guarda los resultados en un archivo
    with open("resultados_caesar.txt", "w", encoding='utf-8') as output_file:
        output_file.write("Mejores resultados algoritmo caesar:\n\n")
        counter = 1
        for result in results:
            output_file.write(f"Resultado {counter}, Llave {result[2]}: {result[1]}\n")
            output_file.write(f"Distancia euclidiana: {result[0]}\n")
            output_file.write("\n")
            counter += 1

    print("Resultados guardados en 'resultados_caesar.txt'")

if __name__ == "__main__":
    main()