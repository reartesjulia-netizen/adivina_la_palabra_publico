# 1. Inicio

import random
import pandas as pd
import os
import openpyxl

# 2. Cargar palabras desde Excel
def cargar_palabras():
    ruta = "D:/PHYTON/Trabajos Practicos Curso ADA/Repositorio Adivina_la_palabra/palabras.xlsx"
    if not os.path.exists(ruta):
        print("❌ No se encontró el archivo 'palabras.xlsx'")
        return []
    df = pd.read_excel(ruta)
    return df['Palabra'].dropna().tolist()

# 3. Mostrar estado del juego
def mostrar_estado(palabra, letras_adivinadas, vidas, letras_incorrectas):
    estado = ""
    for letra in palabra:
        estado += letra + " " if letra in letras_adivinadas else "_ "
    print(f"\nPalabra: {estado.strip()}")
    print(f"Vidas: {vidas}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
    if vidas < 15:
        print(f"⚠️ Ya perdiste {15 - vidas} vida(s)")

# 4. Lógica principal del juego
def jugar():
    palabras = cargar_palabras()
    if not palabras:
        return

    palabra = random.choice(palabras).lower()
    vidas = 15
    letras_adivinadas = []
    letras_incorrectas = []

    print("🎮 Bienvenido al juego de ¡Adivina la palabra!")
    mostrar_estado(palabra, letras_adivinadas, vidas, letras_incorrectas)

    while True:
        letra = input("Ingresa una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("⚠️ Ingresa una sola letra válida")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("🔁 Ya usaste esa letra")
            continue

        # Guardar letra
        if letra in palabra:
            letras_adivinadas.append(letra)
            print("✅ ¡Letra correcta!")
        else:
            vidas -= 1
            letras_incorrectas.append(letra)
            print(f"❌ Letra incorrecta, te quedan {vidas} vidas")
            if vidas < 15:
                print(f"⚠️ Ya perdiste {15 - vidas} vida(s)")

        mostrar_estado(palabra, letras_adivinadas, vidas, letras_incorrectas)

        # Verificar si ganó
        if all(l in letras_adivinadas for l in palabra):
            print("🎉 ¡Felicitaciones, GANASTE!")
            break

        # Verificar si perdió
        elif vidas == 0:
            print(f"😢 Lo siento, PERDISTE. La palabra era: {palabra}")
            break

# 5. Bucle principal
def main():
    try:
        while True:
            jugar()
            seguir = input("¿Querés seguir jugando? (S/N): ").lower()
            if seguir != "s":
                print("👋 Gracias por jugar. ¡Chau!")
                break
    except KeyboardInterrupt:
        print("\n⛔ Juego interrumpido manualmente. ¡Hasta la próxima!")

# 6. Ejecutar
if __name__ == "__main__":
    main()

