# Luis-Nij-Tesis-2022

Repositorio para documentos, archivos y scripts de trabajo de graduación.

El siguiente trabajo pretende aportar en materia de plataformas móviles de robótica con posibles aplicaciones en inteligencia de enjambre. El objetivo principal fue realizar, con un punto de vista basado en ingeniería, un aporte enfocado en las capacidades, limitaciones y modificaciones a ciertos ejemplos de plataformas móviles preexistentes. Para ello se hizo necesario evaluar el estado original, proponer y efectuar cambios que permitieran la integración de los agentes robóticos involucrados en este trabajo, en ambientes de prueba ya utilizados por la Universidad. Se escogieron herramientas de programación y ensamblaje físico coherentes con las especificaciones de los robots así como  pruebas que permitieran corroborar las funcionalidades que ofrecen por defecto y las funcionalidades finales agregadas producto del presente proyecto.

La utilización de robots basados en placa de desarrollo **Raspberry Pi** permitió agregar una mayor capacidad de procesamiento y permitió ampliar los horizontes en lo que a posibilidades de proyectos se refiere. La elección de esta placa de desarrollo fue determinante en la escalabilidad de grupos de robots variados. Se busca que con los resultados obtenidos y la documentación elaborada se amplíe el conocimiento y los recursos disponibles para la Universidad y el Departamento de Ingeniería Electrónica, Mecatrónica  y Biomédica para la cátedra de cursos relacionados a programación, electrónica y robótica. 

Producto de las pruebas planteadas, las modificaciones y los experimentos implementados se obtuvo como resultado la integración de sistemas preexistentes de la Universidad a un entorno en el que los robots de prueba del presente trabajo pudieran interactuar. Así mismo se aportó con documentación respecto a la plataforma y los cambios ejecutados. Todo esto se realizó con la intención facilitar los futuros trabajos que incluyan esta plataforma como parte de los sujetos de investigación

# Antecedentes - Contexto previo de trabajos realizados en Universidad del Valle de Guatemala y el Mundo

Una de las aplicaciones de la ingeniería mecatrónica es la robótica y un tópico de particular interés en esta rama de la ciencia es la robótica de enjambres. Se habla de robótica de enjambres a la coordinación de múltiples robots simples (conocidos como agentes) que en un número considerable constituyen un sistema mucho mas complejo y capaz de realizar tareas mas elaboradas. 

## Robotarium - Georgia Tech

Se conoce como Robotarium a la plataforma desarrollada por estudiantes del Instituto de Tecnología de Georgia, la cual permite realizar simulaciones y verificaciones de algoritmos y pruebas con agentes físicos robóticos. A nivel de software esta plataforma está basada en el uso de Matlab-Python y provee acceso remoto a estudiantes y profesionales de todo el mundo por medio de un análisis previo del trabajo a realizar por parte del personal encargado de dicho laboratorio en el Instituto de Tecnología de Georgia. Físicamente se compone de una plataforma plana, de color blanco sobre la cual se pueden encontrar dispositivos de medición como sensores, cámaras y demás dispositivos de telemetría que extraerán datos de las pruebas. 

<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/64705e9b-7296-4fd5-b387-7e64ec819111" width="680">

Figura 1. Sistema Robotarium instalado en instituto Georgia Tech.

## Proyecto Robotat Fase 1 - Universidad del Valle de Guatemala

En la primera fase del proyecto Robotat de la Universidad del Valle de Guatemala, se trabajó en el diseño de la plataforma física de robots con el objetivo de ser usado en pruebas de modelos de robótica de enjambre. Esta fase fue desarrollada por André Rodas. Se utilizaron cámaras para la captura de imagenes y módulos de comunicación Wireless Field (WiFi) para establecer comunicación entre la computadora central y los diferentes robots agentes,a los que se denominó como **Bitbots**. El proceso de conexión y montaje de la red inalámbrica fue desarrollado por Marlon Castillo. 

## Proyecto Robotat Fase 2 - Universidad del Valle de Guatemala

