# Lab 1 – Encriptado y Decriptado de Texto 💻
Este ejercicio incluye una serie de funciones en Python que permiten descifrar textos utilizando fuerza bruta para cada algoritmo el caesar, afin y vigenere , así como analizar la frecuencia de aparición de letras en un texto cifrado en comparación con la distribución teórica del español.

# Objetivos del laboratorio Parte B 📌
- Implementar el uso de funciones para encriptar y decriptar un texto cifrado
- Identifica los requisitos para un análisis de fuerza bruta por frecuencia.

## Problemas a Resolver 🧠
El objetivo principal es implementar un análisis de fuerza bruta para descifrar tres archivos de texto cifrados que utilizan diferentes técnicas de encriptado:

1. **ceasar.txt** - Cifrado **César**.
2. **afines.txt** - Cifrado **Afín**.
3. **vigenere.txt** - Cifrado **Vigenère**.

Para cada uno de estos archivos, el análisis debe realizarse utilizando un ciclo que recorra todas las claves posibles en el espacio de claves. La función de fuerza bruta debe almacenar las métricas obtenidas para cada clave y ordenar las claves de mejor a peor. El objetivo es devolver las `k` mejores claves, donde la clave más probable para descifrar el texto es la que tiene la mejor métrica.

## Requisitos del lab
- Implementar funciones para cada uno de los métodos de cifrado y decripción:
  - **Cifrado César**.
  - **Cifrado Afín**.
  - **Cifrado Vigenère**.
  
- Crear una función de análisis de **fuerza bruta** que realice las siguientes tareas:
  1. Recorrer todas las claves posibles.
  2. Calcular la métrica para cada clave.
  3. Ordenar las claves en función de la métrica obtenida.
  4. Devolver las `k` mejores claves.

- Implementar una métrica que permita evaluar qué tan "correcto" es el texto descifrado en función de las frecuencias de caracteres.

## Sugerencias
1. **Construcción de la función de fuerza bruta**:
   - Utilizar un ciclo que recorra todas las claves posibles en el espacio de claves.
   - Para cada clave, almacenar un arreglo de las métricas obtenidas.
   - Ordenar el arreglo de las métricas de mejor a peor.
   - Devolver las `k` mejores claves basadas en la métrica.

2. **Métrica de evaluación**:
   - Utilizar la frecuencia de caracteres en el idioma del texto original para determinar qué tan probable es una clave. Por ejemplo, en textos en español, la letra "e" es la más frecuente.
   
3. **Prueba y análisis**:
   - Una vez que las claves son identificadas, utilizar el algoritmo de descifrado para obtener el texto original y validarlo.

# Cómo Ejecutar el Código
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta el script `script.py` para realizar el análisis de fuerza bruta sobre los textos cifrados. 
   ```python
   python script.py.py
   ```
# Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este laboratorio o agregar nuevas funcionalidades, no dudes en enviar un pull request.

# Licencia
Este laboratorio es de uso libre para fines educativos y personales. Por favor, da el crédito correspondiente si utilizas este código en tus proyectos u ejercicios.

   
