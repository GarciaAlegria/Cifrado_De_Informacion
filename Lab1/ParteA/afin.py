# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/28/01
# Descripción: Laboratorio 1 parte A - cifrado afin
# Universidad del Valle de Guatemala
# Cifrados de Información

def cifrar_afin(mensaje, a, b):
    """Cifra un mensaje usando el cifrado afín."""
    resultado = ""
    for letra in mensaje:
        if 'A' <= letra <= 'Z':
            num = ord(letra) - ord('A')
            cifrado = (a * num + b) % 26
            resultado += chr(cifrado + ord('A'))
        elif 'a' <= letra <= 'z':
            num = ord(letra) - ord('a')
            cifrado = (a * num + b) % 26
            resultado += chr(cifrado + ord('a'))
        else:
            resultado += letra  # Mantener otros caracteres sin cambios
    return resultado

def descifrar_afin(mensaje, a, b):
    """Descifra un mensaje usando el cifrado afín."""
    # Calcular el inverso multiplicativo de 'a' (modular 26)
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    else:
        raise ValueError("La clave 'a' no tiene inverso multiplicativo (debe ser coprimo con 26).")

    resultado = ""
    for letra in mensaje:
        if 'A' <= letra <= 'Z':
            num = ord(letra) - ord('A')
            descifrado = (a_inv * (num - b)) % 26
            resultado += chr(descifrado + ord('A'))
        elif 'a' <= letra <= 'z':
            num = ord(letra) - ord('a')
            descifrado = (a_inv * (num - b)) % 26
            resultado += chr(descifrado + ord('a'))
        else:
            resultado += letra  # Mantener otros caracteres sin cambios
    return resultado

def main():
    while True:
        print("\n--- Cifrado Afín ---")
        print("1. Encriptar")
        print("2. Desencriptar")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '3':
            break

        try:
            a = int(input("Ingrese el valor de 'a' (debe ser coprimo con 26): "))
            b = int(input("Ingrese el valor de 'b': "))

            if opcion == '1':
                mensaje = input("Ingrese el mensaje: ")
                mensaje_cifrado = cifrar_afin(mensaje, a, b)
                print("Mensaje cifrado:", mensaje_cifrado)
            elif opcion == '2':
                mensaje = input("Ingrese el mensaje cifrado: ")
                mensaje_descifrado = descifrar_afin(mensaje, a, b)
                print("Mensaje descifrado:", mensaje_descifrado)
            else:
                print("Opción no válida.")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()