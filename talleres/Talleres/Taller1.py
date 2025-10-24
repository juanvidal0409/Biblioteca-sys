from math import comb, perm

# Datos del problema
electronica = 8
sistemas = 3
industrial = 9
total = electronica + sistemas + industrial
seleccionados = 3

# Total de formas de elegir 3 estudiantes sin reemplazo
total_combinaciones = comb(total, seleccionados)

# 2. Los 3 estudiantes sean de Electrónica
casos_electronica = comb(electronica, 3)
prob_electronica = casos_electronica / total_combinaciones

# 3. Los 3 estudiantes sean de Sistemas
casos_sistemas = comb(sistemas, 3)
prob_sistemas = casos_sistemas / total_combinaciones

# 4. 2 de Electrónica y 1 de Sistemas
casos_2E_1S = comb(electronica, 2) * comb(sistemas, 1)
prob_2E_1S = casos_2E_1S / total_combinaciones

# 5. Al menos 1 sea de Sistemas
# Complemento: ninguno de sistemas
casos_sin_sistemas = comb(electronica + industrial, 3)
prob_al_menos_1S = 1 - (casos_sin_sistemas / total_combinaciones)

# 6. Se escoja 1 de cada carrera
casos_1_cada = comb(electronica, 1) * comb(sistemas, 1) * comb(industrial, 1)
prob_1_cada = casos_1_cada / total_combinaciones

# 7. Se seleccionen en el orden: Electrónico - Sistemas - Industrial
# En este caso es una permutación sin reemplazo
casos_orden = electronica * sistemas * industrial
total_permutaciones = perm(total, 3)
prob_orden = casos_orden / total_permutaciones

# Mostrar resultados
print("Probabilidades:")
print(f"2. 3 Electrónica: {prob_electronica:.6f}")
print(f"3. 3 Sistemas: {prob_sistemas:.6f}")
print(f"4. 2 Electrónica y 1 Sistemas: {prob_2E_1S:.6f}")
print(f"5. Al menos 1 Sistemas: {prob_al_menos_1S:.6f}")
print(f"6. 1 de cada carrera: {prob_1_cada:.6f}")
print(f"7. Orden Electrónico-Sistemas-Industrial: {prob_orden:.6f}")
