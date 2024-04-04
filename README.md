# Luis-Nij-Tesis-2022
Repositorio para documentos, archivos y códigos para tesis de Luis Nij.


# Alphabot2 -  Robot diferencial comercial

AlphaBot es el nombre con el que se denomina a una serie de productos desarrollados por la empresa china WaveShare Electronics. Esta línea de productos posee, hasta el momento, dos versiones de de robots móviles con interfaz para las placas de desarrollo Arduino Uno y Raspberry Pi. Ambas versiones poseen documentación general relativamente reciente en el sitio web oficial de la empresa, dicha información data del año 2017. 

Como lo indican en su página oficial, el AlphaBot es una plataforma de desarrollo robótica que conjuga elementos de placas electrónicas, armazón móvil y todo lo necesario para la locomoción del mismo. Se pretende que dicha plataforma dote al usuario de la capacidad de implementar proyectos por medio de los diferentes sensores disponibles en el robot. Algunos ejemplos involucran evasión de obstáculos, seguimiento de líneas, monitoreo con videocámara así como conectividad Bluetooth y/o WiFi dependiendo del modelo de AlphaBot utilizado. Esta oferta de plataforma robótica se encuentra en el rango de precio medio-alto comparado a otras ofertas de la misma empresa orientadas al sector de plataformas móviles con interfaz disponible para Raspberry Pi. Consultando el costo de venta (sin considerar costos de envío, nacionales o internacionales), el AlphaBot2 se ofrece desde los $98.99 USD la versión más sencilla sin placa de desarrollo Raspberry Pi hasta los $238.99 USD (la versión más completa).

