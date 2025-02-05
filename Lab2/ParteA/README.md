# Lab 2 – Base 64 y XOR 🛠️
Este laboratorio tiene como objetivo implementar funciones en Python para trabajar con conversiones de texto a binario, Base64 y la operación XOR. Además, se explorará la manipulación de imágenes usando matrices de bits y la librería Pillow.

# Competencias a Desarrollar 💡
- Implementar el uso de funciones para realizar la operación XOR.
- Implementar funciones para la conversión entre texto y Base64.
- Implementar funciones para la conversión entre texto y binario.
- Identificar los requisitos necesarios para unificar dos imágenes.
- Utilizar la librería Pillow en Python para el manejo de imágenes.
- Implementar el uso de matrices de bits en imágenes.

## Problemas a Resolver 🧠
En este laboratorio, se implementarán funciones para convertir cadenas a bits y a Base64, así como el análisis de una propiedad estadística de la función XOR.

1. Conversión de Texto a Binario
Implementar una función que convierta una cadena de caracteres en una secuencia de bits.
- Cada carácter debe transformarse en su representación ASCII de 8 bits.
- La función debe devolver la concatenación de todos los bits de la cadena.
- Ejemplo: Convertir "AB" a su representación en bits.

2. Conversión de Binario a Texto
Implementar una función que convierta una cadena de bits en texto.
- Cada grupo de 8 bits representa un carácter ASCII.
- La función debe devolver la cadena de texto correspondiente.
- Ejemplo: Convertir "01000001 01000010" de bits a "AB".

3. Conversión de Texto a Base64
Implementar funciones para convertir una cadena de caracteres a Base64 mediante la conversión manual:
- Texto → Binario → Código Unicode → Base64
- Ejemplo: Convertir "Hola" a Base64.

4. Conversión de Base64 a Texto
Implementar funciones que permitan convertir una cadena de Base64 a su texto original:
- Base64 → Código Unicode → Binario → Texto ASCII
- Ejemplo: Convertir "SG9sYQ==" a "Hola".

5. Implementación de la Operación XOR
Crear una función que realice la operación XOR bit a bit entre dos cadenas de texto.
- Si la clave es menor que la palabra, debe repetirse hasta alcanzar el mismo tamaño.
- Ejemplo: Aplicar XOR entre "mensaje" y una clave.

## Requisitos del lab
- Tener instalado python
- Tener un IDE para poder probar el código

## Sugerencias
1. Uso de funciones modulares 🛠️
- Divide el código en funciones específicas para cada conversión (texto a bits, bits a texto, texto a Base64, Base64 a texto, XOR, etc.).
- Esto facilitará la reutilización y depuración del código.

2. Validaciones en las funciones ✅
- Asegúrate de manejar errores cuando se ingresen datos no válidos.
- Verifica que los tamaños de las claves en la operación XOR sean adecuados y que los caracteres sean válidos para las conversiones Base64.

3. Comprensión de Base64 🔤
- Base64 usa un conjunto de 64 caracteres (A-Z, a-z, 0-9, +, /) para representar datos en formato binario.
- Es útil practicar manualmente la conversión para entender mejor cómo funciona.

4. Conversión binaria precisa ⚙️
- Recuerda que cada carácter ASCII debe representarse con 8 bits en binario.
- Asegúrate de completar con ceros a la izquierda cuando sea necesario.

5. Manejo de XOR y claves 🔑
- Si la clave para XOR es más corta que el texto, deberás repetirla o extenderla para que coincida en longitud.
- XOR es una operación reversible, por lo que aplicar la misma clave dos veces devolverá el texto original.

6. Visualización de resultados 🖥️
- Imprime los resultados en pasos intermedios para verificar que las conversiones sean correctas.
- Usa ejemplos cortos para hacer debugging más fácilmente.

# Cómo Ejecutar el Código ⏳
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta el script `script.py` para realizar el análisis de fuerza bruta sobre los textos cifrados. 
   ```python
   python script.py.py
   ```
# Contribuciones 🌟
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este laboratorio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia 📝
Este laboratorio es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.

   
