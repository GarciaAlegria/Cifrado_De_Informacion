# Simulación del Protocolo BB84 - Laboratorio 5

## 📋 Información General

- **Autores:** 
  - Abner Ivan Garcia Alegria - 21285
  - Oscar Esteban Donis - 21610
- **Laboratorio:** 5 - QKD (Quantum Key Distribution)
- **Universidad:** Universidad del Valle de Guatemala
- **Curso:** Cifrado de Información
- **Profesor:** Ludwing Cano

## 🔬 Descripción del Proyecto

En este laboratorio se implementa una simulación del **Protocolo BB84**, el primer protocolo de intercambio de llaves cuánticas (QKD). El protocolo permite que dos computadoras (Alice y Bob) establezcan una clave secreta compartida utilizando las propiedades de la mecánica cuántica.

## 🎯 Objetivos

- Simular el intercambio de claves cuánticas utilizando el protocolo BB84
- Demostrar cómo se establecen claves seguras entre Alice y Bob
- Implementar la detección de interceptación por parte de un espía (Eve)
- Mostrar las propiedades de seguridad de la criptografía cuántica

## ⚡ Funcionamiento del Protocolo BB84

### 1. Polarizaciones de Fotones
El protocolo utiliza cuatro estados de polarización diferentes:
- **Base Vertical:** `↕` (bit 0) y `↔` (bit 1)
- **Base Diagonal:** `↗` (bit 0) y `↖` (bit 1)

### 2. Proceso de Intercambio
1. **Alice** genera bits aleatorios y bases aleatorias
2. **Alice** codifica los bits en polarizaciones de fotones según las bases elegidas
3. **Bob** elige bases aleatorias para medir los fotones
4. **Bob** mide los fotones usando sus bases
5. **Alice y Bob** comparan públicamente sus bases (no los resultados)
6. Mantienen solo los bits donde usaron la misma base para formar la clave secreta

### 3. Detección de Interceptación
Cuando **Eve** intercepta los fotones:
- Debe medir con una base aleatoria
- Su medición altera el estado cuántico del fotón
- Esto introduce errores detectables en la clave final, haciendo que las encriptaciones no funcionen del todo.

## 🛠️ Funciones Principales

| Función | Descripción |
|---------|-------------|
| `generar_bits(n)` | Genera n bits aleatorios (0 o 1) |
| `generar_bases(n)` | Genera n bases aleatorias ('vertical' o 'diagonal') |
| `codificar_fotones(bits, bases)` | Codifica bits en polarizaciones según las bases |
| `medir_fotones(polarizaciones, bases_bob)` | Simula la medición de Bob |
| `construir_clave(...)` | Construye la clave secreta comparando bases |
| `interceptar(...)` | Simula la interceptación de Eve |
| `simular_bb84(n_bits)` | Ejecuta la simulación completa sin interceptación |
| `simular_bb84_con_eve(n_bits)` | Ejecuta la simulación con interceptación |

## 🚀 Uso del Programa

### Prerrequisitos
- Python 3.x
- Módulo `random` (incluido en Python estándar)

### Ejecución
```bash
python simulacion.py
```

### Ejemplo de Salida

```
--- Simulación del Protocolo BB84 ---
Alice generó 12 bits: [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
Bases de Alice:        ['diagonal', 'vertical', 'diagonal', ...]
Polarizaciones enviadas: ['↖', '↕', '↖', '↔', ...]
Bases de Bob:          ['vertical', 'vertical', 'diagonal', ...]
Resultados de Bob:     [0, 0, 1, 1, ...]

--- Construcción de la Clave Secreta ---
Bases coincidentes:    [('vertical', 'vertical'), ('diagonal', 'diagonal'), ...]
Clave de Alice:        [0, 1, 1, 0]
Clave de Bob:          [0, 1, 1, 0]

¡La clave secreta se estableció con éxito!
```

## 🔐 Características de Seguridad

1. **Seguridad Incondicional:** La seguridad se basa en las leyes de la física cuántica.
2. **Detección de Interceptación:** Cualquier intento de espionaje introduce errores detectables al momento de crear la llave e intercambiar mensajes encriptados.
3. **Imposible Copiar Estado cuántico:** Es imposible copiar perfectamente un estado cuántico desconocido
4. **Verificación de Integridad:** Alice y Bob pueden detectar la presencia de Eve al momento de que sus encriptaciones no funcionen correctamente

## 📊 Resultados Esperados

- **Sin Interceptación:** La clave de Alice y Bob debe coincidir perfectamente
- **Con Interceptación:** Se introducen errores que permiten detectar la presencia de Eve

## 🧪 Experimentación

El programa ejecuta dos simulaciones:
1. **Simulación Normal:** Demuestra el funcionamiento ideal del protocolo
2. **Simulación con Eve:** Muestra cómo se detecta la interceptación
