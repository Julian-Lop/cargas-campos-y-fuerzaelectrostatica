def calcular_fuerza_electrica(q1, q2, r):
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    fuerza = (k * abs(q1 * q2)) / (r ** 2)
    return fuerza

def calcular_potencial_electrico(Q, r):
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    potencial = (k * Q) / r
    return potencial

fuerza = calcular_fuerza_electrica(0.000005,-0.000008, 0.05)
potencial = calcular_potencial_electrico(0.000000003, 0.592)

print(f'Fuerza: {fuerza} | Potencial: {potencial}')