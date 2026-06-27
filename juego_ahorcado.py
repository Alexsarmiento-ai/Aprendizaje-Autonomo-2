
#   JUEGO DEL AHORCADO
#   Materia: Logica de Programación
#   Autor  : Alexander Sarmiento
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
#  Un diccionario donde cada dificultad guarda una tupla con dos datos: intentos máximos y pistas disponibles. Los valores no cambian nunca, por eso se usan tuplas.
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
            

#  FUNCIÓN: mostrar el estado actual del juego   
#  Dibuja el estado del juego en pantalla: el muñeco, la palabra con guiones y las letras usadas. Usa un for para recorrer la lista letra por letra.        
 
def mostrar_estado(dibujos, errores, intentos_max, palabra_oculta, letras_usadas, pistas_disponibles, dificultad):
   
    # Mostramos el dibujo según cuántos errores llevamos y va cambiando de acuerdo a los mismos

    if intentos_max == 8:
        # En fácil hay 8 intentos pero solo 7 dibujos (0 al 6)
    
        indice_dibujo = int((errores / intentos_max) * 6)
    else:
        # En medio (6) y difícil (4) 
        indice_dibujo = min(errores, 6)
 
    print(dibujos[indice_dibujo])
 
    # Mostramos la dificultad e intentos restantes
    restantes = intentos_max - errores
    print(f"Dificultad: {dificultad.upper()}  |  Intentos restantes: {restantes} / {intentos_max}")
 
    # Mostramos la palabra con guiones y letras descubiertas
    # BUCLE for: recorremos cada elemento de la lista palabra_oculta
    print("\nPalabra: ", end="")
    for letra in palabra_oculta:
        print(letra + " ", end="")
    print()
 
    # Mostramos las letras ya usadas
    # CONDICIONAL: solo mostramos si ya se usaron letras
    if len(letras_usadas) > 0:
        print("\nLetras usadas:", end=" ")
        for letra in letras_usadas:
            print(letra.upper(), end=" ")
        print()
 
    print(f"\nPistas disponibles: {pistas_disponibles}")
 
 
