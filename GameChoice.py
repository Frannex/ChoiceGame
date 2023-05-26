# Juego: Kenny's Adventure
# Descripción: Un juego de supervivencia en un apocalipsis zombie.
# Instrucciones: El jugador toma decisiones para guiar al personaje principal a través de la historia y sobrevivir.
# Autor: Frannex
# Fecha: 26/5/2023 (ULTIMA MODIFICACIÓN)
#Version: ALPHA 1.0
#Primer proyecto de programacòn

import os #Biblioteca para borrar
import time #Biblioteca para el tiempo

#función que muestra mensajes
def mostrar_mensaje(mensaje):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()
    
#Funcion que muestra los riesgos que tomas
def posibilidad_supervivencia(posibilidad):
    for letra in posibilidad:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()

#Funcion que muestra la abundancia o escacez que hay de un producto
def abundancia_objeto(abundancia):
    for letra in abundancia:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()
    
#funcion para mostrar el aviso
def mostrar_aviso(aviso):
    for letra in aviso:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()

# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls') #cls comando para borrar pantalla

#Personajes
protagonista_nombre = "Kenny"
superviviente_nombreMisterioso= "Superviviente"
superviviente_nombre = "Carver"
superviviente_nombreMisterioso1= "Desconocido"
superviviente_nombre1 = "Lee"

#Conversacion entre personajes
def conversacion_personajes(conver):
    for letra in conver:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()
    
# Llamada a la función para limpiar la pantalla
limpiar_pantalla()

#funcion de repetir si no elige correctamente
def pedir_opcion(opciones): 
    while True: #Bucle 
        eleccion = input() #Digitar 
        if eleccion in opciones:
            return eleccion
        else:
            mostrar_mensaje("¡OPCIÓN INCORRECTA!")
            mostrar_mensaje("Elige entre " + ", ".join(opciones))

#Funcion de procesar mensaje (Efecto realista)
def mensaje_procesando():
    mostrar_mensaje("Procesando....")

#Funcion de
def mostrar_dialogo(texto):
    for letra in texto:
        print(letra, end='', flush=True)  # Imprime la letra sin saltar de línea
        time.sleep(0.05)  # Controla la velocidad de aparición de las letras
    print()  # Salta de línea después de imprimir el texto completo

#Funcion de aviso de juego (Te dice de que se trata el juego)
def aviso_juego():
    limpiar_pantalla()
    mostrar_aviso("Antes de empezar tu aventura....")
    mostrar_aviso("Tienes que saber que este juego trata de tomar decisiones.")
    mostrar_aviso("Abajo de las decisiones que haya tendras un porcentaje de posibilidad de sobrevivir.")
    mostrar_aviso("Mientras más alto sea el porcentaje, más posibilidades de sobrevivir vas a tener.")
    mostrar_aviso("Pero cuidado! En algunas opciones el porcentaje de sobrevivir es bajo pero tienes alta posibilidad de recompensa.")
    mostrar_aviso("Así que piensa bien la decisión antes de tomarla, ya que te podes beneficiar.")
    mostrar_aviso("Las acciones que tomes cambiarán el transcurso de la historia.")
    mostrar_aviso("Piensa bien lo que vas a hacer....")
    limpiar_pantalla()


#funcion con la cual empieza la historia
def introduccion(): 
    mostrar_mensaje("Bienvenidos a Kenny's Adventure.")
    mostrar_mensaje("Es el año 2022.")
    mostrar_mensaje("Es el fin del mundo.")
    mostrar_mensaje("Hace 4 meses empezó el apocalipsis zombie.")
    mostrar_mensaje("Eres Kenny, un joven de 17 años cuyos padres fueron devorados por los zombies.")
    mostrar_mensaje("Estás vagando en un antiguo pueblo abandonado.")
    mostrar_mensaje("Tu objetivo es sobrevivir la primera noche.")
    mostrar_mensaje("Encuentras una casa abandonada.")
    limpiar_pantalla()


