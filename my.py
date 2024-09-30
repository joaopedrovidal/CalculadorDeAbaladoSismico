import math

def calcular_magnitude_e_energia(amplitude, delta_t):
    # Cálculo da magnitude M
    M = math.log10(amplitude) + (3 * math.log10(8.0 * (delta_t / 1000))) - 2.92
    
    # Cálculo da energia liberada E
    E0 = 7e-3  # Energia padrão em kWh
    E = 10**(1.5 * M + 4.8)  # Energia em kWh

    return M, E

def efeitos_terremoto(magnitude):
    if magnitude < 3.0:
        return "Não sentido, mas registrado."
    elif 3.0 <= magnitude < 4.0:
        return "Sentido, mas raramente causa danos."
    elif 4.0 <= magnitude < 5.0:
        return "Causa danos leves em edifícios frágeis."
    elif 5.0 <= magnitude < 6.0:
        return "Causa danos moderados em edifícios."
    elif 6.0 <= magnitude < 7.0:
        return "Causa danos significativos em áreas povoadas."
    elif 7.0 <= magnitude < 8.0:
        return "Causa grandes danos em áreas urbanas."
    else:
        return "Causa destruição em larga escala."

def main():
    print("Cálculo da Magnitude e Energia Liberada de um Terremoto")
    
    # Entrada do usuário
    amplitude = float(input("Digite a amplitude máxima (A) em mm: "))
    delta_t = float(input("Digite a distância entre as ondas P e S (Δt) em mm: "))

    # Cálculo
    magnitude, energia = calcular_magnitude_e_energia(amplitude, delta_t)
    
    # Resultados
    print(f"\nMagnitude (M): {magnitude:.2f}")
    print(f"Energia Liberada (E): {energia:.2f} kWh")
    print(f"Efeitos do terremoto: {efeitos_terremoto(magnitude)}")

if __name__ == "__main__":
    main()