Para la segunda fase del proyecto se optó por utilizar una versión modificada del algoritmo **Particle Swarm Optimization** como modelo de planificación de trayectorias. Esto fue desarrollado por Aldo Aguilar y busca que por medio del concepto de funciones de costo se encuentren los valores optimos para dirigir a los agentes del enjambre. Se encontró que una de las principales limitaciones en la implementación del algoritmo en agentes con dimensiones físicas es la posible saturación de actuadores y movimiento irregular. Para resolver esto se propuso que la posición calculada por el algoritmo debe ser únicamente una sugerencia y que partiendo de esa referencia, el agente procede a calcular la rotación que debería ejecutar para dirigirse a dicho punto y considerar como caso óptimo, aquellos movimientos con la menor energía involucrada. Durante esta fase se implementaron simulaciones de particulas sin masa ni dimensiones en Matlab y se utilizó **Webots** para simular el comportamiento de los agentes en un entorno con restricciones físicas. 

Así mismo, Eduardo Santizo empleó la metodología de aprendizaje reforzado y aprendizaje profundo para elaborar un **PSO Tuner** y un generador de trayectorias. Esto involucró la utilización de una red neuronal recurrente cuyo entrenamiento necesitó mas de 7000 simulaciones del algoritmo estándar \textit{PSO} y así poder reducir el tiempo de convergencia del algoritmo original **PSO**. Para el planificador de trayectorias se utilizó aprendizaje profundo con **Webots**. Se pretendía valorar las trayectorias generadas en base al esquema de penalización-recompensa en donde la trayectoria calculada recibía una recompensa si permitía que los robots esquivaran obstáculos y recibía una penalización si chocaba contra ellos. Por otra parte, Gabriela Iriarte presentó avances en la implementación del algoritmo de inteligencia de enjambre conocido como **Ant Colony Optimization** como alternativa al planificador de trayectorias y al **MPSO**. Las simulaciónes de su trabajo se desarrollaron en **Matlab** y **Webots**.

## Proyecto Robotat Fase 3 - Universidad del Valle de Guatemala

En esta fase se busca enfocar los esfuerzos en el diseño de una plataforma móvil que permita aplicar los algoritmos de robótica de enjambre desarrollados en fases anteriores. Se toma como base los conceptos y diseños de robots agentes como el **E-puck**, **Pi-Puck** y los **Kylobots** con el objetivo de hacer rentable y escalable la producción de los mismos. Esta etapa del proyecto continúa en proceso, sin embargo se obtienen avances en cuanto a los costos y a los módulos de comunicación y análisis de imagen con cámara lo que permite abrir la posibilidad de futuras implementaciones. 

## Ecosistema Robotat - Universidad del Valle de Guatemala

En las instalaciones de la Universidad se cuenta con un laboratorio que dispone de un sistema de experimentación en robótica denominado **Robotat**. Está constituido por una mesa de pruebas con bordillo, rodeada de un sistema de cámaras de captura de movimiento de alta precisión y baja latencia administrados por una computadora central. Dicho sistema utiliza dispositivos denominados "marcadores" que son piezas plásticas con características especiales para ser detectadas por el sistema de cámaras. Este conjunto se integra a una red inalámbrica por medio de un enrutador dedicado sin conexión a internet. Dentro del equipo de computo que administra el sistema de cámaras se dispone de un código fuente para ejecutar un servidor que responda a solicitudes de la ubicación y características de los marcadores de prueba. En la **Figura 2** se observa el sistema completo, en las **Figuras 3 y 4** observamos un acercamiento al sistema de cámaras.


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/2173e6ae-3700-4c5c-b8a0-24ace943d391" width="680">

Figura 2: Sistema Robotat en Universidad del Valle de Guatemala


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/5ac79c25-5d1a-4aa8-aea6-edfbd3686036" width="680">

Figura 3: Sistema Robotat - Camaras de captura de movimiento vista 1


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/d54d2905-971a-431e-86e0-da89eb3fd72b" width="680">

Figura 4: Sistema Robotat - Camaras de captura de movimiento vista 2


## Alphabot02 - Robot modular comercial


En el mercado existen diferentes propuestas de plataformas móbiles con aplicaciones en robótica. Una de estas opciones, desarrollada por la empresa China **Waveshare Electronics**, se denomina **Alphabot** y actualmente cuenta con dos iteraciones en el diseño de esta línea de robots.  El kit comercial posee una placa de circuito impreso como base del chasis y sobre ella, una segunda placa con posibilidad de conectar una Raspberry Pi o una placa Arduino como unidad de procesamiento.  En la Figura 5 observamos el agente robótico con la placa de desarrollo expuesta, en la Figura 6 observamos el agente robótico ensamblado.


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/95495c5d-9413-4f79-ad1b-3aee30aadd99" width="480">

