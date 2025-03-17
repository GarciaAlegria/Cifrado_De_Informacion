# Laboratorio3 🛠️

Este laboratorio se enfoca en la implementación y análisis de cifrados avanzados, incluyendo cifrados de bloque y de flujo, así como en la evaluación de su seguridad en escenarios prácticos.

# Algunas consideraciones
Tomar en cuenta que para el ejercicio 4 y para probarlo cargar los scrips a cifrar en la carpeta parte4seguros, no te preocupes por las otras carpetas, si no las tienes se crean solas, al igual que la llave se genera sola y de forma random asi que solo asegurarse de cargar los archivos a cifrar en parte4seguros.

# Competencias a Desarrollar 💡

* Implementar AES con modos ECB y CBC en un entorno real.
* Aplicar ChaCha20 como alternativa de cifrado de flujo.
* Analizar los riesgos de los modos ECB y CBC en imágenes.
* Implementar cifrados en un protocolo de comunicación con Wireshark.
* Explorar cómo se rompe un cifrado mal implementado.

## Problemas a Resolver 🧠

1.  **Análisis y Cifrado de Imágenes con AES ECB y CBC:**
    * Utilizar una imagen BMP o PPM en escala de grises.
    * Cifrar la imagen con AES en modo ECB y visualizar el resultado.
    * Cifrar la misma imagen con AES en modo CBC y comparar.
    * Responder preguntas sobre los patrones revelados por ECB, las diferencias con CBC y la seguridad de ECB para datos estructurados.

2.  **Captura y Análisis de Tráfico Cifrado con Wireshark:**
    * Crear un script que envíe mensajes cifrados con AES-CBC a un servidor.
    * Capturar el tráfico con Wireshark y analizar los paquetes.
    * Determinar si se puede identificar que los mensajes están cifrados con AES-CBC y proponer mejoras para proteger la comunicación.

3.  **Implementación y Comparación de ChaCha20 y AES:**
    * Implementar ChaCha20 para cifrar y descifrar mensajes.
    * Comparar su rendimiento con AES en tiempos y consumo de memoria.
    * Analizar qué cifrado es más rápido y en qué casos debería usarse ChaCha20 en lugar de AES.

4.  **Simulación de Ransomware con AES:**
    * Crear un script que cifre archivos de texto con AES en una carpeta.
    * Implementar un script separado para descifrar los archivos usando la clave de descifrado.
    * Reflexionar sobre cómo evitar ataques de ransomware y la importancia del almacenamiento seguro de claves.

## Requisitos del lab

* Máquina virtual Ubuntu o contenedor Docker con pycryptodome instalado.
* Imagen en formato BMP para analizar cifrados ECB y CBC (tux.ppm.zip).
* Wireshark para capturar tráfico cifrado.
* Descargar ejercicio_socket.zip.
* Tener instalado python
* Tener un IDE para poder probar el código

## Consideraciones Adicionales 📝

* Documentar las implementaciones y análisis realizados.
* Incluir capturas de pantalla de Wireshark y visualizaciones de imágenes cifradas.
* Proporcionar ejemplos de código y scripts utilizados.

## Sugerencias 💡

* Dividir el código en funciones para una mayor claridad y reutilización.
* Utilizar comentarios para explicar el funcionamiento de cada sección del código.
* Experimentar con diferentes parámetros y configuraciones para profundizar en la comprensión de los cifrados.

# Cómo Ejecutar el Código ⏳

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta todo el script `lab3.ipynb` para poder probar todos las partes del lab

# Contribuciones 🌟

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este laboratorio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia 📝

Este laboratorio es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.