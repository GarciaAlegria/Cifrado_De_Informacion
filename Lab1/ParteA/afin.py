# Autor: Abner Ivan Garcia Alegria - 21285
# Fecha: 2024/28/01
# Descripción: Laboratorio 1 parte A - cifrado afin
# Universidad del Valle de Guatemala
# Cifrados de Información

def clean_text(texto):
    """Limpia el texto dejando solo letras del alfabeto español en minúsculas."""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    texto = texto.lower()
    return ''.join(c for c in texto if c in alfabeto)

def cifrar_afin(mensaje, a, b):
    """Cifra un mensaje usando el cifrado afín con alfabeto español."""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje = clean_text(mensaje)
    resultado = ""
    
    for letra in mensaje:
        if letra in alfabeto:
            pos = alfabeto.index(letra)
            nueva_pos = (a * pos + b) % 27
            resultado += alfabeto[nueva_pos]
            
    return resultado

def descifrar_afin(mensaje, a, b):
    """Descifra un mensaje usando el cifrado afín con alfabeto español."""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje = clean_text(mensaje)
    
    # Calcular el inverso multiplicativo de 'a' (modulo 27)
    for i in range(27):
        if (a * i) % 27 == 1:
            a_inv = i
            break
    else:
        raise ValueError("La clave 'a' no tiene inverso multiplicativo (debe ser coprimo con 27)")
    
    resultado = ""
    for letra in mensaje:
        if letra in alfabeto:
            pos = alfabeto.index(letra)
            nueva_pos = (a_inv * (pos - b)) % 27
            resultado += alfabeto[nueva_pos]
            
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
            a = int(input("Ingrese el valor de 'a' (debe ser coprimo con 27): "))
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