Figura 5: Plataforma Móbil **Alphabot 2** desarmada, vista frontal.


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/b3950bf8-393a-40d2-8d4c-b29a603f46a8" width="480">

Figura 6: Plataforma Móbil **Alphabot 2** desarmada, vista superior. 

# ¿Cuál es el aporte que pretendemos?

Para continuar con el desarrollo de las aplicaciones de robótica de enjambre se hace necesario utilizar una plataforma móvil que permita la locomoción de los agentes en un entorno de pruebas no virtuales. Es importante recordar que una parte crucial en el desarrollo de estos algoritmos de robótica es la validación con sistemas físicos y en ambientes reales. El nuevo laboratorio de robótica de la UVG, que cuenta con una plataforma de pruebas y sistema de captura de movimiento permitirá continuar con la línea de investigación. Gracias a los distintos avances en el proyecto Robotat se han desarrollado variaciones en algoritmos de róbotica de enjambre como PSO y Ant Colony y se les ha aplicado mejoras basadas en aprendizaje profundo que logren mayor eficiencia en sus procesos de cálculo. Así mismo, se han desarrollado herramientas y complementos de software cuyo objetivo fue mitigar la falta de agentes físicos en la implementación de los algoritmos antes mencionados. Se pretende entonces, continuar con la línea de investigación en robótica y desarrollo de software, parcialmente pausados entre otros motivos por la pandemia de COVID-19. Se busca evaluar las capacidades de distintas opciones de plataformas móviles que permitan implementar algoritmos y llevar a cabo experimentos de robótica de enjambre en pruebas físicas.

Al momento de la realización de este trabajo, la situación general respecto a la pandemia por COVID-19 comenzaba a presentar transición hacia una  **nueva normalidad**. Ello incluyó la habilitación de espacios de trabajo grupal con las limitantes de aforo y tiempo de trabajo que gradualmente presentaron menores restricciones. Gracias a esta transición fue posible desarrollar pruebas que involucraron la integración sistemas físicos prácticos, entre ellos una red inalámbrica dedicada a proyectos de robótica en los laboratorios de las nuevas instalaciones de la universidad así como el sistema de cámaras para captura de movimientos **Optitrack**. Así mismo, gracias a la cooperación con la Universidad de Navarra, fue posible agenciarse de agentes robóticos por lo que este proyecto incluye implementación en código y pruebas con agentes físicos. Esto permitió realizar experimentos en cuanto a las características de componentes de los agentes y su integración con el sistema Robotat. Se focalizaron esfuerzos en comprender el funcionamiento, bondades y limitaciones de la plataforma móvil disponible dejando para futuros trabajos la implementación de algoritmos, códigos fuente y proyectos con rutinas puntuales. La documentación y recursos audiovisuales representan también parte fundamental del aporte de este trabajo.

# CONOCIMIENTO PREVIO 

## Alphabot2 -  Análisis mas profundo.

**AlphaBot** es el nombre con el que se denomina a una serie de productos desarrollados por la empresa china **WaveShare** **Electronics**. Esta línea de productos posee, hasta el momento, dos versiones de de robots móviles con interfaz para las placas de desarrollo **Arduino Uno** y **Raspberry Pi**. Ambas versiones poseen documentación general relativamente reciente en el sitio web oficial de la empresa, dicha información data del año 2017. 

