taller1 = float(input("Ingrese la nota del Taller 1: "))
taller2 = float(input("Ingrese la nota del Taller 2: "))
cuestionario1 = float(input("Ingrese la nota del Cuestionario 1: "))
cuestionario2 = float(input("Ingrese la nota del Cuestionario 2: "))
proyecto_final = float(input("Ingrese la nota del Proyecto final: "))

peso_taller1 = 0.20
peso_taller2 = 0.15
peso_cuestionario1 = 0.22
peso_cuestionario2 = 0.10
peso_proyecto_final = 0.33

nota_definitiva = (
    taller1 * peso_taller1 +
    taller2 * peso_taller2 +
    cuestionario1 * peso_cuestionario1 +
    cuestionario2 * peso_cuestionario2 +
    proyecto_final * peso_proyecto_final
)

if 1.0 <= nota_definitiva <= 5.0:
    print(f"La nota final calculada es: {nota_definitiva:.2f}")
    if nota_definitiva >= 4.5:
        print("¡Excelente trabajo!")
    elif nota_definitiva >= 3.5:
        print("Buena nota.")
    elif nota_definitiva >= 2.5:
        print("Regular.")
    else:
        print("Insuficiente.")
else:
    print("La nota final está fuera del rango válido. Verifica las notas ingresadas.")
