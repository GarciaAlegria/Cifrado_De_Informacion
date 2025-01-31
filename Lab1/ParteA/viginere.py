# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/28/01
# Descripción: Laboratorio 1 parte A - cifrado viginere
# Universidad del Valle de Guatemala
# Cifrados de Información

def vigenere_encrypt(word, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    x1, x2 = 'áéíóúü', 'aeiouu'
    proc = word.strip().translate(str.maketrans(x1, x2))
    key2 = (key * (len(proc) // len(key))) + key[:len(proc) % len(key)]
    newW = ""
    
    for c, c2 in zip(proc.lower(), key2.lower()):
        if c in alpha:
            newW += alpha[((alpha.index(c) + alpha.index(c2)) % len(alpha))]
        else:
            newW += c
    
    return newW

def vigenere_decrypt(word, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    key2 = (key * (len(word) // len(key))) + key[:len(word) % len(key)]
    newW = ""
    
    for c, c2 in zip(word.lower(), key2.lower()):
        if c in alpha:
            newW += alpha[((alpha.index(c) - alpha.index(c2)) % len(alpha))]
        else:
            newW += c
    
    return newW.capitalize()

def main():
    flag = True
    while flag:
        try:
            print("\nMenú (Cifrado Vigenere)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
            opt = int(input("\nIngrese una opción: "))
            
            if opt == 1:
                word = input("Palabra a encriptar: ")
                key = input("Ingrese clave: ")
                print("\nPalabra encriptada:", vigenere_encrypt(word, key))
            elif opt == 2:
                word = input("Palabra a desencriptar: ")
                key = input("Ingrese clave: ")
                print("\nPalabra desencriptada:", vigenere_decrypt(word, key))
            elif opt == 3:
                flag = False
                print()
            else:
                print("La opción ingresada no existe")
        except:
            print("Ha ocurrido un error con la opción ingresada")

if __name__ == "__main__":
    main()
