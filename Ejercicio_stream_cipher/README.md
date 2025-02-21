# Ejercicio Stream Cipher 🛠️
Este ejercicio se enfoca en comprender los fundamentos del cifrado de flujo utilizando la operación XOR y la generación de keystreams pseudoaleatorios.

# Competencias a Desarrollar 💡
*   Comprender el concepto de keystream y su rol en el cifrado de flujo.
*   Implementar un esquema básico de cifrado y descifrado con XOR.
*   Analizar las implicaciones de seguridad de la reutilización y longitud del keystream.
*   Implementar funciones para la generación de keystreams pseudoaleatorios.

## Problemas a Resolver 🧠
1. **Generación de Keystream:**
*   Implementar una función que genere un keystream pseudoaleatorio basado en:
        *   Un PRNG básico.
        *   Una clave (seed/nonce) para inicializar el PRNG.
        *   El keystream debe tener al menos la longitud del mensaje a cifrar.

2. **Cifrado:**
*   Implementar una función que cifre un mensaje de texto plano usando XOR con el keystream generado.

3.  **Descifrado:**
    *   Implementar una función que descifre un mensaje cifrado usando XOR con el mismo keystream.

4.  **Análisis de Seguridad:**
    *   Responder a las preguntas sobre qué sucede al cambiar la clave, los riesgos de reutilizar el keystream y cómo la longitud del keystream afecta la seguridad.


## Requisitos del lab
- Tener instalado python
- Tener un IDE para poder probar el código

## Sugerencias
1.  **Modularización del Código:**
    *   Divide el código en funciones para generación de keystream, cifrado y descifrado.

2.  **Pruebas Unitarias:**
    *   Utiliza pruebas unitarias para validar el correcto funcionamiento del cifrado y descifrado.

3.  **Reflexión sobre PRNGs:**
    *   Considera las limitaciones de los PRNGs simples en contextos de seguridad real.

# Cómo Ejecutar el Código ⏳
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta todo el script `streamcipher.ipynb` para ver el mensaje encriptado y desencriptado con la keystream.

# Contribuciones 🌟
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este ejercicio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia 📝
Este laboratorio es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.

   
