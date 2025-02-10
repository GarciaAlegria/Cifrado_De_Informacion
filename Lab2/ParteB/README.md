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

1. Implementación de la Operación XOR
- Crear una función que realice la operación XOR bit a bit entre dos cadenas de texto.
- Si la clave es menor que la palabra, debe repetirse hasta alcanzar el mismo tamaño.
- Ejemplo: Aplicar XOR entre "mensaje" y una clave.

2. Descifrado de una Imagen XOR
- Dada la imagen XOR_Imagen y la llave "cifrados_2025", encontrar el valor original de la imagen.
- Convertir la imagen a Base64 y aplicarle un XOR con la llave.
- Explicar por qué la imagen se corrompe al aplicar XOR con una llave de texto.

7. XOR entre Dos Imágenes
- Investigar cómo aplicar un XOR entre dos imágenes
- Elegir dos imágenes y realizar la operación XOR entre ellas.
- Explicar los inconvenientes encontrados al realizar la operación.

## Requisitos del lab
- Tener instalado python
- Tener un IDE para poder probar el código
- Tener instalado las librerias pillow y numpy

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
- Visualizar el XOR entre dos imagenes
- Vizualizar una imagen entre un XOR de imagen como llave un texto

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

   