Como lo indican en su página oficial, el **AlphaBot** es una plataforma de desarrollo robótica que conjuga elementos de placas electrónicas, armazón móvil y todo lo necesario para la locomoción del mismo. Se pretende que dicha plataforma dote al usuario de la capacidad de implementar proyectos por medio de los diferentes sensores disponibles en el robot. Algunos ejemplos involucran evasión de obstáculos, seguimiento de líneas, monitoreo con videocámara así como conectividad **Bluetooth** y/o **WiFi** dependiendo del modelo de **AlphaBot** utilizado. Esta oferta de plataforma robótica se encuentra en el rango de precio medio-alto comparado a otras ofertas de la misma empresa orientadas al sector de plataformas móviles con interfaz disponible para **Raspberry Pi**. Consultando el costo de venta (sin considerar costos de envío, nacionales o internacionales), el **AlphaBot2** se ofrece desde los $98.99$ $USD (la versión más sencilla sin placa de desarrollo **Raspberry Pi** hasta los $238.99 $USD (la versión más completa). 

El **AlphaBot** posee un diseño modular, ensamblable sin necesidad de soldadura de componentes ni herramientas complejas. Como se observa en la Figura 7, el diseño consta de una placa superior específica dependiendo del modelo de placa de desarrollo a utilizar, una placa base común para todos los modelos la cual posee los actuadores y sensores así como un brazo articulado en la parte superior que posee integración con video cámara.
El **Alphabot2** pretende abarcar un mercado amplio relacionado a la docencia de temas de programación y electrónica así como su utilización por entusiastas y grupos con reciente introducción en la materia. El único detalle a considerar proveniente de fábrica es la no inclusión de baterías. El presente trabajo enfocó el análisis en la plataforma robótica **AlphaBot** en su segunda versión con interfaz de conexión para placa de desarrollo **Raspberry Pi** denominado **AlphaBot2-Pi**. 

<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/b16198cf-3ffd-447e-9c1a-60ab8602b5f9" width="480">

Figura 7. Composision estructural del agente robótico Alphabot02

## ¿Donde Comenzar? 

Resulta útil contar con un conocimiento previo de programación básico de python, microcontroladores y conocimiento básico de electricidad y electrónica.
La plataforma Alphabot, como se mencionó anteriormente es un robot ensamblado de origen chino que puede utilizar Raspberry Pi o Arduino para funcionar dependiendo del modelo adquirido. En este repositorio se discutirá el funcionamiento y se brindarán descripciones y apoyo para la version que monta compatibilidad para modelos Raspberry Pi 3 en adelante. Así mismo, se brindará apoyo utilizando Python como lenguaje de programación y sus librerias asociadas 

## Robótica de Enjambre

La robótica de enjambre estudia las diferentes estrategias de coordinación de un gran numero de robots simples. Se inspira en el comportamiento observado en insectos sociales, los cuales ejemplifican como un gran numero de individuos pueden interactuar entre sí para crear sistemas complejos e inteligentes. Cabe destacar que en este tipo de sistemas, el comportamiento colectivo surge de forma auto-organizada a partir de las acciones entre individuos y su entorno. Por tanto la inteligencia de enjambre es una característica que emerge como resultado de las interacciones de las masas.

En este tipo de sistemas, el enjambre se caracteriza por ser un conjunto de individuos capaces de agregar nuevos miembros (sistema con capacidad de cambio en numero de elementos), tener movimiento coordinado y capacidad de dispersarse. Organizados como enjambre, los robots son capaces de realizar tareas colectivas mucho más complejas y demandantes las cuales serían incapaces de realizar si trabajaran de manera individual. Además, a nivel de implementación siempre resulta mucho mas conveniente el diseño y construcción de sistemas roboticos de menor complejidad

## Programación Multi hilos

En el ámbito de la programación, se habla de hilos de ejecución, también conocidos como procesos ligeros, a una estrategia de implementación de software que tiene como objetivo evitar el desperdicio de recursos en el sistema. Una de las principales razones por la que los sistemas computacionales se vuelven lentos en la ejecución de tareas es por la continua interacción entre procesador y memoria y la asignación de espacio de memoria cada uno de los procesos agendados. Los hilos son rutinas independientes  de un proceso macro que puede tener uno o muchos hilos ejecutándose. Esto permite desarrollar tareas simultaneamente en un mismo programa en lugar de ser desarrolladas de manera secuencial. La implementación de hilos permite la perspectiva al hilo de ejecución de tener exclusividad en sus recursos asignados. 

Si bien la implementación de hilos en un proceso permite agilizar el uso de recursos y optimizar el rendimiento, n siempre resulta conveniente utilizarlos. Casos en donde las tareas dependan de un resultado anterior o del resultado de otras tareas resultan incompatibles para el uso de hilos. El uso de hilos de ejecución resulta conveniente cuando hablamos de tareas con objetivos diferentes entre sí. 

## Ordenadores Raspberry Pi

Raspberry Pi es el nombre de una serie de mini ordenadores diseñados por la Fundación Raspberry Pi, una organización de origen inglés dedicada a difusión de educación en temas de computación. Esta serie de computadoras fue lanzada al mercado en 2012 y desde entonces ha desarrollado diferentes iteraciones mejorando las capacidades de hardware.

El modelo original de Raspberry tuvo un procesador de un único núcleo con 700MHz de velocidad e incorporaba 256 MB de memoria RAM. Los computadores de este tipo se han caracterizado por tratar de hacer asequible la adquisición de los mismos lo que se refleja en los precios de compra directos con la Fundación Raspberry Pi. Concretamente estos ordenadores han costado en promedio 35 dólares americanos (USD) y poseen modelos tan económicos como 5 dólares.

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

* Sensores Ultrasónico: Este tipo de sensores basa su funcionamiento en la emisión de ondas sonoras de ultra alta frecuencia. En particular, el sensor comercial SR-04 denominado “sensor ultrasónico” utiliza señales de 40kHz para detectar objetos. Estos sensores poseen una fuente emisora y un dispositivo receptor. Por tanto, para estimar la distancia a objetos se debe realizar un calculo intermedio que relacione la velocidad de propagación de la señal emitida con el tiempo en que esta señal es emitida y recibida por el dispositivo. Los dispositivos basados en este principio pueden verse afectados por fuentes de sonido ultrasónicas e incluso por sensores del mismo tipo apuntando entre sí. Sin embargo, poseen ciertas ventajas puesto que no se ven afectados por características particulares del objeto como el color de su superficie o la incidencia de luz sobre ellos.

* Sensores infrarrojo: Este tipo de sensores basa su funcionamiento en la emisión de pulsos de luz por debajo del rango visible para el ser humano. Similar al principio de medición de los sensores ultrasónicos, el sensor infrarrojo detecta la presencia de objetos en un rango de distancia determinado por medio de la refracción de la señal emitida en la superficie del obstáculo. Esto presenta algunas ventajas en cuanto a implementación ya que suelen ser económicos, no requieren de mucho espacio y consumen menos potencia.

# PRIMERA PARTE - PLATAFORMA ALPHABOT / EXPERIMENTACIÓN

A lo largo de las etapas del proyecto **Robotat** se han implementado diferentes pruebas relacionadas a temas de robótica de enjambre tales como algoritmos, comunicación y aprendizaje profundo. Debido a la contingencia mundial por el coronavirus, en los años 2020 y 2021 los esfuerzos fueron focalizados a realizar experimentos en ambientes simulados en computadora tales como **Webots**, un programa de código abierto con didáctica enfocada a la robótica, y **Matlab**, un sistema de cómputo numérico capaz de procesar grandes cantidades de datos. Fue hasta 2022 cuando se presentó una tesis cuyo tema giró en torno a la creación de un modelo de agente robótico fabricado en UVG con la capacidad de probar dichos algoritmos y procesos en un entorno físico. El presente trabajo tomó como base un modelo de robot móvil comercial disponible en el mercado y procedió a realizar una extracción de parámetros desde la perspectiva de ingeniería lo cual constituye el capítulo a continuación.

## Primera Implementación en UVG
 
Se dispone de ejemplares del **AlphaBot2-Pi** (de aquí en adelante, **AB2**) gracias a la cooperación entre la Universidad de Navarra, España y el Departamento de Ingeniería Electrónica, Mecatrónica y Biomédica de la Universidad del Valle de Guatemala. Dichos activos fueron otorgados en 2022 a la unidad de UVG antes mencionada **(Figura 8 izquierda)** y al autor del presente trabajo como estudiante colaborador de UVG **(Figura 8 derecha)**. Durante el proyecto de cooperación se confirió al autor del presente trabajo la tarea de preparar los **AB2** para su utilización en pruebas de ejecución y validación de algoritmos de física granular estudiados por el Licenciado Robles. Producto de ello se emitió un reportaje publicado en la sección de noticias del sitio web oficial de la Universidad del Valle brindando más detalles al respecto.


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/bc420aec-b07b-4d52-bbf1-4fc698ef9cc2" width="720">

Figura 8. Trabajo en conjunto, Juan Diego Robles (Izquierda) Universidad de Navarra, España; Luis Javier Nij (Derecha) Universidad del Valle de Guatemala

En esa oportunidad se construyó el sistema robótico guiándose con las instrucciones proporcionadas por el fabricante. Como resultado se obtuvo el sistema descrito en la **Figura 9** destacando visualmente la inclusión de una video cámara con brazo móvil articulado.  Debido a la necesidad de realizar constantes pruebas, se realizaron modificaciones a las características originales del robot. Se hizo necesario aumentar la capacidad y modificar la compatibilidad de las baterías del agente con las opciones de baterías disponibles en Guatemala. Las baterías escogidas aumentaron el tiempo de autonomía así como el peso y espacio requerido para transportarlas. Para ello se diseñó un acople provisional basándose en los puntos de unión originales del robot de tal modo que tanto el costo de modificación como el impacto al robot mismo fueran mínimos. Como se observa en la **Figura 10** se optó por implementar un diseño modular apilado. Esto requirió desmontar la estructura de la video cámara antes mencionada en favor de ubicar las baterías (fuente considerable de peso) lo mas cercana al suelo considerando el diseño original permitiendo mantener el centro de masa del robot lo mas bajo posible. 

En dicha oportunidad el objetivo principal consistió en verificar la funcionalidad original de la plataforma así como su capacidad de ejecutar tareas relacionadas al seguimiento de líneas pintadas en el suelo. Como se observa en la **Figura 11**, se construyó un sistema simple de circuito de prueba (pista) para probar y afinar dicha característica que requería del uso de sensores infrarrojos ubicados en la placa electrónica inferior del robot. En el repositorio se encuentra disponible un video tomado desde una perspectiva superior de la pista de pruebas. En dicho video se observa el movimiento de los agentes (3 agentes) a través del circuito levando consigo un código identificador ArUco**. Dichos identificadores permitieron utilizar herramientas de software para marcar el movimiento relativo de objetos y extraer datos relacionados a velocidades, orientaciones relativas entre otros. 

<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/8ed7a569-994d-48c9-8f0a-cada9f8281b1" width="720">

Figura 9. Ejemplar de **Alphabot2-Pi** ensamblado en su forma original


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/93c8dcf6-4d20-4a42-b58a-49f5c21e7ae1" width="720">

Figura 10. Ejemplar de **Alphabot2-Pi** facilitado gracias al apoyo de Lic. Juan diego Robles con modificaciones provisionales implementadas


<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/6cc89aca-12bb-456a-9008-deabe1dbd2be" width="720">

Figura 11. Trabajo en conjunto, Juan Diego Robles (Izquierda) Universidad de Navarra, España; Luis Javier Nij (Derecha) Universidad del Valle de Guatemala utilizando recursos del entorno.

<img src="https://github.com/NIJ18482/Luis-Nij-Tesis-2022/assets/60576547/f3c0beb8-31c2-4776-895e-05b5ebe483bd" width="720">

Figura 12. Captura de Video durante Pruebas. Implementación de marcadores para reconocimiento de movimiento **ArUco**

# SEGUNDA PARTE - PLATAFORMA ALPHABOT 2 / ADAPTACIONES



Durante el presente trabajo el **AB2** sufrió diversas modificaciones tomando como referencia el diseño original de fábrica. Para que implementar su uso en el entorno Robotat se requirieron cambios tanto en el sistema físico como en los programas y software para administrarlo. Así mismo se plantearon ciertas normas en su diseño y planificación de estructura de red con el objetivo de ser un agente robótico con aplicaciones escalables a futuro. El presente capítulo es una recopilación de como se propusieron y ejecutaron dichos cambios. 

## Modificaciones de Hardware - Sensores de Proximidad

Uno de los primeros hallazgos surgidos durante la etapa de experimentación con el **AB2** se relaciona con el tema de los sensores de proximidad integrados en la placa inferior. Los sensores de proximidad presentes en el **AB2** utilizan señales infrarrojas que rebotan sobre los objetos y gracias a ello detectan la presencia de obstáculos frente al agente robótico. Estos sensores se encuentran apuntando hacia el frente del **AB2** tal como se puede observar en la figura A CONTINUACION. Durante la experimentación con el agente robótico se encontró que los sensores son del tipo binario, es decir presentan un umbral de detección que indica si hay o no hay obstáculo frente a él. Estos sensores no son capaces de medir distancias concretas si no mas bien se activan o desactivan ante la presencia de objetos a cierta distancia. Esta distancia es relativa a la posición de dichos sensores y apunta ortogonalmente frente a ellos. Se puede manipular el umbral de detección desde unos pocos centímetros hasta ciertos $14$ cm sin perder precisión considerable. Para realizar pruebas respecto al umbrales de detección se hizo necesario ajustar la resistencia de sensibilidad de los sensores que, como podemos ver en la Figura siguiente se encuentra en la placa inferior, sobre la cara que da al suelo. Se hace necesario utilizar destornillador fino y bastante paciencia ya que son potenciómetros tipo trimpot, cabe resaltar que cada sensor tiene si propio potenciómetro. 

--- INSERTAR FIGURA ---

Debido a que el sistema de captura de movimiento **OptiTrack** utiliza cámaras que emiten señales infrarrojas se observó que el agente robótico presenta falsas lecturas de obstáculos cuando se intenta medir su posición con dicho sistema. Así mismo debido a la ubicación de la mesa de pruebas del Robotat relativa a la ventana que da al exterior del laboratorio, se observó que la incidencia de luz solar presenta complicaciones para los sensores del robot. Esto se observó 
principalmente por horas cercanas al medio día y por la tarde, ya que el ángulo de incidencia es más directo sobre el ambiente de trabajo. Como se observa en la figura \ref{fig:Robotat_Optitrack}, la ventana del laboratorio es considerablemente amplia y por tanto permite un alto grado de iluminación natural.  

Tomando en consideración lo anterior se evaluó la posibilidad de cambiar el mecanismo de detección de obstáculos por un sistema que no dependa ni se vea interferido por las señales infrarrojas del sistema **OptiTrack**. De este modo surgió la propuesta de utilizar un sensor ultrasónico y aprovechar los pines que trae la placa inferior del **AB2** especiales para dicho sensor. Cabe mencionar que esta elección está guiada en el hecho de que el sensor ultrasónico basa su funcionamiento en el mecanismo de emisión y recepción de ondas sonoras que rebotan en los obstáculos. Esto permite medir con mayor precisión la presencia de objetos y su distancia al agente robótico en comparación a los sensores infrarrojos que trae por defecto.

Se  procedió a abandonar el uso de los sensores infrarrojos frontales y utilizar los pines libres para un segundo sensor de proximidad ultrasónico. Las pruebas realizadas arrojaron resultados positivos en cuanto a la compatibilidad de dichos pines con un sensor ultrasónico. Debido a que uno de los objetivos de este trabajo es permitir la integración de diferentes agentes robóticos, se optó por diseñar una carcasa de protección que considerase un único sensor de proximidad ultrasónico por robot considerando la cantidad de sensores disponibles. 

## Modificaciones de Hardware - Video Cámara Pi-Cam

Producto del diseño de la carcasa de protección para el agente robótico se trabajó bajo la premisa de eliminar el brazo articulado que permite el movimiento de la cámara de video del **AB2**. Se llegó a la conclusión de eliminar el mecanismo de brazo articulado, y por tanto el uso de servomotores, dado que el agente robótico es capaz de girar sobre su propio eje vertical y dado que la tarea de reconocimiento de obstáculos se desarrolla con mayor eficiencia si la cámara apunta directamente al frente del robot. Esta consideración se incluye en el diseño de la carcasa haciendo que la cámara se encuentre encima del sensor de proximidad del robot y apunte siempre hacia adelante. Como podemos observar en la siguiente Figura la primera iteración de la carcaza se describe a continuación.

## Modificaciones de Hardware - Carcaza de Protección Iteración 1 

Para la primera iteración de la carcasa 
se planteó un diseño de geometría simple, apegado a la forma original del agente robótico. Se aumentó la altura del robot en virtud de dar espacio para almacenar las baterías en el interior de la carcasa. Se colocaron tanto la cámara como el sensor de proximidad apuntando hacia el frente del robot y dado el grosor escogido para la carcasa este protege de mejor manera los componentes internos. 

Se observó que es necesario agregar ranuras de ventilación o un mecanismo activo para la depuración de aire caliente dentro del agente robótico ya que la placa de **Raspberry Pi** eleva la temperatura en el interior de la carcasa. Así mismo se obtuvo el hallazgo de la necesidad de cambiar la geometría de la carcasa en cuanto a la ubicación de la cámara ya que en caso de chocar con objetos frontales, este último componente puede verse severamente dañado.


## Modificaciones de Software - Interfaz de Conexión 

Derivado de que la plataforma de desarrollo del **AB2** es la **Raspberry Pi**, se encontraron dos métodos principales para la programación y manejo del agente robótico: un gestor remoto o vía ssh. Se realizaron pruebas con el programa Virtual Network Computing (VNC) como sistema de conexión remota. Para lo anterior se debe habilitar dicha interfaz en el menú de configuraciones de la placa de desarrollo y enlazar una cuenta. En el presente trabajo se utilizó la cuenta de correo del autor y se registraron perfiles de conexión para los tres agentes robóticos disponibles para el proyecto. Por el lado de ssh, el proceso de conexión es mas sencillo ya que se puede establecer por medio de una terminal ejecutando los comandos ``ssh usuario$@$direccion ip'' para posteriormente ingresar la contraseña.

Dependiendo de las necesidades, se encontró que ambos métodos poseen ventajas y desventajas. Debido a que el **AB2** tiene como objetivo ser una plataforma de movilidad no restringida se hace de vital importancia el uso eficiente de energía proveniente de las baterías. Para este proyecto se adquirieron baterías nuevas con el objetivo de evitar complicaciones en la autonomía del agente. Se observó que administrar los agentes vía VNC es intuitivo y fácil ya que hay una interfaz gráfica a manera de escritorio de por medio que permite realizar tareas como programar y almacenar códigos directamente en la memoria del agente Sin embargo se observó que este método consumió mayor potencia limitando el tiempo de uso de los agentes de entre 30 y 40 minutos con baterías de 2.2Ah completamente cargadas.Por otra parte la conexión vía ssh arrojó mejores resultados en cuanto autonomía ya que únicamente se requería una conexión por línea de comandos sin interfaz gráfica. Se realizaron pruebas de ejecución de códigos vía ssh y se observó que la autonomía se elevó a varios días aun considerando que las pruebas requirieron activar los motores y leds. 

Si bien el uso de VNC representó un mayor consumo de potencia se encontró que por medio del cambio de fondo de pantalla en cada uno de los agentes hacía mas fácil saber qué agente se está administrando. En ssh esa facilidad no se tuvo y en algunos puntos debido a que el aspecto de la línea de comandos es el mismo para todos los agentes a excepción del usuario corriendo en las placas de desarrollo se optó por usar un software que facilitara el proceso de conexión y el caso antes mencionado. Por ello se optó por utilizar el programa Termius, un cliente ssh que permite crear perfiles de conexión, agregar etiquetas y configurar contraseñas automáticas además de tener la capacidad de enviar archivos desde el equipo que ejecuta el programa hacia el equipo remoto. Esto facilitó la edición de códigos y su transferencia a los agentes que, en un principio con VNC se hacía vía memoria USB flash. 


Derivado de lo anterior se decidió por optar por el uso de ssh por medio de Termius para la administración de los agentes robóticos. Cabe mencionar que para lograr la conexión ssh o VNC primero se debió configurar los agentes para que reconocieran y establecieran conexión con la red inalámbrica del sistema Robotat. 

## Modificaciones de Software - Nombramiento de Agentes

Para establecer un orden en cuanto a las pruebas, facilitar el proceso de conexión con los agentes se establecieron direcciones ip estáticas para los agentes robóticos y para la computadora del autor. Derivado de que la plataforma **AB2** posee un puerto de conexión estándar para los pines de propósito genera, así de que existen varias versiones de placa de desarrollo compatibles con este puerto se optó por diversificar el uso en cuanto a modelo de Raspberry Pi**. En la tabla 1 podemos observar resumido el esquema de direccionamiento para este proyecto. Se abargó el rango de direcciones estáticas desde la 192.168.50.60 hasta la 192.168.50.68. Las primeras 5 direcciones pensadas en servir como direcciones para equipos de cómputo del autor y en el futuro para futuros investigadores y el rango de la 65 a la 68 para 4 agentes robóticos. Si bien solo se cuenta con 3 agentes robóticos completos, se pretende dejar reservado el espacio para un agente mas y de momento implementarlo en un solo agente robótico con posibilidad de intercambiar las placas, específicamente entre el agente A1 y A2.

## Modificaciones de Software - Librería de Funciones

