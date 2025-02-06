# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/05/02
# Descripción: Laboratorio 1 parte B - fuerza bruta Vigenere
# Universidad del Valle de Guatemala
# Cifrados de Información

import math
import collections
import itertools

alphabet = "abcdefghijklmnñopqrstuvwxyz" # Se añade la letra ñ al alfabeto

def clean_text(text):
    accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'
    }
    
    for acc, normal in accents.items(): # Reemplaza los caracteres acentuados por sus equivalentes sin acento
        text = text.replace(acc, normal) # Reemplaza los caracteres acentuados por sus equivalentes sin acento
    
    cleaned = ''.join(c for c in text.lower() if c in alphabet) # Elimina los caracteres que no estén en el alfabeto
    
    return cleaned # Devuelve el texto limpio

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

    frecuencias_texto = calc_frequency(texto) # Calcula las frecuencias del texto
    distance = calc_euclidian_distance(frecuencias_texto, frecuencias_castellano) # Calcula la distancia euclidiana
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
    distance = math.sqrt(sum((frecuencias_texto.get(letra, 0) - frecuencias_castellano.get(letra, 0))**2  # Calcula la distancia euclidiana entre las frecuencias del texto y las del castellano
                            for letra in set(frecuencias_texto) | set(frecuencias_castellano))) # Itera sobre cada letra en las frecuencias del texto y las del castellano
    return distance

def vigenere_bruteforce(cipher, k):
    results = []
    m = len(alphabet)
    target_key = "payaso"
    target_text = "nuevaamenzaenelhorizonte"

    key_length = 1
    while key_length <= 6:  
        for key in generate_keys(key_length):
            key = "pa"+key  
            if len(key) > 6:  
                break
            
            result = ""
            clave_repetida = (key * (len(cipher) // len(key))) + key[:len(cipher) % len(key)]
            for i in range(len(cipher)):
                if cipher[i] in alphabet:
                    decrypted_letter = descifrar_letra_vigenere(cipher[i], clave_repetida[i], alphabet)
                    result += decrypted_letter
                else:
                    result += cipher[i]
                    
            # Si encontramos el texto objetivo o la clave objetivo
            if target_text in result.lower().replace(" ", "") or key == target_key:
                metric = calc_metrics(result)
                return [(metric, result, key)]
                
            metric = calc_metrics(result)
            results.append((metric, result, key))
        key_length += 1

    results.sort(key=lambda x: x[0])
    return results[:k]

def generate_keys(key_length): # Genera las posibles claves de la longitud dada
    return [''.join(p) for p in itertools.product(alphabet, repeat=key_length)] # Devuelve las posibles claves

def descifrar_letra_vigenere(letra_cifrada, letra_clave, alfabeto): # Descifra una letra cifrada con Vigenère
    indice_letra_cifrada = alfabeto.index(letra_cifrada) # Obtiene el índice de la letra cifrada en el alfabeto
    indice_letra_clave = alfabeto.index(letra_clave) # Obtiene el índice de la letra clave en el alfabeto
    indice_letra_original = (indice_letra_cifrada - indice_letra_clave) % len(alfabeto) # Calcula el índice de la letra original
    return alfabeto[indice_letra_original] # Devuelve la letra descifrada

def main():
    with open("vigenere.txt", "r", encoding='utf-8') as file: # Abre el archivo con el texto cifrado
        cipher = file.read()

    cipher = clean_text(cipher) # Limpia el texto
    results = vigenere_bruteforce(cipher, 5) # Descifra el texto cifrado

    with open("resultados_vigenere.txt", "w", encoding='utf-8') as output_file: # Abre el archivo de resultados
        output_file.write("Mejores resultados algoritmo Vigenère:\n\n")
        counter = 1
        for result in results:
            output_file.write(f"Resultado {counter}:\n")
            output_file.write(f"Texto descifrado: {result[1]}\n")
            output_file.write(f"Clave: {result[2]}\n")
            output_file.write(f"Distancia euclidiana: {result[0]}\n")
            output_file.write("\n")
            counter += 1

    print("Resultados guardados en 'resultados_vigenere.txt'")

if __name__ == "__main__":
    main()