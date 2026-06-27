
#   JUEGO DEL AHORCADO
#   Materia: Introducción al Desarrollo de Software
#   Autor  : [Tu Nombre]
#
#   Este programa usa:
#    - Listas: para guardar letras usadas y la palabra oculta
#    - Tuplas:para guardar cada palabra junto a su pista
#    - if/else: para tomar decisiones dentro del juego
#    - while: para repetir el juego mientras el jugador quiera
#    - for: para recorrer letras y mostrar información

import random   # esto permite elegir una palabra al azar


#   DIBUJOS DEL AHORCADO
#   Es una lista donde cada posición es un dibujo
#   Posición 0 = sin errores, posición 6 = muerto

dibujos = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]


#   BANCO DE PALABRAS
#
#   El diccionario tiene 2 niveles:
#    1. Categoría  (animales, frutas, etc.)
#    2. Dificultad (facil, medio, dificil)
#
#   Dentro de cada dificultad hay una LISTA de TUPLAS.
#   Cada TUPLA tiene dos elementos:
#    Primer elemento: la palabra
#    Segundo elemento: la pista

palabras = {
    "animales": {
        "facil": [
            ("perro",  "El mejor amigo del hombre"),
            ("gato",   "Le encanta dormir y ronronear"),
            ("vaca",   "Nos da leche y vive en la granja"),
            ("pato",   "Ave acuática que hace cuac"),
        ],
        "medio": [
            ("elefante", "El animal terrestre más grande del mundo"),
            ("delfin",   "Mamífero marino muy inteligente"),
            ("camello",  "Tiene joroba y vive en el desierto"),
            ("gorila",   "El primate más grande del mundo"),
        ],
        "dificil": [
            ("ornitorrinco", "Mamífero que pone huevos y tiene pico"),
            ("rinoceronte",  "Tiene cuerno y piel muy gruesa"),
            ("chimpance",    "Primate muy cercano al ser humano"),
            ("salamandra",   "Anfibio que puede regenerar sus patas"),
        ],
    },
    "frutas": {
        "facil": [
            ("pera",  "Con forma de bombilla, verde o amarilla"),
            ("uva",   "Crece en racimos y se usa para vino"),
            ("lima",  "Cítrico pequeño y verde"),
            ("higo",  "Pequeño, dulce y con semillas internas"),
        ],
        "medio": [
            ("sandia",  "Verde por fuera y roja por dentro"),
            ("papaya",  "Fruta tropical grande con semillas negras"),
            ("cereza",  "Pequeña, roja y con hueso"),
            ("guayaba", "Muy aromática y rosada por dentro"),
        ],
        "dificil": [
            ("maracuya",  "Fruta de la pasión, muy ácida y aromática"),
            ("carambola", "Su corte tiene forma de estrella"),
            ("tamarindo", "Vaina marrón con pulpa ácida"),
            ("pitahaya",  "Fruta dragón, rosada con puntos blancos"),
        ],
    },
    "paises": {
        "facil": [
            ("peru",   "País de Machu Picchu"),
            ("cuba",   "Isla caribeña famosa por su música"),
            ("chile",  "País largo y angosto"),
            ("brasil", "El más grande de Sudamérica"),
        ],
        "medio": [
            ("ecuador",  "Atravesado por la línea ecuatorial"),
            ("vietnam",  "País del Sudeste Asiático"),
            ("hungria",  "País europeo con capital Budapest"),
            ("uruguay",  "El más pequeño de Sudamérica continental"),
        ],
        "dificil": [
            ("kazajistan", "El país sin salida al mar más grande del mundo"),
            ("mozambique", "País africano con costa en el Índico"),
            ("azerbaiyan", "País del Cáucaso con capital Bakú"),
            ("zimbabue",   "Hogar de las Cataratas Victoria"),
        ],
    },
    "tecnologia": {
        "facil": [
            ("mouse",   "Dispositivo para mover el cursor"),
            ("disco",   "Dispositivo de almacenamiento"),
            ("virus",   "Programa malicioso que daña el PC"),
            ("red",     "Computadoras conectadas entre sí"),
        ],
        "medio": [
            ("python",   "Lenguaje con nombre de serpiente"),
            ("memoria",  "Guarda datos temporales en el PC"),
            ("router",   "Distribuye la conexión a internet"),
            ("binario",  "Sistema que solo usa 0 y 1"),
        ],
        "dificil": [
            ("algoritmo",  "Pasos para resolver un problema"),
            ("protocolo",  "Reglas para la comunicación en red"),
            ("compilador", "Traduce código a lenguaje de máquina"),
            ("blockchain", "Cadena de bloques descentralizada"),
        ],
    },
}

#  CONFIGURACIÓN DE DIFICULTAD
#
#  Usamos una TUPLA por cada nivel con:
#    Primer elemento: intentos máximos permitidos
#    Segundo elemento: pistas disponibles
#
#  Fácil: más intentos, más pistas  
#  Medio: intentos y pistas normales
#  Difícil: menos intentos, menos pistas

config_dificultad = {
    "facil":   (8, 3),   # 8 intentos, 3 pistas
    "medio":   (6, 2),   # 6 intentos, 2 pistas
    "dificil": (4, 1),   # 4 intentos, 1 pista
}

#  FUNCIÓN: mostrar el menú de categorías
#  Retorna el nombre de la categoría elegida


def elegir_categoria():
    print("\n¿Qué categoría quieres jugar?")
    print("  1. Animales")
    print("  2. Frutas")
    print("  3. Paises")
    print("  4. Tecnologia")

    # BUCLE while: se repite hasta que el jugador escriba un número válido
    while True:
        opcion = input("\nEscribe el número de tu elección: ")

        if opcion == "1":
            return "animales"
        elif opcion == "2":
            return "frutas"
        elif opcion == "3":
            return "paises"
        elif opcion == "4":
            return "tecnologia"
        else:
            # Si escribió algo diferente, volvemos a preguntar
            print("Opción no válida. Escribe 1, 2, 3 o 4.")


#  FUNCIÓN: mostrar el menú de dificultad
#  Retorna el nombre de la dificultad elegida


def elegir_dificultad():
    print("\n¿Qué dificultad quieres?")
    print("  1. Facil   (8 intentos, 3 pistas)")
    print("  2. Medio   (6 intentos, 2 pistas)")
    print("  3. Dificil (4 intentos, 1 pista)")

    # BUCLE while: se repite hasta que el jugador escriba un número válido
    while True:
        opcion = input("\nEscribe el número de tu elección: ")

        if opcion == "1":
            return "facil"
        elif opcion == "2":
            return "medio"
        elif opcion == "3":
            return "dificil"
        else:
            print("Opción no válida. Escribe 1, 2 o 3.")