#funcion si eliges la primera opción (1)
def opcion_1():
    mostrar_mensaje("Has decidido entrar en la casa.")
    mostrar_mensaje("Escuchas unos ruidos que provienen del segundo piso.")
    mostrar_mensaje("¿Qué haces?.")
    limpiar_pantalla()
    mostrar_mensaje("1. Sales corriendo de la casa.")
    posibilidad_supervivencia("Posibilidad de sobrevivir: 50%.")
    mostrar_mensaje("2. Sales sigilosamente de la casa.")
    posibilidad_supervivencia("Posibilidad de sobrevivir: 20%.")
    mostrar_mensaje("3. Decides ir a investigar qué pasa.")
    posibilidad_supervivencia("Posibilidad de sobrevivir: 35%. Pero alta posibilidad de recibir recompensa.")
    eleccion2 = pedir_opcion(["1", "2", "3"])
    limpiar_pantalla()
    #salir corriendo de la casa
    if eleccion2 == "1":
        mostrar_mensaje("Decides salir corriendo de la casa.")
        mostrar_mensaje("Al salir corriendo haces mucho ruido y algo parece haberte escuchado.")
        mostrar_mensaje("Mientras estás corriendo, decides mirar hacia atrás.")
        mostrar_mensaje("¡ES UN ZOMBIE QUE ESTÁ A PUNTO DE COMERTE!.")
        mostrar_mensaje("¿QUÉ HACES?.")
        limpiar_pantalla()
        mostrar_mensaje("1. SACAS EL CUCHILLO DE TU CINTURA.")
        mostrar_mensaje("2. SIGUES CORRIENDO.")
        eleccion3 = pedir_opcion(["1", "2"])
        limpiar_pantalla()
        #sacar cuchillo
        if eleccion3 == "1":
            mostrar_mensaje("ELEGISTE SACAR EL CUCHILLO DE TU CINTURA.")
            mostrar_mensaje("LO ACUCHILLAS AL ZOMBIE PERO NO ES SUFICIENTE.")
            mostrar_mensaje("¿¿¿¿QUÉ VAS A HACER?????.")
            limpiar_pantalla()
            mostrar_mensaje("1. Te rindes.")
            posibilidad_supervivencia("Posibilidad de sobrevivir: 1%.") 
            mostrar_mensaje("2. Lo acuchillas de nuevo.")
            posibilidad_supervivencia("Posibilidad de sobrevivir: 65%.")
            eleccion4 = pedir_opcion(["1", "2"])
            limpiar_pantalla()
            #rendición del personaje(muerte)
            if eleccion4 == "1":
                mostrar_mensaje("Decides que no vale la pena seguir luchando.")
                mostrar_mensaje("¡HAS MUERTO!.") 
                manejar_partida(True)
                return
            #intentar acuchillar devueltar al zombie (sobrevivis)
            elif eleccion4 == "2":
                mostrar_mensaje("DECIDIS DAR TU ÚLTIMO INTENTO.")
                mostrar_mensaje("LOGRAS ACABAR CON EL ZOMBIE.")
                mostrar_mensaje("HAS LOGRADO SOBREVIVIR, FELICITACIONES!.")
                limpiar_pantalla()
                mostrar_mensaje("Luego de haber sobrevivido milagrosamente al ataque del zombie decides alejarte del pueblo por las dudas y te diriges al bosque.")
                mostrar_mensaje("Ya en el bosque casi siendo el atardecer empezas a plantearte donde podes quedarte a la noche.")
                mostrar_mensaje("Pensando en tu proximo plan a lo mejos milagrosamente ves un arbol de manzana.")
                mostrar_mensaje("Decides comer un par de manzanas para regenerar tu energia, ya que has pasado muchos dias sin comer.")
                mostrar_mensaje("Ya es de noche y llegas a una especie de granja abandonada.")
                mostrar_mensaje("¿Que haces?.")
                limpiar_pantalla()
                mostrar_mensaje("1. Seguir caminando")
                posibilidad_supervivencia("Posibilidad de sobrevivir: 35%.") 
                mostrar_mensaje("2. Te refugias en la granja abandonada")
                posibilidad_supervivencia("Posibilidad de sobrevivir: 45%.") 
                eleccion6 = pedir_opcion(["1", "2"])
                limpiar_pantalla()
                #seguir caminando
                if eleccion6 == "1":
                    mostrar_mensaje("Has elegido seguir caminando.")
                    mostrar_mensaje("Esta todo oscuro así que decides ver en tu mochila si tenes algo.")
                    mostrar_mensaje("¿Que vas a agarrar?.")
                    limpiar_pantalla()
                    mostrar_mensaje("1. Encendedor con poco gas.")
                    abundancia_objeto("El encendedor esta muy usado. Alta posibilidad de que se quede sin gas.")
                    mostrar_mensaje("2. 3 Fosforos.")
                    abundancia_objeto("Escacez de fosforos. Alta posibilidad de quedarse sin fosforos.")
                    mostrar_mensaje("3. Linterna casi sin pilas.")
                    abundancia_objeto("Escacez de pila para la lintera. Alta posibilidad que te quedes sin linterna.")
                    eleccion7 = pedir_opcion(["1", "2","3"])
                    limpiar_pantalla()
                    #usar encendedor
                    if eleccion7 == "1":
                        mostrar_mensaje("Has elegido usar el encencedor.")
                        mostrar_mensaje("Tu campo de visión es medio pero algo es algo.")
                        mostrar_mensaje("Sigues caminando hasta que a 4 metros de tu derecha ves lo que parece ser una llanta.")
                        mostrar_mensaje("Siguiendo ves una silueta de lo que parece ser un auto medio chocado en la cuneta.")
                        mostrar_mensaje("¿Que haces?.")
                        mostrar_mensaje("1. Te acercas a la silueta.")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 33%. Alta posibilidad de recompensa") 
                        mostrar_mensaje("2. Te alejas.")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 67%.") 
                        eleccion8 = pedir_opcion(["1", "2"])
                        limpiar_pantalla()
                        #acercarte
                        if eleccion8 == "1":
                            mostrar_mensaje("Has elegido acercarte a la silueta del auto.")
                            mostrar_mensaje("¿Antes de acercarte que haces?.")
                            mostrar_mensaje("1. Sacar el cuchillo")                            
                            mostrar_mensaje("2. No sacar el cuchillo")
                            eleccion9 = pedir_opcion(["1", "2"])
                            limpiar_pantalla()
                            #sacar cuchillo
                            if eleccion9=="1":
                                mostrar_mensaje("Has elegido sacar el cuchillo por las dudas.")
                                mostrar_mensaje("Te acercas y...........")
                                mostrar_mensaje("No hay peligro. Gracias a Dios!")
                                mostrar_mensaje("Empiezas a revisarr el auto y...")
                                mostrar_mensaje("Haz encontrado un rifle con mira!.")
                                mostrar_mensaje("Ahora podras cazar y defenderte.")
                                mostrar_mensaje("Lo malo es que tiene una bala. ")
                                mostrar_mensaje("¿Que vas a hacer?.")
                                limpiar_pantalla()
                                mostrar_mensaje("1. Seguir buscando.")
                                mostrar_mensaje("2. Retirarse.")
                                eleccion10 = pedir_opcion(["1", "2"])
                                limpiar_pantalla()
                                if eleccion10=="1":
                                    mostrar_mensaje("Has elegido seguir buscando")
                                    mostrar_mensaje("Al principio no encuentras nada pero...")
                                    mostrar_mensaje("Has encontrado una especie de bolso.")
                                    mostrar_mensaje("Al revisarlo has encontrado 8 balas del rifle y además una lata de arveja.")
                                    mostrar_mensaje("Ahora tenes que tomar una decisión.")
                                    limpiar_pantalla()
                                    mostrar_mensaje("1. Pasar la noche en el auto")
                                    posibilidad_supervivencia("Posibilidad de sobrevivir: 25.4%.") 
                                    mostrar_mensaje("2. Seguir caminando en plena noche")
                                    posibilidad_supervivencia("Posibilidad de sobrevivir: 16.3%.") 
                                    eleccion11 = pedir_opcion(["1", "2"])
                                    limpiar_pantalla()
                                    #sobrevivis la noche
                                    if eleccion11:
                                        mostrar_mensaje("Has decidido pasar la noche en el auto.")
                                        mostrar_mensaje("Sin duda muy arriesgado.")
                                        mostrar_mensaje("Cierras los ojos y rezas aparecer vivo al día siguiente.")
                                        mostrar_mensaje("A la media hora de haberte dormido unos ruidos te despiertan.")                                       
                                        mostrar_mensaje("Al mirar por la ventana del auto tu sangre se congela.")
                                        mostrar_mensaje("Debido a que era una horda de zombies enfrente tuya.")
                                        mostrar_mensaje("Entonces decides tirarte en el suelo del auto y taparte con una especie de manta.")
                                        mostrar_mensaje("Empiezas a rezar que no te encuentren.")
                                        mostrar_mensaje("Pero por suerte del destino no se percataron de vos.")
                                        mostrar_mensaje("Felicidades! Has pasado la noche.")
                                        manejar_partida(True)
                                        return
                                    #moris debido a la horda y te quedas sin encendedor
                                    if eleccion11:
                                        mostrar_mensaje("Decides seguir caminando en plena noche.")
                                        mostrar_mensaje("Al pasar media hora tu encendedor se queda sin gas y estas en la completa oscuridad.")
                                        mostrar_mensaje("Empiezas a escuchar muchos sonidos raros.")
                                        mostrar_mensaje("Resulta ser una horda de zombies!.")
                                        mostrar_mensaje("Al estar en completa oscuridad no puedes saber donde estan.")
                                        mostrar_mensaje("Pero en un momento inesperado sientes que unos dientes se clavan en tu cuello.")
                                        mostrar_mensaje("Es un zombie que te esta devorando.")
                                        mostrar_mensaje("¡Has muerto!.")
                                        manejar_partida(True)
                                        return
                            #morir debido a la horda pero con el encendeor
                            if eleccion10=="2":
                                mostrar_mensaje("Has elegido alejarte de la silueta del auto.")
                                mostrar_mensaje("Al pasar 25 minutos empiezas a escuchar sonidos raros.")
                                mostrar_mensaje("Cuando visualizas con el poco gas que le quedaba a tu encendedor te das cuenta que es una manada de zombies.")
                                mostrar_mensaje("Te congelas del miedo.")
                                mostrar_mensaje("Pero cuando por fin reaccionas, los zombies te atacan.")
                                mostrar_mensaje("¡Has muerto!.")
                                manejar_partida(True)
                                return
                    #usar encendedor                                    
                    if eleccion7 == "1":
                        mostrar_mensaje("Has elegido usar los fosforos.")    
                        mostrar_mensaje("Tu campo de visión es muy bajo.")
                        mostrar_mensaje("Por lo que seguis caminando por la ruta sin ver a los costados.")
                        mostrar_mensaje("Durante 15 minutos caminas hasta que te cansas y decides reintregarte al bosque.")
                        mostrar_mensaje("Justo cuando entras al bosque a lo lejos escuchas lo que parece ser una horda de zombies.")
                        mostrar_mensaje("Menos mal que decidiste integrarte al bosque.")
                        mostrar_mensaje("Si hubieses seguido por la ruta, hubieses muerto.")
                        limpiar_pantalla()
                        mostrar_mensaje("Caminas por el bosque durante un buen rato.")
                        mostrar_mensaje("Sin dudas caminar por el bosque sin luz no es lo mejor.")
                        mostrar_mensaje("Tomas una decisión.")
                        limpiar_pantalla()
                        mostrar_mensaje("1. Subirte arriba de un arbol y pasar la noche allí.")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 5.4%.") 
                        mostrar_mensaje("2. Seguir caminando en plena noche")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 0.3%.") 
                        eleccion12 = pedir_opcion(["1", "2"])
                        limpiar_pantalla()
                        #pasar noche en el arbol (sobrevivis)
                        if eleccion12=="1":
                            mostrar_mensaje("Has elegido pasar la noche arriba de un arbol.")
                            mostrar_mensaje("No es demasiado comodo pero por lo menos podes dormir.")
                            mostrar_mensaje("Decides dormir.")
                            mostrar_mensaje("Despiertas al dia siguiente.")
                            mostrar_mensaje("Has sobrevivido la noche!.")
                            manejar_partida(True)
                            return
                        
                        #seguir caminando por el bosque (muerte 100% asegurada)
                        elif eleccion12=="2":
                            mostrar_mensaje("Has decidido seguir caminando por el bosque.")
                            mostrar_mensaje("Durante media hora caminas sin rumbo y en plena oscuridad.")
                            mostrar_mensaje("Cuando....")
                            mostrar_mensaje("Sin querer y debido a la oscuridad te atrapa una trampa para osos en el pie.")
                            mostrar_mensaje("Empiezas a gritar debido al gran dolor que estas sintiendo.")
                            mostrar_mensaje("Intentas librarte pero no puedes, ya que no ves nada.")
                            mostrar_mensaje("Tu grito atraen la atención de un par de zombies que rondaban en el bosque.")
                            mostrar_mensaje("Tienes 2 opciones.")
                            limpiar_pantalla()
                            mostrar_mensaje("1. Clavarte tu cuchillo en la garganta para no ser devorado brutalmente por los zombies.")
                            posibilidad_supervivencia("Posibilidad de sobrevivir: 0%.") #Te suicidas
                            mostrar_mensaje("2. Intentar liberarte de la trampa")
                            posibilidad_supervivencia("Posibilidad de sobrevivir: 0.4%.") #Te devoran
                            eleccion13 = pedir_opcion(["1", "2"])
                            limpiar_pantalla()
                            #suicidio
                            if eleccion13=="1":
                                mostrar_mensaje("Has decidido clavarte tu cuchillo en la garganta.")
                                mostrar_mensaje("Lo haces, ya que no queres morir en agonia.")
                                mostrar_mensaje("¡Te has suicidado!")
                                manejar_partida(True)
                                return
                            #masacrado
                            elif eleccion13=="2":
                                mostrar_mensaje("Decides seguir intentando luchar por tu vida.")
                                mostrar_mensaje("Pero es imposible, no lográs liberarte.")
                                mostrar_mensaje("Los zombie te masacran brutalmente.")
                                mostrar_mensaje("¡Has sido devorado!.")
                                manejar_partida(True)
                                return                                
                    #Usas la linterna
                    if eleccion7 == "3":
                        mostrar_mensaje("Has elegido usar la linterna.")
                        mostrar_mensaje("Tu campo de visión es alto, pero recuerda, tienes poca bateria.")
                        mostrar_mensaje("Usala bien.")
                        mostrar_mensaje("Empiezas a caminar por la ruta con tu linterna de largo alcance.")
                        mostrar_mensaje("Luego de caminar por un rato, notás que a tu izquierda a lo lejos hay un tipo de galpon.")      
                        mostrar_mensaje("Vas a tener que tomar una decisión.")
                        limpiar_pantalla()      
                        mostrar_mensaje("1. Investigar el galpon") 
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 27%.")     
                        mostrar_mensaje("2. Seguir tu camino")  
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 34%.")    
                        eleccion14 = pedir_opcion(["1", "2"])
                        limpiar_pantalla()
                        #Investigar el galpon
                        if eleccion14=="1":
                            mostrar_mensaje("Has elegido investigar el galpon.")
                            mostrar_mensaje("Parece estar abandonado pero quien sabe, puede haber alguien dentro.")
                            mostrar_mensaje("Sacas tu cuchillo, te armas de valor y decides entrar.")
                            mostrar_mensaje("Al entrar no hay nada.")
                            mostrar_mensaje("Entonces, decidis investigar con la poca bateria que le queda en tu linterna.")
                            mostrar_mensaje("Felicidades! Has encontrado un machete, parece estar muy filoso.")
                            mostrar_mensaje("¿Cuál es tu siguiente paso?.")
                            limpiar_pantalla()
                            mostrar_mensaje("1. Quedarse en el galpon")
                            posibilidad_supervivencia("Posibilidad de sobrevivir: 26%.")
                            mostrar_mensaje("2. Seguir tu camino")
                            posibilidad_supervivencia("Posibilidad de sobrevivir: 16.4%.")
                            eleccion15 = pedir_opcion(["1", "2"])
                            limpiar_pantalla()
                            if eleccion15=="1":
                                mostrar_mensaje("Has decidido pasar la noche en el galpón.")
                                mostrar_mensaje("Te duermes.")
                                mostrar_mensaje("Es la madrugada cuando un ruido te despierta.")
                                mostrar_mensaje("Te levantas y ves a una persona desconocida apuntandote con un arma.")
                                conversacion_personajes(f"{superviviente_nombreMisterioso}: NO MUEVAS UN SOLO PELO.")
                                conversacion_personajes(f"{superviviente_nombreMisterioso}: ¿QUE CARAJO ESTÁS HACIENDO?.")
                                conversacion_personajes(f"{protagonista_nombre}: Ey, ey, tranquilo!")
                                conversacion_personajes(f"{superviviente_nombreMisterioso}: ¿Eres uno de esos putos bandidos verdad?")
                                mostrar_mensaje("De que manera entablas conversación con el superviviente?.")
                                mostrar_mensaje("1. De forma calmada.")
                                mostrar_mensaje("2. De forma agresiva.")
                                eleccion19 = pedir_opcion(["1", "2"])
                                limpiar_pantalla()
                                #hablar de forma tranquila
                                if eleccion19=="1":
                                    conversacion_personajes(f"{protagonista_nombre}: Escucha amigo, disculpame!.")
                                    conversacion_personajes(f"{protagonista_nombre}: Porfavor, no dispares.")
                                    conversacion_personajes(f"{protagonista_nombre}: No sabia que este galpón estas abandonado.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: ¿TE PENSAS QUE SOY IDIOTA?.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: VIENES A ROBARME.")
                                    conversacion_personajes(f"{protagonista_nombre}: Hablemos, porfavor.")
                                    conversacion_personajes(f"{protagonista_nombre}: Mi nombre es Kenny, ¿Cual es el tuyo?.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: ....")
                                    conversacion_personajes(f"{protagonista_nombre}: Porfavor, no dispares, tranquilizate.")
                                    conversacion_personajes(f"{protagonista_nombre}: No quiero morir.")
                                    mostrar_mensaje("El superviviente baja el arma.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: ¿Seguro que no eres un bandido?")
                                    conversacion_personajes(f"{protagonista_nombre}: Te lo juro.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Disculpame chico.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: La semana pasada una banda de bandidos vino a este refugio.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Y me intentaron robar las cosas.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Claro, no lo lograron.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Ya que asesine a uno de esos hijos de puta.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Y los otros salieron corrieron.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Mi nombre es Carver, un placer conocerte.")
                                    conversacion_personajes(f"{protagonista_nombre}: Un placer conocerlo Carver.")
                                    conversacion_personajes(f"{protagonista_nombre}: Si no es mucha molestia, podria pasar la primera noche aquí.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: .....")
                                    conversacion_personajes(f"{protagonista_nombre}: Porfavor, solo esta noche, a la mañana siguiente me retirare.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: Más te vale no intentar nada.")
                                    conversacion_personajes(f"{protagonista_nombre}: Muchisimas gracias señor.")
                                    mostrar_mensaje("Has pasado la noche en el galpón")
                                    mostrar_mensaje("Has sobrevivido la primera noche")
                                    manejar_partida(True)
                                    return
                                #hablar de forma agresiva
                                elif eleccion19=="1":
                                    conversacion_personajes(f"{protagonista_nombre}: Baja la puta arma ahora!.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: ¿¡TE CREES QUE ESTOY BROMEANDO IMBECIL?!.")
                                    conversacion_personajes(f"{protagonista_nombre}: No tenes los suficientes huevos.")
                                    conversacion_personajes(f"{protagonista_nombre}: He conocido asesinos, vos no tenes pinta de ser uno de esos.")
                                    mostrar_mensaje("Procedes a levantarte.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: QUIETO IMBECIL! O VOY A DISPARAR?")
                                    conversacion_personajes(f"{protagonista_nombre}: No te da pedazo de pelotudo.")
                                    mostrar_mensaje("Lo ignoras y seguis acercandote.")
                                    conversacion_personajes(f"{superviviente_nombreMisterioso}: ¡QUIETO, NO LO VOY A REPETIR UNA VEZ MÁS.")
                                    mostrar_mensaje("¿Que vas a hacer.")
                                    mostrar_mensaje("1. Sacas tu cuchillo y lo atacas.")
                                    mostrar_mensaje("2. Te acercas un poco más.")
                                    eleccion20 = pedir_opcion(["1", "2"])
                                    limpiar_pantalla()
                                    #Matar a carver
                                    if eleccion20=="1":
                                        mostrar_mensaje("Procedes a atacarlo.")
                                        mostrar_mensaje("Te dispara pero erra todos los tiros.")
                                        mostrar_mensaje("Le clavas el cuchillo en el corazón.")
                                        mostrar_mensaje("Lo matas.")
                                        mostrar_mensaje("Revisas su cuerpo y agarras las cosas utiles de él.")
                                        mostrar_mensaje("Con tus pocas fuerzas moves el cuerpo hacia afuera para que no haya olor.")
                                        mostrar_mensaje("Pasas la noche en el galpón.")
                                        mostrar_mensaje("Has sobrevivido la primera noche.")
                                        manejar_partida(True)
                                        return
                                    
                                    elif eleccion20=="2":
                                        mostrar_mensaje("Procedes a acertarte un poco más.")
                                        conversacion_personajes(f"{superviviente_nombreMisterioso}: ¡TE LO HE ADVERTIDO!.")
                                        mostrar_mensaje("Te acribilla.")
                                        mostrar_mensaje("¡HAS SIDO ASESINADO!.")
                                        manejar_partida(True)
                                        return     
                                        
                                        
                            #seguis por tu camino
                            elif eleccion15=="2":
                                mostrar_mensaje("Has decidido seguir por tu camino ")
                                mostrar_mensaje("Estas un buen rato caminando en el bosque hasta que...")
                                mostrar_mensaje("Escuchas un disparo en el bosque")
                                mostrar_mensaje("Decides ir a investigar")
                                mostrar_mensaje("Te escondes detras de un arbol.")
                                mostrar_mensaje("Visualizas a un superviviente el cuál esta luchando contra 4 zombies.")
                                mostrar_mensaje("¿Que acción vas a tomar?")
                                limpiar_pantalla()
                                mostrar_mensaje("1. Vas a ayudarlo ")
                                posibilidad_supervivencia("Posibilidad de sobrevivir: 34%. Alta posibilida de recompensa")
                                mostrar_mensaje("2. Lo ignoras y seguis tu camino ") 
                                posibilidad_supervivencia("Posibilidad de sobrevivir: 36%")
                                eleccion16 = pedir_opcion(["1", "2"])
                                limpiar_pantalla()
                                
                                #ayudar al superviviente
                                if eleccion16=="1":
                                    mostrar_mensaje("Decides ayudarlo")
                                    limpiar_pantalla()
                                    mostrar_mensaje("¿Que armas vas a usar? ")
                                    mostrar_mensaje("1. Machete ")
                                    mostrar_mensaje("2. Cuchillo ")
                                    eleccion16 = pedir_opcion(["1", "2"])
                                    limpiar_pantalla()
                                    if eleccion16=="1":
                                        mostrar_mensaje("Has decidido usar el machete.")
                                        limpiar_pantalla()
                                        mostrar_mensaje("Salis de tu escondite y te dirigis a los zombies.")
                                        mostrar_mensaje("Matas a 2 de ellos y el otro superviviente mata a los otros 2.")
                                        mostrar_mensaje("Te agradece por salvarlo.")
                                        mostrar_mensaje("De que manera entablas conversación con el superviviente?.")
                                        limpiar_pantalla()
                                        mostrar_mensaje("1. De forma amable.")
                                        mostrar_mensaje("2. De forma agresiva.")
                                        mostrar_mensaje("3. Lo asesinas para robarle el fusil de asalto que tiene.")
                                        eleccion17 = pedir_opcion(["1", "2"])
                                        limpiar_pantalla()
                                        
                                        #de forma amable
                                        if eleccion17=="1":
                                            conversacion_personajes(f"{protagonista_nombre}: ¿Estas lastimado.?")
                                            conversacion_personajes(f"{superviviente_nombreMisterioso}: Gracias a Dios no, sino hubieses por vos seguro ya no estaria aqui.")
                                            conversacion_personajes(f"{protagonista_nombre}: ¿Como te llamas?.")
                                            conversacion_personajes(f"{superviviente_nombreMisterioso}: Mi nombre es Carver. Un placer, ¿el tuyo?")
                                            conversacion_personajes(f"{protagonista_nombre}: Kenny, un placer encontrar una cara amigable.")
                                            conversacion_personajes(f"{superviviente_nombre}: Luces algo joven.")
                                            conversacion_personajes(f"{protagonista_nombre}: Tengo 17 años.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿¿17 AÑOS??. ¿Donde estan tus padres pibe?.")
                                            conversacion_personajes(f"{protagonista_nombre}: Han sido devorados por lo zombies.")
                                            conversacion_personajes(f"{superviviente_nombre}: Oh.")
                                            conversacion_personajes(f"{superviviente_nombre}: Lamento escuchar eso.")
                                            conversacion_personajes(f"{protagonista_nombre}: Es el apocalipsis. Todos perdemos personas.")
                                            conversacion_personajes(f"{superviviente_nombre}: Oye, usas muy bien ese machete.")
                                            conversacion_personajes(f"{superviviente_nombre}: Sin dudas antes de esto habras sido un Samurai.")
                                            conversacion_personajes(f"{protagonista_nombre}: Muchas gracias por el halago.")
                                            conversacion_personajes(f"{protagonista_nombre}: La verdad es, que la acabo de encontrar en un galpon abandonado.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿Dijiste galpón abandonado?.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿Hablas de uno a unos minutos de aqui?.")
                                            conversacion_personajes(f"{protagonista_nombre}: Emmmm.")
                                            conversacion_personajes(f"{protagonista_nombre}: Si, ¿Porque preguntas?.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¡Es mi refugio!.")
                                            conversacion_personajes(f"{superviviente_nombre}: Ese machete seguro es el que le pertenecia mi padre jaja!.")
                                            conversacion_personajes(f"{protagonista_nombre}: DIOS.")
                                            conversacion_personajes(f"{protagonista_nombre}: ¡PERDON!")
                                            conversacion_personajes(f"{protagonista_nombre}: No era mi intención robartelo!")
                                            conversacion_personajes(f"{protagonista_nombre}: Es que el lugar parecia abandonado y....")
                                            conversacion_personajes(f"{superviviente_nombre}: Che, no te hagas drama.")
                                            conversacion_personajes(f"{superviviente_nombre}: Quedatelo.")
                                            conversacion_personajes(f"{superviviente_nombre}: Después de haberme salvado, es lo minimo que te puedo recompensar.")
                                            conversacion_personajes(f"{protagonista_nombre}: ¡Muchas gracias!.")
                                            conversacion_personajes(f"{superviviente_nombre}: Yo diria de ir a mi refugio.")
                                            conversacion_personajes(f"{superviviente_nombre}: Estar en pleno bosque de noche, no se si es buena idea.")
                                            conversacion_personajes(f"{protagonista_nombre}: ¿Estas seguro que no tenes problema que me quede con vos?.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¡Por supuesto que no, has salvado mi vida!.")
                                            conversacion_personajes(f"{protagonista_nombre}: Bueno. Muchisimas gracias!")
                                            mostrar_mensaje("Vuelven al galpón y pasas la noche ahi.")
                                            mostrar_mensaje("Felicidades! Has sobrevivido la primer noche.")
                                            manejar_partida(True)
                                            return
                                            
                                            #de forma agresiva
                                        elif eleccion17=="2":
                                            conversacion_personajes(f"{superviviente_nombreMisterioso}: Has salvado mi vida! Muchisimas gracias.")
                                            conversacion_personajes(f"{protagonista_nombre}: Casi haces que me maten por salvarte, maldito imbecil.")
                                            conversacion_personajes(f"{superviviente_nombreMisterioso}: Disculpame...")
                                            conversacion_personajes(f"{superviviente_nombreMisterioso}: Soy Carver.¿Cual es tu nombre?")
                                            conversacion_personajes(f"{protagonista_nombre}: Que te importa.")
                                            conversacion_personajes(f"{superviviente_nombre}: Oye, nadie te obligo que me salvaras la vida.")
                                            conversacion_personajes(f"{protagonista_nombre}: Lo hice por principios, no voy a dejar que asesinen a otro humano.")
                                            conversacion_personajes(f"{protagonista_nombre}: Aunque claramente, a cambio me tenes que dar tu rifle de asalto.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿Que carajos dices?.")
                                            conversacion_personajes(f"{protagonista_nombre}: Ya me escuchaste.")
                                            conversacion_personajes(f"{protagonista_nombre}: He salvado tu vida, me debes eso.")
                                            limpiar_pantalla()
                                            mostrar_mensaje("Procedes a poner tu machete en su cuello")
                                            limpiar_pantalla()
                                            conversacion_personajes(f"{protagonista_nombre}: Dame tu rifle de asalto o veras.")
                                            conversacion_personajes(f"{superviviente_nombre}: Bueno, bueno.")
                                            conversacion_personajes(f"{superviviente_nombre}: Tranquilo, aqui lo tienes.")
                                            limpiar_pantalla()
                                            mostrar_mensaje("Te ha dado su rifle de asalto")
                                            limpiar_pantalla()
                                            conversacion_personajes(f"{protagonista_nombre}: Dame también tu mochila.")
                                            conversacion_personajes(f"{superviviente_nombre}: Ya veo porque me salvaste.")
                                            conversacion_personajes(f"{superviviente_nombre}: Simplemente querías robarme las cosas.")
                                            conversacion_personajes(f"{superviviente_nombre}: Maldito bandido de mierda.")
                                            conversacion_personajes(f"{protagonista_nombre}: Es el apocalipsis hermano.")
                                            mostrar_mensaje("Toma una decisión")
                                            mostrar_mensaje("1. Lo asesinas")
                                            posibilidad_supervivencia("Posibilidad de sobrevivir: 75%")
                                            mostrar_mensaje("2. Lo dejas vivir")
                                            posibilidad_supervivencia("Posibilidad de sobrevivir: 56%")
                                            eleccion18 = pedir_opcion(["1", "2"])
                                            limpiar_pantalla()
                                            #matar a Carver
                                            if eleccion18=="1":
                                                conversacion_personajes(f"{protagonista_nombre}: Lo siento amigo.")
                                                conversacion_personajes(f"{protagonista_nombre}: Pero no puedo dejarte vivo.")
                                                conversacion_personajes(f"{superviviente_nombre}: Porfavor, te lo ruego.")
                                                conversacion_personajes(f"{superviviente_nombre}: No me asesines.")
                                                mostrar_mensaje("Le apuntas en la cabeza")
                                                mostrar_mensaje("Procedes a asesinarlo")
                                                mostrar_mensaje("Carver ha muerto.")
                                                limpiar_pantalla()
                                                mostrar_mensaje("Decides volver al galpón debido a la situación peligrosa del bosque.")
                                                mostrar_mensaje("Pasas la noche ahi.")
                                                mostrar_mensaje("Felicidades, has sobrevivido la primer noche!.")
                                                manejar_partida(True)
                                                return
                                                
                                                
                                            #perdonar a Carver
                                            elif eleccion18=="2":
                                                conversacion_personajes(f"{protagonista_nombre}: Andate lejos de acá.")
                                                conversacion_personajes(f"{protagonista_nombre}: Espero que no te vuelva a ver.")
                                                conversacion_personajes(f"{superviviente_nombre}: Vete al carajo.")
                                                mostrar_mensaje("Carver procede a levantarse.")
                                                mostrar_mensaje("Se va por el bosque.")
                                                mostrar_mensaje("Desaparece de tu vista.")
                                                limpiar_pantalla
                                                mostrar_mensaje("Debido a que corres riesgo de que Carver intente vengarse de vos decides volver al galpón.")
                                                mostrar_mensaje("Pasas la noche en el galpón.")
                                                mostrar_mensaje("Sobrevives la primera noche.")
                                                manejar_partida(True)
                                                return
                                        #matar a carver
                                        elif eleccion17=="3":
                                            conversacion_personajes(f"{superviviente_nombre}: Muchas gracias por salvarme!.")
                                            conversacion_personajes(f"{protagonista_nombre}: No hay de que amigo.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿Como puedo pagarte?.")
                                            conversacion_personajes(f"{protagonista_nombre}: Ya lo has hecho.")
                                            conversacion_personajes(f"{superviviente_nombre}: ¿Disculpame?.")
                                            mostrar_mensaje("Procedes a clavar tu machete en su cabeza.")
                                            mostrar_mensaje("Empiezas a machetearlo muchas veces.") 
                                            mostrar_mensaje("¡Has asesinado a Carver!.") 
                                            mostrar_mensaje("¡Has obtenido un fusil de asalto.") 
                                            mostrar_mensaje("Tomas su mochila y la abres.") 
                                            mostrar_mensaje("¡Has obtenido dos latas de arveja!.") 
                                            mostrar_mensaje("Decides volver al galpón para intentar sobrevivir.") 
                                            mostrar_mensaje("Sobrevives la primera noche.")
                                            manejar_partida(True)
                                            return
                                            
                                    elif eleccion16:
                                        mostrar_mensaje("Has decidido usar el cuchillo.")
                                        limpiar_pantalla()
                                        mostrar_mensaje("Sigilosamente te acercas por detrás de los zombies para matarlos.")
                                        mostrar_mensaje("Cuando estas apunto de matar a los zombies.")
                                        mostrar_mensaje("Recibes una bala perdida del superviviente.")
                                        mostrar_mensaje("Empiezas a gritar del dolor.")
                                        mostrar_mensaje("Un zombie te ataca y te asesina.")
                                        mostrar_mensaje("Los 3 zombies restantes atacan al superviviente y también lo asesinan.")
                                        mostrar_mensaje("¡Has muerto!.")
                                        mostrar_mensaje("¡El superviviente ha muerto!.")
                                        manejar_partida(True)
                                        return     
                                    
                                    #seguir tu camino(muerte)
                                    if eleccion16=="2":    
                                        mostrar_mensaje("Has elegido ignorarlo y seguir tu camino.")
                                        mostrar_mensaje("Justo cuando ibas a dejar el lugar.")
                                        mostrar_mensaje("El superviviente le erra un tiro a los zombies y te pega a vos.")
                                        mostrar_mensaje("Empiezas a sangrar muchisimo.")
                                        mostrar_mensaje("¡Has muerto desangradote!.")
                                        manejar_partida(True)
                                        return
                #Ir al a granja
                if eleccion6 == "2":
                    mostrar_mensaje("Has elegido ir a la granja.")
                    mostrar_mensaje("Decides sacar tu cuchillo.")
                    mostrar_mensaje("Abres la puerta y entras.")
                    mostrar_mensaje("Todo parece estar calmado hasta que.....")
                    conversacion_personajes(f"{superviviente_nombre1}: Movete y te disparo.")
                    limpiar_pantalla()
                    mostrar_mensaje("¿Como le vas a hablar al desconocido?.")
                    mostrar_mensaje("1. Calmado.")
                    posibilidad_supervivencia("Posibilidad de sobrevivir: 86%")
                    mostrar_mensaje("2. Agresivo.")
                    posibilidad_supervivencia("Posibilidad de sobrevivir: 56%")
                    eleccion21 = pedir_opcion(["1", "2"])
                    limpiar_pantalla()
                    #le hablas calmado
                    if eleccion21 == "1":
                        conversacion_personajes(f"{protagonista_nombre}: Tranquilo.")
                        conversacion_personajes(f"{superviviente_nombre1}: ¿Quien eres?.")
                        conversacion_personajes(f"{protagonista_nombre}: Me llamo Franco.")
                        conversacion_personajes(f"{protagonista_nombre}: Y quiero vivir.")
                        conversacion_personajes(f"{protagonista_nombre}: Tranquilo.")
                        conversacion_personajes(f"{protagonista_nombre}: ¿Como te llamas?.")
                        conversacion_personajes(f"{superviviente_nombreMisterioso1}: Me llamo Lee.")
                        conversacion_personajes(f"{superviviente_nombreMisterioso1}: Esta es mi granja.")
                        conversacion_personajes(f"{protagonista_nombre}: Escuchame Lee, te pido disculpas.")
                        conversacion_personajes(f"{protagonista_nombre}: Estaba buscando refugio, no sabia que esta era tu casa.")
                        conversacion_personajes(f"{superviviente_nombreMisterioso1}: Vuelve de donde viniste.")
                        mostrar_mensaje("Que vas a hacer?.")
                        mostrar_mensaje("1. Pedirle que te deje entrar")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 56%")
                        mostrar_mensaje("2. Asesinarlo.")
                        posibilidad_supervivencia("Posibilidad de sobrevivir: 46.4%")
                        eleccion22 = pedir_opcion(["1", "2"])
                        limpiar_pantalla()
                        #pedirle que te deje entrar
                        if eleccion22 == "1":
                            conversacion_personajes(f"{protagonista_nombre}: Porfavor, dejame entrar.")
                            conversacion_personajes(f"{protagonista_nombre}: Llevo dias sin poder comer bien y dormir.")
                            conversacion_personajes(f"{protagonista_nombre}: Dejame esta noche por lo menos.")
                            conversacion_personajes(f"{superviviente_nombreMisterioso1}: ¿Como se que no me vas a asesinar?.")
                            conversacion_personajes(f"{superviviente_nombreMisterioso1}: ¿Como se que no sos un asesino o un bandido?.")
                            conversacion_personajes(f"{protagonista_nombre}: Quedate con mi cuchilo, no me importa.")
                            conversacion_personajes(f"{protagonista_nombre}: Porfavor, te lo ruego.")
                            conversacion_personajes(f"{superviviente_nombreMisterioso1}: .....")
                            conversacion_personajes(f"{superviviente_nombreMisterioso1}: Entra, intenta hacer algo y te asesino.")
                            conversacion_personajes(f"{protagonista_nombre}: Muchas gracias, enserio, muchisimas gracias señor....")
                            conversacion_personajes(f"{superviviente_nombre1}: Lee.")
                            conversacion_personajes(f"{protagonista_nombre}: Un placer Lee, soy Kenny.")
                            limpiar_pantalla()
                            mostrar_mensaje("Has pasado la noche en la granja.")
                            mostrar_mensaje("Has sobrevivido la primer noche")
                            manejar_partida()
                            return
                        
                        #intentar asesesinarlo
                        elif eleccion22 == "2":
                            mostrar_mensaje("Sacas tu cuchillo de la cintura.")
                            mostrar_mensaje("Estas apunto de apuñarlo al superviviente.")
                            mostrar_mensaje("Pero el te dispara.")
                            mostrar_mensaje("¡Has sido asesinado!.")
                            manejar_partida(True)
                            return
                            
        #seguis corriendo (sobrevivis)
        elif eleccion3 == "2":
            mostrar_mensaje("Decides seguir corriendo.")
            mostrar_mensaje("Logras escapar del zombie por ahora.")
            manejar_partida(True)
            return
    #salir sigilosamente de la casa (sobrevivis)
    elif eleccion2 == "2":
        mostrar_mensaje("Decides salir sigilosamente de la casa.")
        mostrar_mensaje("Logras salir sin hacer ruido.")
        mostrar_mensaje("Sigues vagando por el pueblo en busca de raciones.")
        manejar_partida(True)
        return
    #decidir investigar que sucede
    elif eleccion2 == "3":
        mostrar_mensaje("Decides ir a investigar qué pasa.")
        mostrar_mensaje("Subes las escaleras del segundo piso.")
        mostrar_mensaje("En una esquina encuentras una mesa de luz.")
        mostrar_mensaje("La abris.")
        mostrar_mensaje("Has encontrado un revolver con 8 balas! Enhorabuena. Ha valido la pena subir al segundo piso.")
        mostrar_mensaje("Ahora estas armado.")
        mostrar_mensaje("Sigues recorriendo el segundo piso.")
        mostrar_mensaje("Encuentras una habitación cerrada.")
        mostrar_mensaje("¿Qué haces?.")
        limpiar_pantalla()
        mostrar_mensaje("1. Intentas abrir la puerta.")
        posibilidad_supervivencia("Posibilidad de sobrevivir: 50%.")
        mostrar_mensaje("2. Sales corriendo de la casa.")
        posibilidad_supervivencia("Posibilidad de sobrevivir: 50%.") 
        eleccion3 = pedir_opcion(["1", "2"])
        limpiar_pantalla()
        #intentar abrir la puerta (sobrevivis)
        if eleccion3 == "1":
            mostrar_mensaje("Intentas abrir la puerta pero está cerrada con llave.")
            mostrar_mensaje("Pero al hacer ruido el zombie se alerta.")
            mostrar_mensaje("Te escondes en el ropero de la casa.")
            mostrar_mensaje("El zombie sale de la casa corriendo a Dios sepa donde.")
            mostrar_mensaje("Logras escapar del peligro.")
            manejar_partida(True)
            return
        #salir corriendo de la casa
        elif eleccion3 == "2":
            mostrar_mensaje("Decides salir corriendo de la casa.")
            mostrar_mensaje("Al salir corriendo haces mucho ruido y algo parece haberte escuchado.")
            mostrar_mensaje("Mientras estás corriendo, decides mirar hacia atrás.")
            mostrar_mensaje("¡ES EL ZOMBIE QUE ESTÁ A PUNTO DE COMERTE!.")
            mostrar_mensaje("¿QUÉ HACES?")
            limpiar_pantalla()
            mostrar_mensaje("1. SACAS EL CUCHILLO DE TU CINTURA.")
            posibilidad_supervivencia("Posibilidad de sobrevivir: 34%.")
            mostrar_mensaje("2. SACAS EL REVÓLVER DE TU CINTURA.")
            posibilidad_supervivencia("Posibilidad de sobrevivir: 45%.")
            mostrar_mensaje("3. SIGUES CORRIENDO.")
            posibilidad_supervivencia("Posibilidad de sobrevivir: 23%.") 
            eleccion4 = pedir_opcion(["1", "2", "3"])
            limpiar_pantalla()
            #sacar cuchillo nuevamente de la cintura (muerte 100%)
            if eleccion4 == "1":
                mostrar_mensaje("ELEGISTE SACAR EL CUCHILLO DE TU CINTURA.")
                mostrar_mensaje("LO ACUCHILLAS AL ZOMBIE PERO NO ES SUFICIENTE.")
                mostrar_mensaje("¿¿¿¿QUÉ VAS A HACER?????.")
                limpiar_pantalla()
                mostrar_mensaje("1. Te rindes.")
                posibilidad_supervivencia("Posibilidad de sobrevivir: 1.5%.") 
                mostrar_mensaje("2. Lo acuchillas de nuevo.") 
                posibilidad_supervivencia("Posibilidad de sobrevivir: 33%.")
                eleccion5 = pedir_opcion(["1", "2"])
                limpiar_pantalla()
                #rendición (muerte)
                if eleccion5 == "1":
                    mostrar_mensaje("Decides que no vale la pena seguir luchando.") 
                    mostrar_mensaje("¡HAS MUERTO!.")
                    manejar_partida(True)
                    return
                #logras acuchillar al zombie devuelta (muerte x2)
                elif eleccion5 == "2":
                    mostrar_mensaje("DECIDIS DAR TU ÚLTIMO INTENTO.")
                    mostrar_mensaje("EL ZOMBIE TE ARRANCA UN PEDAZO DEL ESTOMAGO.")
                    mostrar_mensaje("PERO LOGRAS ACUCHILLARLO.")
                    mostrar_mensaje("LOGRAS ACABAR CON EL ZOMBIE.")
                    mostrar_mensaje("PERO LA HERIDA ES MUY GRAVE.")
                    mostrar_mensaje("¡HAS MUERTO!.")
                    manejar_partida(True)
                    return
            #sacar revolver
            elif eleccion4 == "2":
                mostrar_mensaje("ELEGISTE SACAR EL REVÓLVER DE TU CINTURA.")
                mostrar_mensaje("LE DISPARAS AL ZOMBIE.")
                mostrar_mensaje("PERO SOLO LO HERISTE.")
                mostrar_mensaje("¿¿¿¿QUÉ VAS A HACER?????.")
                limpiar_pantalla()
                mostrar_mensaje("1. Te rindes.")
                posibilidad_supervivencia("Posibilidad de sobrevivir: 4.3%.")
                mostrar_mensaje("2. Le disparas de nuevo.") 
                posibilidad_supervivencia("Posibilidad de sobrevivir: 65%.")
            
                eleccion5 = pedir_opcion(["1", "2"])
                limpiar_pantalla()
                #rendición (muerte)
                if eleccion5 == "1":
                    mostrar_mensaje("Decides que no vale la pena seguir luchando.")
                    mostrar_mensaje("¡HAS MUERTO!.")
                    manejar_partida(True)
                    return
                #dispararle nuevamente (sobrevivis)
                elif eleccion5 == "2":
                    mostrar_mensaje("DECIDIS DAR TU ÚLTIMO INTENTO.")
                    mostrar_mensaje("LE DISPARAS NUEVAMENTE.")
                    mostrar_mensaje("LOGRAS ACABAR CON EL ZOMBIE.")
                    mostrar_mensaje("¡FELICIDADES, HAS GANADO!.")
                    manejar_partida(True)
                    return
            #salir corriendo (muerte)
            elif eleccion4 == "3":
                mostrar_mensaje("DECIDES SEGUIR CORRIENDO.")
                mostrar_mensaje("PERO TE OLVIDASTE DE ALGO.")
                mostrar_mensaje("QUE LLEVAS DIAS SIN COMER BIEN Y DORMIR BIEN.")
                mostrar_mensaje("POR LO QUE NO ESTAS EN TU MEJOR MOMENTO.")
                mostrar_mensaje("EL ZOMBIE TE ALCANZA.")
                mostrar_mensaje("¡HAS MUERTO!.")
                manejar_partida(True)
                return



