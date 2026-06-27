Proyecto Integrador
El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas 
Autor: Alexander Sarmiento
Materia: Lógica de Programación
Objetivo del sistema
En esta oportunidad he desarrollado el Juego del Ahorcado desarrollado en Python que corre en la terminal. Donde el jugador elige una categoría de palabras y un nivel de dificultad, luego intenta adivinar la palabra oculta letra por letra antes de quedarse sin intentos. Cuenta con un sistema de pistas limitadas y lleva el registro de partidas y victorias durante la sesión. A medida que avanza el juego se va dibujando el muñeco del ahorcado si el jugador no acierta la letra.
El proyecto fue desarrollado como práctica de programación aplicando los conceptos básicos de Python: listas, tuplas, condicionales, bucles y funciones.

Descripción de funcionalidades
A continuación, se presentarán las funcionalidades que va a tener el juego; tales como categoría de palabras, dificultad ajustable, un sistema de pistas y el conteo de partidas y victorias. 

Funcionalidades

4 categorías de palabras: Animales, Países, Frutas, Tecnología
3 niveles de dificultad: fácil, medio y difícil (cambian los intentos y las pistas disponibles)
Sistema de pistas: cada palabra tiene una pista única, con usos limitados según la dificultad
Conteo de partidas: lleva el registro de partidas jugadas y victorias durante la sesión
Ahorcado en ASCII: el dibujo se actualiza con cada error cometido

¿Cómo se juega?
1.	Escribes tu nombre
2.	Eliges una categoría (Animales, Frutas, Países, Tecnología)
3.	Eliges una dificultad (Fácil, Medio, Difícil)
4.	El sistema elige una palabra al azar y la muestra con guiones
5.	Escribes letras una por una para adivinar la palabra
6.	Puedes escribir pista para recibir una ayuda (limitadas según dificultad)
7.	Puedes escribir salir para abandonar la partida

   Tabla de dificultades
Dificultad	Intentos	Pistas disponibles
Fácil        8      	3
Medio        6	      2
Difícil	     4	      1

Funcionalidades de Python usadas en el código

Listas — para guardar las letras usadas y la palabra oculta con guiones
Tuplas — para guardar cada palabra junto a su pista, y la configuración de cada dificultad
Diccionarios — para organizar las palabras por categoría y dificultad
if / elif / else — para tomar decisiones (letra correcta, letra repetida, pista, salir)
while — para repetir el juego mientras queden intentos y el jugador quiera seguir
for — para recorrer letras, mostrar la palabra oculta y las letras usadas

Instalación y uso
1. Clona el repositorio
Link: https://github.com/Alexsarmiento-ai/Aprendizaje-Autonomo-2
2. Ejecuta el juego
Python juego_ahorcado.py

Mejoras planeadas a futuro:

 Modo multijugador (un jugador elige la palabra, el otro adivina)
 Más categorías: deportes, películas, comidas
 Versión con interfaz gráfica usando Pygame


Gracias a la realización de este proyecto integrador he podido aplicar los fundamentos vistos en clase como condicionales, bucles, listas y las tuplas. Reforzando el conocimiento aprendido y siendo capaz de familiarizarme más con las herramientas que se utilizan en programación.
El poder desarrollar el Juego del Ahorcado me ayudo mucho a poder practicar todo lo que he visto en clase durante este tiempo. Es realmente gratificante ver como el conocimiento adquirido se puede aplicar en lineas de codigo, y que de eso pueda resultar un juego com este, hasta los software mas completos y complejos.

Fecha: 27/06/2026
