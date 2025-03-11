# Ejercicio Block Cipher 🛠️
Este ejercicio se enfoca en comprender los fundamentos de los modos de operación en cifrados de bloque y la implementación de algoritmos de cifrado usando la librería pycryptodome.

# Competencias a Desarrollar 💡
*   Comprender el concepto de modos de operación y su importancia en los cifrados de bloque.
*   Implementar un esquema básico de cifrado y descifrado con la librería pycryptodome.
*   Analizar las diferencias al cifrar usando DES, 3DES y AES.

## Problemas a Resolver 🧠
1. **Generación de una función de cifrado y descifrado DES:**
*   Escribir una función en el lenguaje de programación que prefieran, que tome un mensaje en texto plano y lo cifre implementando el algoritmo de cifrado DES con el modo ECB.
*   Implementar la generación aleatoria de la llave.
*   Implementar la función de relleno de bits manualmente.

2. **Generación de una función de cifrado y descifrado 3DES:**
*   Escribir una función en el lenguaje de programación que prefieran, que tome un mensaje en texto plano y lo cifre implementando el algoritmo de cifrado 3DES con el modo CBC.
*   Implementar la generación aleatoria de la llave.
*   Utilizar la función de relleno de bits de la librería mediante pad.

3.  **Generación de una función de cifrado y descifrado AES con CBC y ECB:**
*   Implementar una función que tome una imagen brindada en texto plano y la cifre utilizando el algoritmo AES con los modos CBC y ECB.
*   Implementar la generación aleatoria del vector de inicialización (IV).
*   Implementar la generación aleatoria de la llave.
*   Utilizar la función de relleno de bits de la librería mediante pad.

4.  **Preguntas a Responder:**
*   ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
*   ¿Qué modo de operación está implementado?
*   ¿Por qué no debemos usar ECB en datos sensibles?
*   ¿Cuál es la diferencia entre ECB y CBC? ¿Se puede notar directamente en una imagen?
*   ¿Qué es el IV?
*   ¿Qué es el PADDING?
*   ¿En qué situaciones se recomienda cada modo de operación?
*   ¿Cómo elegir un modo seguro en cada lenguaje de programación?


## Requisitos del lab
- Tener instalado python
- Tener instalado la librería PIL y pycryptodome lo puedes instalar con pip3 install pycryptodome pillow numpy

- Tener un IDE para poder probar el código

## Consideraciones Adicionales 📝
*   Incluye en tu solución ejemplos de entrada y salida (texto plano, cifrado y descifrado).
*   Utiliza pruebas unitarias para validar que el cifrado y el descifrado funcionan correctamente.
*   Reflexiona sobre las limitaciones de los generadores pseudoaleatorios simples en la seguridad de cifrados reales.

## Sugerencias 💡
*   Dividir el código en funciones para la generación de llaves, cifrado y descifrado.
*   Utilizar pruebas unitarias para validar el correcto funcionamiento del cifrado y descifrado.
*   Considerar las limitaciones de los PRNGs simples en contextos de seguridad real.

# Cómo Ejecutar el Código ⏳
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta todo el script `BlockCipher.ipynb` para ver el mensaje encriptado y desencriptado del DES, 3DES y AES usando el modo ECB y CBC.

# Contribuciones 🌟
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este ejercicio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia 📝
Este laboratorio es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.

   
