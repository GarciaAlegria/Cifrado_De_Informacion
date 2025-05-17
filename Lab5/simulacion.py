# Simulación del Protocolo BB84
# Abner Ivan Garcia Alegria - 21285
# Oscar Esteban Donis - 21610
# Laboratorio 5 - QKD
# Universidad del Valle de Guatemala
# Cifrado de información
# Ludwing Cano

import random

def generar_bits(n): # Genera n bits aleatorios (0 o 1).
    """Genera n bits aleatorios (0 o 1)."""
    return [random.randint(0, 1) for _ in range(n)] # Genera una lista de n bits aleatorios.

def generar_bases(n): # Genera n bases aleatorias ('vertical' o 'diagonal').
    """Genera n bases aleatorias ('vertical' o 'diagonal')."""
    bases = ['vertical', 'diagonal'] # Define las bases posibles.
    return [random.choice(bases) for _ in range(n)] # Genera una lista de n bases aleatorias.

def codificar_fotones(bits, bases): # Codifica los bits en polarizaciones de fotones según las bases.
    """Codifica los bits en polarizaciones de fotones según las bases."""
    polarizaciones = [] # Lista para almacenar las polarizaciones de los fotones.
    for bit, base in zip(bits, bases): # Itera sobre los bits y las bases.
        if base == 'vertical':
            polarizaciones.append('↕' if bit == 0 else '↔') # Si la base es vertical, asigna '↕' para 0 y '↔' para 1.
        else:  # base diagonal
            polarizaciones.append('↗' if bit == 0 else '↖') # Si la base es diagonal, asigna '↗' para 0 y '↖' para 1.
    return polarizaciones

def medir_fotones(polarizaciones, bases_bob): # Mide las polarizaciones de los fotones con las bases de Bob.
    """Mide las polarizaciones de los fotones con las bases de Bob."""
    resultados_bob = [] # Lista para almacenar los resultados de Bob.
    for polarizacion, base_bob in zip(polarizaciones, bases_bob): # Itera sobre las polarizaciones y las bases de Bob.
        if base_bob == 'vertical': # Si la base de Bob es vertical
            if polarizacion in ['↕', '↔']: # Si la polarización es '↕' o '↔'
                resultados_bob.append(0 if polarizacion == '↕' else 1) # Asigna 0 para '↕' y 1 para '↔'.
            else:  # Bob midió con la base incorrecta
                resultados_bob.append(random.randint(0, 1)) # Asigna un valor aleatorio (0 o 1).
        else:  # base diagonal
            if polarizacion in ['↗', '↖']: # Si la polarización es '↗' o '↖'
                resultados_bob.append(0 if polarizacion == '↗' else 1) # Asigna 0 para '↗' y 1 para '↖'.
            else:  # Bob midió con la base incorrecta
                resultados_bob.append(random.randint(0, 1)) # Asigna un valor aleatorio (0 o 1).
    return resultados_bob

def construir_clave(bases_alice, bases_bob, bits_alice, resultados_bob): # Construye la clave secreta comparando las bases.
    """Construye la clave secreta comparando las bases."""
    clave_alice = [] # Lista para almacenar la clave de Alice.
    clave_bob = [] # Lista para almacenar la clave de Bob.
    bases_coincidentes = [] # Lista para almacenar las bases coincidentes.
    for i, (base_a, base_b) in enumerate(zip(bases_alice, bases_bob)): # Itera sobre las bases de Alice y Bob.
        if base_a == base_b: # Si las bases coinciden
            clave_alice.append(bits_alice[i]) # Agrega el bit de Alice a su clave.
            clave_bob.append(resultados_bob[i]) # Agrega el resultado de Bob a su clave.
            bases_coincidentes.append((base_a, base_b)) # Agrega la base coincidente a la lista.
    return clave_alice, clave_bob, bases_coincidentes # Devuelve las claves y las bases coincidentes.