#funcion si eliges la segunda opcion(2)
def opcion_2():
    mostrar_mensaje("Has decidido seguir vagando por el pueblo.") #otra opcion
    mostrar_mensaje("Lastimosamente al no entrar en la casa, no te percataste que habia un zombie dentro de ese lugar.") #otra opcion
    mostrar_mensaje("Cuando empiezas a escuchar unos pasos detras tuyos, ya es tarde.") #otra opcion
    mostrar_mensaje("El zombie te ha devorado.") #otra opcion
    mostrar_mensaje("¡HAS MUERTO!.") #otra opcion
    manejar_partida(True)
    return #Volver

#funcion para comenzar
def comenzar(): 
    aviso_juego()
    introduccion()
    mostrar_mensaje("¿Qué haces?.")
    mostrar_mensaje("1. Decides entrar en la casa.")
    posibilidad_supervivencia("Alto nivel de peligro (40% de sobrevivir), pero alta recompensa potencial. Ten en cuenta los riesgos.")
    mostrar_mensaje("2. Decides seguir vagando por el pueblo.")
    posibilidad_supervivencia("Bajo nivel de peligro (60% de sobrevivir), pero sin recompensa potencial. Piensa tu decisión.")
    eleccion1 = pedir_opcion(["1", "2"])
    limpiar_pantalla()

    if eleccion1 == "1":
        opcion_1()
        limpiar_pantalla()
    elif eleccion1 == "2":
        opcion_2()
        limpiar_pantalla()

    mostrar_mensaje("FIN DEL JUEGO")

#Funcion para reiniciar el juego
def manejar_partida(reiniciar):
    mostrar_mensaje("FIN DE LA PARTIDA") #THE END
    if reiniciar:
        mostrar_mensaje("¿Deseas reiniciar el juego?") #reiniciar la partida
        mostrar_mensaje("1. Sí")
        mostrar_mensaje("2. No")
        eleccion = pedir_opcion(["1", "2"])
        if eleccion == "1":
            comenzar()
        else: 
            mostrar_mensaje("Gracias por haber jugado!")
            mostrar_mensaje("¡Hasta luego!")
    else:
        mostrar_mensaje("Gracias por haber jugado!")
        mostrar_mensaje("¡Hasta luego!")

comenzar() #Obligatorio, sino, no funcina tu codigo
