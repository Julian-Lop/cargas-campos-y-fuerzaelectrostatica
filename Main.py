import math

def calcular_fuerza_electrica(p1, p2):
    var_q1, var_x1, var_y1 = p1.values()
    var_q2, var_x2, var_y2 = p2.values()
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    rx =  var_x1 - var_x2
    ry = var_y1 - var_y2
    r = math.sqrt( ((rx**2) + (ry**2)) )
    fuerza = (k * abs(var_q1 * var_q2)) / (r ** 2)
    return fuerza

def calcular_potencial_electrico(Q,x,y):
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    r = math.sqrt( ((x**2) + (y**2)) )
    potencial = (k * Q) / r
    return potencial

particula1 = {'q1': 0.000005, 'x1': -0.02, 'y1': 0.01}
particula2 = {'q2': -0.000008, 'x2': 0.01, 'y2': 0.05}

fuerza = calcular_fuerza_electrica(particula1,particula2)

potencial = calcular_potencial_electrico(0.000000003, 0.508, 0.3048)

print(f'Fuerza: {fuerza} | Potencial: {potencial}')