def simular_bb84(n_bits): # Simula el protocolo BB84.
    """Simula el protocolo BB84."""
    print("\n--- Simulación del Protocolo BB84 ---")

    # Alice genera bits y bases
    bits_alice = generar_bits(n_bits)
    bases_alice = generar_bases(n_bits) # Genera n bits y bases aleatorias
    print(f"Alice generó {n_bits} bits: {bits_alice}")
    print(f"Bases de Alice:        {bases_alice}")

    # Alice codifica los fotones
    polarizaciones = codificar_fotones(bits_alice, bases_alice)
    print(f"Polarizaciones enviadas: {polarizaciones}")

    # Bob genera sus bases aleatoriamente
    bases_bob = generar_bases(n_bits)
    print(f"Bases de Bob:          {bases_bob}")

    # Bob mide los fotones
    resultados_bob = medir_fotones(polarizaciones, bases_bob)
    print(f"Resultados de Bob:     {resultados_bob}")

    # Alice y Bob comparan sus bases y construyen la clave
    clave_alice, clave_bob, bases_coincidentes = construir_clave(bases_alice, bases_bob, bits_alice, resultados_bob)
    print("\n--- Construcción de la Clave Secreta ---")
    print(f"Bases coincidentes:    {bases_coincidentes}")
    print(f"Clave de Alice:        {clave_alice}")
    print(f"Clave de Bob:          {clave_bob}")

    if clave_alice == clave_bob:
        print("\n¡La clave secreta se estableció con éxito!")
    else:
        print("\n¡Hubo errores en la transmisión!")

# Implementación de Eve interceptando
def interceptar(polarizaciones, bases_eve):
    """Eve intercepta y mide los fotones con sus propias bases."""
    resultados_eve = [] # Lista para almacenar los resultados de Eve.
    for polarizacion, base_eve in zip(polarizaciones, bases_eve): # Itera sobre las polarizaciones y las bases de Eve.
        if base_eve == 'vertical': # Si la base de Eve es vertical
            resultados_eve.append(0 if polarizacion in ['↕', '↖'] else 1) # Si mide vertical, ↗ se interpreta como 1
            if polarizacion in ['↕', '↔']:
                polarizaciones[polarizaciones.index(polarizacion)] = '↕' if random.random() < 0.5 else '↔' # Reenvía un estado
            else:
                polarizaciones[polarizaciones.index(polarizacion)] = '↕' if resultados_eve[-1] == 0 else '↔'
        else:  # base diagonal
            resultados_eve.append(0 if polarizacion in ['↗', '↕'] else 1) # Si mide diagonal, ↕ se interpreta como 1
            if polarizacion in ['↗', '↖']:
                polarizaciones[polarizaciones.index(polarizacion)] = '↗' if random.random() < 0.5 else '↖' # Reenvía un estado
            else:
                polarizaciones[polarizaciones.index(polarizacion)] = '↗' if resultados_eve[-1] == 0 else '↖'
    print(f"\n--- Eve Intercepta ---")
    print(f"Bases de Eve:          {bases_eve}")
    print(f"Resultados de Eve:     {resultados_eve}")
    print(f"Polarizaciones reenviadas por Eve: {polarizaciones}")
    return polarizaciones

def simular_bb84_con_eve(n_bits): # Simula el protocolo BB84 con Eve interceptando.
    """Simula el protocolo BB84 con Eve interceptando."""
    print("\n--- Simulación del Protocolo BB84 con Eve ---")

    # Alice genera bits y bases
    bits_alice = generar_bits(n_bits)
    bases_alice = generar_bases(n_bits)
    print(f"Alice generó {n_bits} bits: {bits_alice}")
    print(f"Bases de Alice:        {bases_alice}")

    # Alice codifica los fotones
    polarizaciones = codificar_fotones(bits_alice, bases_alice)
    print(f"Polarizaciones enviadas: {polarizaciones}")

    # Eve intercepta
    bases_eve = generar_bases(n_bits)
    polarizaciones_despues_eve = interceptar(polarizaciones[:], bases_eve) # Pasar una copia para no modificar la original

    # Bob genera sus bases aleatoriamente
    bases_bob = generar_bases(n_bits)
    print(f"Bases de Bob:          {bases_bob}")

    # Bob mide los fotones (después de la posible intervención de Eve)
    resultados_bob = medir_fotones(polarizaciones_despues_eve, bases_bob)
    print(f"Resultados de Bob:     {resultados_bob}")

    # Alice y Bob comparan sus bases y construyen la clave
    clave_alice, clave_bob, bases_coincidentes = construir_clave(bases_alice, bases_bob, bits_alice, resultados_bob)
    print("\n--- Construcción de la Clave Secreta ---")
    print(f"Bases coincidentes:    {bases_coincidentes}")
    print(f"Clave de Alice:        {clave_alice}")
    print(f"Clave de Bob:          {clave_bob}")

    if clave_alice == clave_bob:
        print("\n¡La clave secreta se estableció (posiblemente comprometida)!")
    else:
        print("\n¡Hubo errores en la transmisión (posible detección de Eve)! ")

# Ejecutar la simulación
n_bits_simulacion = 12
simular_bb84(n_bits_simulacion)

# Ejecutar la simulación con Eve
simular_bb84_con_eve(n_bits_simulacion)