#  FUNCIÓN: una ronda completa del juego del ahorcado
#  Aqui se cordina todo el funcionamiento del juego: llama a las funciones del menú, ejecuta las listas y ejecuta el while principal donde el jugador adivina letras una por una.
#  Retorna True si ganó, False si perdió

 
def jugar_ronda():
    # Paso 1: el jugador elige categoría y dificultad
    categoria  = elegir_categoria()
    dificultad = elegir_dificultad()
 
    # Paso 2: leemos la configuración de esa dificultad
    
    intentos_max       = config_dificultad[dificultad][0] 
    pistas_disponibles = config_dificultad[dificultad][1]  
 
    # Paso 3: el sistema elige una tupla al azar según categoría Y dificultad
    tupla_elegida = random.choice(palabras[categoria][dificultad])

    palabra = tupla_elegida[0]   # la palabra a adivinar
    pista   = tupla_elegida[1]   # la pista de esa palabra
 
    # Paso 4: Se inicia el estado del juego
    errores = 0   # el contador de errores empieza en cero
 
    # LISTA: letras que el jugador ya intentó
    letras_usadas = []
 
    # LISTA: la palabra oculta con guiones
    # BUCLE for: por cada letra de la palabra, ponemos un guion
    palabra_oculta = []
    for letra in palabra:
        palabra_oculta.append("_")
 
    print(f"\n¡Empezamos! Dificultad: {dificultad.upper()}")
    print(f"La palabra tiene {len(palabra)} letras y tienes {intentos_max} intentos.")
    print("Comandos: escribe una letra, 'pista' para pedir pista, o 'salir' para abandonar.")
 
    # Paso 5: BUCLE principal del juego
    # Se repite mientras queden intentos Y la palabra no esté completa
    while errores < intentos_max and "_" in palabra_oculta:
 
        # Mostramos el estado actual
        mostrar_estado(dibujos, errores, intentos_max, palabra_oculta, letras_usadas, pistas_disponibles, dificultad)
 
        # Pedimos una letra al jugador
        entrada = input("\nEscribe una letra: ").lower().strip()
 
        # CONDICIONAL: que elige el jugador 
 
        if entrada == "salir":
            print("\nAbandonaste la partida.")
            return False
 
        elif entrada == "pista":
            
            if pistas_disponibles > 0:
                pistas_disponibles = pistas_disponibles - 1
                print(f"\n💡 PISTA: {pista}")
            else:
                print("\nYa no te quedan pistas.")
 
        elif len(entrada) != 1 or not entrada.isalpha():
            # El jugador escribió algo que no es una sola letra
            print("\nEscribe solo UNA letra.")
 
        elif entrada in letras_usadas:
            # La letra ya fue usada antes
            print(f"\nYa usaste la letra '{entrada.upper()}'. Intenta con otra.")
 
        else:
            # Es una letra nueva y válida
            letras_usadas.append(entrada)   # la agregamos a la LISTA
 
            # CONDICIONAL: la letra está en la palabra?
            if entrada in palabra:
                print(f"\n✅ ¡Correcto! La letra '{entrada.upper()}' está en la palabra.")
 
                # BUCLE for: buscamos en qué posiciones está esa letra
                for i in range(len(palabra)):
                    if palabra[i] == entrada:
                        palabra_oculta[i] = entrada   # revelamos esa posición
 
            else:
                # La letra no está en la palabra → sumamos un error
                errores = errores + 1
                print(f"\n❌ La letra '{entrada.upper()}' no está en la palabra.")
 
    # Paso 6: el bucle termina y se revisa el por qué
    # CONDICIONAL: ganó o perdió?
    if "_" not in palabra_oculta:
        # No quedan guiones → el jugador adivinó toda la palabra
        mostrar_estado(dibujos, errores, intentos_max, palabra_oculta, letras_usadas, pistas_disponibles, dificultad)
        print("\n🎉 ¡GANASTE! Adivinaste la palabra correctamente.")
        return True
    else:
        # Se acabaron los intentos → el jugador perdió
        mostrar_estado(dibujos, errores, intentos_max, palabra_oculta, letras_usadas, pistas_disponibles, dificultad)
        print(f"\n💀 ¡PERDISTE! La palabra era: {palabra.upper()}")
        return False
 
 
#  PROGRAMA PRINCIPAL
#  ES LO QUE EL JUGADOR VE CUANDO EJECUTA EL PROGRAMA
#  Aquí empieza a ejecutarse todo
 
print("=" * 40)
print("      BIENVENIDO AL AHORCADO")
print("=" * 40)
 
nombre = input("\n¿Cuál es tu nombre? ")
print(f"\nHola, {nombre}. ¡Buena suerte!")
 
# Llevamos el conteo de partidas y victorias con variables simples
partidas  = 0
victorias = 0
 
# BUCLE while: se repite mientras el jugador quiera seguir jugando
seguir_jugando = True
 
while seguir_jugando:
 
    # Jugamos una ronda y guardamos si ganó o no
    gano = jugar_ronda()
 
    # Actualizamos los contadores
    partidas = partidas + 1
    if gano:
        victorias = victorias + 1
 
    # Mostramos el marcador
    print(f"\n📊 {nombre} — Partidas: {partidas}  Victorias: {victorias}")
 
    # Preguntamos si quiere jugar otra vez
    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower().strip()
 
    # CONDICIONAL: continuamos o salimos
    if respuesta == "s":
        seguir_jugando = True
    else:
        seguir_jugando = False
 
# Mensaje de despedida al salir del bucle
print(f"\n¡Hasta luego, {nombre}!")
print(f"Jugaste {partidas} partidas y ganaste {victorias}. ¡Gracias por jugar!")

