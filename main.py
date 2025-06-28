
# Importamos las funciones necesareas para este proyecto
import random
import os
import pyttsx3
import PySimpleGUI as sg
import time

# Iniciamos la libreria que da voz a la historia
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'spanish')

# Definimos el layout de la interfaz grafica
layout = [
    [sg.Text("Presiona el botón para crear una historia aleatoria:")],
    [sg.Button("¡Generar historia!")],
    [sg.Multiline("", size=(60, 5), key="-OUTPUT-", visible=False)]
]

# Iniciamos la ventana de la interfaz grafica
window = sg.Window("Generador de Historias", layout)


# Definimos la funcion que genera la historia
def get_history():
    characters = [
        "una científica que habla con los árboles",
        "un ninja torpe pero valiente",
        "un pato con jetpack",
        "una extraterrestre fan del reguetón",
        "un gato filósofo que odia los lunes",
        "una momia influencer",
        "un chef obsesionado con las nubes",
        "un esqueleto que toca el violín",
        "una niña que programa sueños",
        "un perro que quiere ser detective",
        "un ogro vegetariano con alergia al brócoli",
        "una cucaracha con sombrero de copa",
        "un robot que aprende a bailar salsa",
        "una bruja que fabrica caramelos mágicos",
        "un astronauta que teme a la oscuridad",
        "una hormiga que dirige una orquesta",
        "un vampiro alérgico a la sangre",
        "una sirena que canta heavy metal",
        "un fantasma con miedo a los humanos",
        "una nube que sueña con ser dragón",
        "un dragón que colecciona peluches",
        "un zombie que estudia medicina",
        "una estrella fugaz que hace grafitis",
        "un duende que roba calcetines",
        "un camaleón que cambia de idioma cuando se asusta"
    ]

    places = [
        "en una ciudad hecha de chicle",
        "dentro de una computadora antigua",
        "en una biblioteca infinita",
        "en una dimensión donde todo es al revés",
        "en un volcán convertido en parque de diversiones",
        "en un tren que nunca se detiene",
        "en un bosque donde llueve helado",
        "flotando en una burbuja sobre el océano",
        "en una isla donde todo flota",
        "en un pueblo que vive al revés",
        "en una fábrica de arcoíris",
        "en una cueva llena de espejos mágicos",
        "en el corazón de una estrella",
        "en un planeta donde solo viven gatos",
        "en una tienda abandonada que nunca cierra",
        "en una autopista del tiempo",
        "en una escuela de monstruos",
        "en una ciudad subterránea habitada por pingüinos",
        "dentro de un videojuego glitcheado",
        "en un circo volador sobre las nubes",
        "en un castillo invisible",
        "en un desierto que cambia cada noche",
        "en un río hecho de jugo de naranja",
        "en un laboratorio dentro de un árbol gigante",
        "en una estación espacial abandonada"
    ]

    problems = [
        "tiene que preparar una cena para dragones",
        "ha perdido su sombra y alguien más la usa",
        "está atrapado en una canción",
        "quiere resolver un misterio sin pistas",
        "busca el WiFi sagrado en una zona sin señal",
        "ha sido acusado injustamente de comerse la luna",
        "necesita entregar una pizza a través del tiempo",
        "debe recuperar un recuerdo que nunca vivió",
        "compite en una carrera interdimensional",
        "tiene que enseñar a hablar a las piedras",
        "tiene prohibido usar vocales por 24 horas",
        "ha sido elegido para gobernar por accidente",
        "descubre que es parte de un experimento secreto",
        "debe convencer a una planta carnívora de hacerse vegetariana",
        "intenta traducir el idioma de los grillos",
        "quiere abrir una cafetería en el Polo Norte",
        "debe aprender a volar sin alas",
        "encuentra una carta escrita por su yo del futuro",
        "despierta convertido en un mueble",
        "quiere crear el emoji perfecto",
        "ha intercambiado cuerpos con una rana",
        "debe superar un laberinto de espejos vivos",
        "intenta ganar un concurso de ronquidos mágicos",
        "descubre que su reflejo tiene vida propia",
        "quiere construir una ciudad en las nubes"
    ]
    return f"Una vez, {random.choice(characters)} que vivia {random.choice(places)} {random.choice(problems)}"


# Definimos la funcion que enseña la historia por pantalla
def show_history(window):
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "¡Generar historia!":
            history = get_history()
            window["-OUTPUT-"].update(history, visible=True)
            window.refresh()
            engine.say(history)
            engine.runAndWait()
    window.close()


# Definimos la funcion principal
def main():
    show_history(window)



# Ejecutamos la funcion principal si el programa es el principal
if __name__ == "__main__":
    main()
