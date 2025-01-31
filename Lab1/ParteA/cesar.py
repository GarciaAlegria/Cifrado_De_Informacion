# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/28/01
# Descripción: Laboratorio 1 parte A - cifrado cesar
# Universidad del Valle de Guatemala
# Cifrados de Información

import string

def normalize_text(text):
    """Reemplaza caracteres acentuados por sus equivalentes sin acento."""
    a, b = 'áéíóúü', 'aeiouu'
    return text.strip().translate(str.maketrans(a, b)).lower()

def cesar_encriptar(text, desplazamiento):
    """Cifra un texto usando el cifrado César con el desplazamiento dado."""
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    text = normalize_text(text)
    resultado = ""
    
    for char in text:
        if char in alphabet:
            nuevo_indice = (alphabet.index(char) + desplazamiento) % len(alphabet)
            resultado += alphabet[nuevo_indice]
        else:
            resultado += char
    
    return resultado

def cesar_desencriptar(text, desplazamiento):
    """Descifra un texto cifrado con el cifrado César usando el desplazamiento dado."""
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""
    
    for char in text:
        if char in alphabet:
            nuevo_indice = (alphabet.index(char) - desplazamiento) % len(alphabet)
            resultado += alphabet[nuevo_indice]
        else:
            resultado += char
    
    return resultado.capitalize()

def main():
    while True:
        print("\nMenú (Cifrado César)\n1) Encriptar\n2) Desencriptar\n3) Salir")
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                texto = input("Palabra a encriptar: ")
                desplazamiento = int(input("Desplazamiento: "))
                print("\nPalabra encriptada:", cesar_encriptar(texto, desplazamiento))
            elif opcion == 2:
                texto = input("Palabra a desencriptar: ")
                desplazamiento = int(input("Desplazamiento: "))
                print("\nPalabra desencriptada:", cesar_desencriptar(texto, desplazamiento))
            elif opcion == 3:
                break
            else:
                print("La opción ingresada no existe")
        except ValueError:
            print("Ha ocurrido un error con la opción ingresada")

if __name__ == "__main__":
    main()