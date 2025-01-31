# Generador de Cifrado y Conversiones en Python 💻
Este ejercicio incluye una serie de funciones en Python que permiten realizar múltiples conversiones entre representaciones de texto y binario, aplicar operaciones XOR, y generar llaves dinámicas para cifrados. Todo el código está diseñado sin el uso de librerías externas.
## Funcionalidades 🧠
1. Conversión de Texto a Binario
- ASCII a Binario: Convierte palabras en texto ASCII a su representación binaria.
- BASE64 a Binario: Convierte palabras codificadas en Base64 a su representación binaria.

2. Conversión de Binario a Otros Formatos
- Binario a Base64: Convierte cadenas binarias a su representación en Base64.
- Binario a ASCII: Convierte cadenas binarias a texto ASCII.
- Base64 a ASCII (vía Binario): Realiza una conversión de Base64 a ASCII pasando por su representación binaria.

3. Operación XOR
- Aplica la operación XOR entre cadenas binarias.

4. Generación de Llaves Dinámicas
- Genera llaves dinámicas utilizando caracteres ASCII imprimibles, sin depender de librerías externas.

5. Cifrado con Llave Fija y Dinámica
- Llave Fija: Aplica un cifrado XOR entre el texto dado y una llave fija.
- Llave Dinámica: Genera una llave dinámica de tamaño especificado y aplica un cifrado XOR con ella.

# Historia del Cifrado
El cifrado ha sido una herramienta fundamental en la protección de información desde tiempos antiguos. Una de las primeras técnicas conocidas es el Cifrado César, utilizado por Julio César para enviar mensajes secretos durante sus campañas militares en Roma. Este método consistía en desplazar las letras del alfabeto por un número fijo de posiciones, haciendo que el mensaje fuera ilegible para cualquier persona que no conociera la clave de desplazamiento.

# Cómo Ejecutar el Código
1. Descarga el archivo parte2.py
2. Abre una terminal o entorno de desarrollo y ejecuta el archivo:
   ```python
   python parte2.py
   ```
# Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este ejercicio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia
Este proyecto es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.

   