![image](https://user-images.githubusercontent.com/60576547/202885375-8bfc6cfe-7512-4938-96c8-73ac50673eec.png)

# Conocimiento Previo -  ¿Donde Comenzar? 

Resulta útil contar con un conocimiento previo de programación básico de python, microcontroladores y conocimiento básico de electricidad y electrónica.
La plataforma Alphabot, como se mencionó anteriormente es un robot ensamblado de origen chino que puede utilizar Raspberry Pi o Arduino para funcionar dependiendo del modelo adquirido. En este repositorio se discutirá el funcionamiento y se brindarán descripciones y apoyo para la version que monta compatibilidad para modelos Raspberry Pi 3 en adelante. Así mismo, se brindará apoyo utilizando Python como lenguaje de programación y sus librerias asociadas 

## Robótica de Enjambre

La robótica de enjambre estudia las diferentes estrategias de coordinación de un gran numero de robots simples. Se inspira en el comportamiento observado en insectos sociales, los cuales ejemplifican como un gran numero de individuos pueden interactuar entre sí para crear sistemas complejos e inteligentes. Cabe destacar que en este tipo de sistemas, el comportamiento colectivo surge de forma auto-organizada a partir de las acciones entre individuos y su entorno. Por tanto la inteligencia de enjambre es una característica que emerge como resultado de las interacciones de las masas.

En este tipo de sistemas, el enjambre se caracteriza por ser un conjunto de individuos capaces de agregar nuevos miembros (sistema con capacidad de cambio en numero de elementos), tener movimiento coordinado y capacidad de dispersarse. Organizados como enjambre, los robots son capaces de realizar tareas colectivas mucho más complejas y demandantes las cuales serían incapaces de realizar si trabajaran de manera individual. Además, a nivel de implementación siempre resulta mucho mas conveniente el diseño y construcción de sistemas roboticos de menor complejidad

## Programación Multi hilos

En el ámbito de la programación, se habla de hilos de ejecución, también conocidos como procesos ligeros, a una estrategia de implementación de software que tiene como objetivo evitar el desperdicio de recursos en el sistema. Una de las principales razones por la que los sistemas computacionales se vuelven lentos en la ejecución de tareas es por la continua interacción entre procesador y memoria y la asignación de espacio de memoria cada uno de los procesos agendados. Los hilos son rutinas independientes  de un proceso macro que puede tener uno o muchos hilos ejecutándose. Esto permite desarrollar tareas simultaneamente en un mismo programa en lugar de ser desarrolladas de manera secuencial. La implementación de hilos permite la perspectiva al hilo de ejecución de tener exclusividad en sus recursos asignados. \cite{hilos}

Si bien la implementación de hilos en un proceso permite agilizar el uso de recursos y optimizar el rendimiento, n siempre resulta conveniente utilizarlos. Casos en donde las tareas dependan de un resultado anterior o del resultado de otras tareas resultan incompatibles para el uso de hilos. El uso de hilos de ejecución resulta conveniente cuando hablamos de tareas con objetivos diferentes entre sí. 

## Ordenadores Raspberry Pi

Raspberry Pi es el nombre de una serie de mini ordenadores diseñados por la Fundación Raspberry Pi, una organización de origen inglés dedicada a difusión de educación en temas de computación. Esta serie de computadoras fue lanzada al mercado en 2012 y desde entonces ha desarrollado diferentes iteraciones mejorando las capacidades de hardware\cite{whatisRPi}.

El modelo original de Raspberry tuvo un procesador de un único núcleo con 700MHz de velocidad e incorporaba 256 MB de memoria RAM. Los computadores de este tipo se han caracterizado por tratar de hacer asequible la adquisición de los mismos lo que se refleja en los precios de compra directos con la Fundación Raspberry Pi. Concretamente estos ordenadores han costado en promedio 35 dólares americanos (USD) y poseen modelos tan económicos como 5 dólares \cite{whatisRPi}.

Desde su lanzamiento, la plataforma Raspberry Pi ha tenido una aceptación notable al rededor del mundo ya que muchas personas la utilizan para aprender y desarrollar proyectos de programación y electrónica. Gracias a que estas tarjetas electrónicas incorporan pines físicos es posible realizar tareas en las que el procesador interactúe con elementos y circuitería externa. Esto ha dotado de multitud de posibilidades a la tarjeta electrónica lo cual se ve reflejado en su popularidad en la comunidad de desarrolladores, estudiantes y entusiastas.


### Modelos disponibles

* Pi 1 Modelo B (2012)
* Pi 1 Modelo A (2013)
* Pi 1 Modelo B+ (2014)
* Pi 1 Modelo A+ (2014)
* Pi 2 Modelo B (2015)
* Pi Zero (2015)
* Pi 3 Modelo B (2016)
* Pi Zero W (2017)
* Pi 3 Modelo B+ (2018)
* Pi 3 Modelo A+ (2019)
* Pi 4 Modelo A (2019)
* Pi 4 Modelo B (2020)
* Pi 400 (2021)

### Módulo de Cámaras

En modelos recientes, la Raspberry Pi ofrece la capacidad de conectar una cámara a la tarjeta electrónica. Esto permite la posibilidad de integrarla a proyectos relacionados con visión por computadora e identificación de patrones. Actualmente el modelo oficial de cámara desarrollado por la Fundación Raspberry Pi es el conocido como IMX219 de la marca Sony con 8 Megapíxeles de resolución el cual se conecta por medio de una Interfaz Serial para Cámara (Serial Camera Interface, SCI). A pesar de  esto existen opciones con mejor resolución pudiendo encontrar modelos con hasta 12.3 Mega píxeles de resolución 

### GPIO: Pines de Propósito General

Como se mencionó al principio de esta sección, estas placas electrónicas cuentan con interfaz tipo pin con la que el procesador de las Raspberry Pi puede interactuar con circuitería externa. A este conjunto de 40 pines de entrada y salida se le conoce como Pines de Propósito General (GPIO, General Purpose Input and Output por sus siglas en inglés). Estos pines pertenecen al denominado Hardware Agregado a la Superficie (Hardware Attached on Top, HAT) y se encuentran ordenados en un arreglo de 2 filas de 20 pines cada una. Para hacer uso de estos pines es necesario instalar algunos paquetes de software adicionales como el caso de la librería WiringPi en el caso de administrarlos con lenguaje Python. 

A pesar de la posibilidad de interactuar con elementos externos, los GPIO tienen la limitante de trabajar únicamente con circuitos digitales impidiendo realizar lecturas de tipo analógico directamente con dichos pines. A pesar de esto, algunos de los pines tienen la capacidad de programarse como pines de comunicación para protocolos como SPI (Slave Peripherial Interface) o I2C (Inter-Integrated Circuit) lo cual nos permitirá mitigar esta necesidad apoyándonos del uso de circuitos integrados dedicados al fin antes mencionado. Cabe resaltar que dado su diseño, los pines GPIO poseen limitantes eléctricas de voltaje y corriente lo cual requiere especial cuidado a la hora de conectar la tarjeta electrónica con circuitos externos. En general, se recomienda que los pines de la Raspberry Pi se utilicen como medio de comunicación con microcontroladores o circuitos de control que permitan amplificar y manejar características eléctricas más demandantes como transistores, relevadores, acopladores ópticos etc.

### Sensores de Proximidad - Distancia

Parte fundamental de las características operativas de un agente robótico es disponer de medios para conocer su entorno. Las características de interés pueden incluir temperatura ambiental, incidencia de luz, presencia de señales o fuentes de campos magnéticos y, en particular, distancias relativas a otros objetos. Tener la capacidad de medir esta última característica resulta de importante interés, especialmente en aplicaciones con entornos restringidos o en entornos con obstáculos u otros agentes robóticos. Para suplir esta necesidad, actualmente se disponen de diferentes tipos de sensores con variados principios físicos que permiten detectar proximidad a objetos y en algunos casos medir distancias en un rango determinado. Dependiendo de las características del medio en que se realiza la medición, así como las características de los objetos que se desea detectar se pueden mencionar los siguientes tipos de sensores:

* Sensores Ultrasónico: Este tipo de sensores basa su funcionamiento en la emisión de ondas sonoras de ultra alta frecuencia. En particular, el sensor comercial SR-04 denominado “sensor ultrasónico” utiliza señales de 40kHz para detectar objetos. Estos sensores poseen una fuente emisora y un dispositivo receptor. Por tanto, para estimar la distancia a objetos se debe realizar un calculo intermedio que relacione la velocidad de propagación de la señal emitida con el tiempo en que esta señal es emitida y recibida por el dispositivo \cite{IR_US_Sensors}. Los dispositivos basados en este principio pueden verse afectados por fuentes de sonido ultrasónicas e incluso por sensores del mismo tipo apuntando entre sí. Sin embargo, poseen ciertas ventajas puesto que no se ven afectados por características particulares del objeto como el color de su superficie o la incidencia de luz sobre ellos.

* Sensores infrarrojo: Este tipo de sensores basa su funcionamiento en la emisión de pulsos de luz por debajo del rango visible para el ser humano. Similar al principio de medición de los sensores ultrasónicos, el sensor infrarrojo detecta la presencia de objetos en un rango de distancia determinado por medio de la refracción de la señal emitida en la superficie del obstáculo. Esto presenta algunas ventajas en cuanto a implementación ya que suelen ser económicos, no requieren de mucho espacio y consumen menos potencia.

# PRIMERA PARTE - PLATAFORMA ALPHABOT / EXPERIMENTACIÓN

A lo largo de las etapas del proyecto \textit{Robotat} se han implementado diferentes pruebas relacionadas a temas de robótica de enjambre tales como algoritmos, comunicación y aprendizaje profundo. Debido a la contingencia mundial por el coronavirus, en los años 2020 y 2021 los esfuerzos fueron focalizados a realizar experimentos en ambientes simulados en computadora tales como \textiWebots, un programa de código abierto con didáctica enfocada a la robótica, y \textit{Matlab}, un sistema de cómputo numérico capaz de procesar grandes cantidades de datos. Fue hasta 2022 cuando se presentó una tesis cuyo tema giró en torno a la creación de un modelo de agente robótico fabricado en UVG con la capacidad de probar dichos algoritmos y procesos en un entorno físico. El presente trabajo tomó como base un modelo de robot móvil comercial disponible en el mercado y procedió a realizar una extracción de parámetros desde la perspectiva de ingeniería lo cual constituye el capítulo a continuación.

## Acerca del agente robótico

\textit{AlphaBot} es el nombre con el que se denomina a una serie de productos desarrollados por la empresa china \textit{WaveShare Electronics}. Esta línea de productos posee, hasta el momento, dos versiones de de robots móviles con interfaz para las placas de desarrollo \textit{Arduino Uno} y \textit{Raspberry Pi}. Ambas versiones poseen documentación general relativamente reciente en el sitio web oficial de la empresa, dicha información data del año 2017. 

Como lo indican en su página oficial, el \textit{AlphaBot} es una plataforma de desarrollo robótica que conjuga elementos de placas electrónicas, armazón móvil y todo lo necesario para la locomoción del mismo \cite{Alphabot_MainPage}. Se pretende que dicha plataforma dote al usuario de la capacidad de implementar proyectos por medio de los diferentes sensores disponibles en el robot. Algunos ejemplos involucran evasión de obstáculos, seguimiento de líneas, monitoreo con videocámara así como conectividad \textit{Bluetooth} y/o \textit{WiFi} dependiendo del modelo de \textit{AlphaBot} utilizado. Esta oferta de plataforma robótica se encuentra en el rango de precio medio-alto comparado a otras ofertas de la misma empresa orientadas al sector de plataformas móviles con interfaz disponible para \textit{Raspberry Pi}. Consultando el costo de venta (sin considerar costos de envío, nacionales o internacionales), el \textit{AlphaBot2} se ofrece desde los $98.99$\$ USD (la versión más sencilla sin placa de desarrollo \textit{Raspberry Pi} hasta los $238.99$\$ USD (la versión más completa) \cite{Alphabot2_MainPage}. 

El \textit{AlphaBot} posee un diseño modular, ensamblable sin necesidad de soldadura de componentes ni herramientas complejas. Como se observa en la Figura \ref{fig:Alphabot_Partes}, el diseño consta de una placa superior específica dependiendo del modelo de placa de desarrollo a utilizar, una placa base común para todos los modelos la cual posee los actuadores y sensores así como un brazo articulado en la parte superior que posee integración con video cámara.
El \textit{Alphabot2} pretende abarcar un mercado amplio relacionado a la docencia de temas de programación y electrónica así como su utilización por entusiastas y grupos con reciente introducción en la materia. El único detalle a considerar proveniente de fábrica es la no inclusión de baterías. El presente trabajo enfocó el análisis en la plataforma robótica \textit{AlphaBot} en su segunda versión con interfaz de conexión para placa de desarrollo \textit{Raspberry Pi} denominado \textit{AlphaBot2-Pi}. 

## Primera Implementación en UVG
 
Se dispone de ejemplares del \textit{AlphaBot2-Pi} (de aquí en adelante, \textit{AB2}) gracias a la cooperación entre la Universidad de Navarra, España y el Departamento de Ingeniería Electrónica, Mecatrónica y Biomédica de la Universidad del Valle de Guatemala. Dichos activos fueron otorgados en 2022 a la unidad de UVG antes mencionada (Figura \ref{fig:mesh100} izquierda) y al autor del presente trabajo como estudiante colaborador de UVG (Figura \ref{fig:mesh100} derecha). Durante el proyecto de cooperación se confirió al autor del presente trabajo la tarea de preparar los \textit{AB2} para su utilización en pruebas de ejecución y validación de algoritmos de física granular estudiados por el Licenciado Robles. Producto de ello se emitió un reportaje publicado en la sección de noticias del sitio web oficial de la Universidad del Valle \cite{NijyJuanDi} brindando más detalles al respecto.

En esa oportunidad se construyó el sistema robótico guiándose con las instrucciones proporcionadas por el fabricante. Como resultado se obtuvo el sistema descrito en la Figura \ref{fig:Alphabot_Original} destacando visualmente la inclusión de una video cámara con brazo móvil articulado.  Debido a la necesidad de realizar constantes pruebas, se realizaron modificaciones a las características originales del robot. Se hizo necesario aumentar la capacidad y modificar la compatibilidad de las baterías del agente con las opciones de baterías disponibles en Guatemala. Las baterías escogidas aumentaron el tiempo de autonomía así como el peso y espacio requerido para transportarlas. Para ello se diseñó un acople provisional basándose en los puntos de unión originales del robot de tal modo que tanto el costo de modificación como el impacto al robot mismo fueran mínimos. Como se observa en la Figura \ref{fig:Alphabot_Nij} se optó por implementar un diseño modular apilado. Esto requirió desmontar la estructura de la video cámara antes mencionada en favor de ubicar las baterías (fuente considerable de peso) lo mas cercana al suelo considerando el diseño original permitiendo mantener el centro de masa del robot lo mas bajo posible. 

En dicha oportunidad el objetivo principal consistió en verificar la funcionalidad original de la plataforma así como su capacidad de ejecutar tareas relacionadas al seguimiento de líneas pintadas en el suelo. Como se observa en la Figura \ref{fig:Alphabot_LineFollow}, se construyó un sistema simple de circuito de prueba (pista) para probar y afinar dicha característica que requería del uso de sensores infrarrojos ubicados en la placa electrónica inferior del robot. En el repositorio se encuentra disponible un video tomado desde una perspectiva superior de la pista de pruebas. En dicho video se observa el movimiento de los agentes (3 agentes) a través del circuito levando consigo un código identificador \textit{ArUco}. Dichos identificadores permitieron utilizar herramientas de software para marcar el movimiento relativo de objetos y extraer datos relacionados a velocidades, orientaciones relativas entre otros. 


