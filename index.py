def calcular_fuerza_electrica(q1, q2, r):
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    fuerza = (k * abs(q1 * q2)) / (r ** 2)
    return fuerza

def calcular_potencial_electrico(Q, r):
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    potencial = (k * Q) / r
    return potencial
