# Luis-Nij-Tesis-2022
Repositorio para documentos, archivos y códigos para tesis de Luis Nij.


# Alphabot2 -  Robot diferencial comercial

AlphaBot es el nombre con el que se denomina a una serie de productos desarrollados por la empresa china WaveShare Electronics. Esta línea de productos posee, hasta el momento, dos versiones de de robots móviles con interfaz para las placas de desarrollo Arduino Uno y Raspberry Pi. Ambas versiones poseen documentación general relativamente reciente en el sitio web oficial de la empresa, dicha información data del año 2017. 

Como lo indican en su página oficial, el AlphaBot es una plataforma de desarrollo robótica que conjuga elementos de placas electrónicas, armazón móvil y todo lo necesario para la locomoción del mismo. Se pretende que dicha plataforma dote al usuario de la capacidad de implementar proyectos por medio de los diferentes sensores disponibles en el robot. Algunos ejemplos involucran evasión de obstáculos, seguimiento de líneas, monitoreo con videocámara así como conectividad Bluetooth y/o WiFi dependiendo del modelo de AlphaBot utilizado. Esta oferta de plataforma robótica se encuentra en el rango de precio medio-alto comparado a otras ofertas de la misma empresa orientadas al sector de plataformas móviles con interfaz disponible para Raspberry Pi. Consultando el costo de venta (sin considerar costos de envío, nacionales o internacionales), el AlphaBot2 se ofrece desde los $98.99 USD la versión más sencilla sin placa de desarrollo Raspberry Pi hasta los $238.99 USD (la versión más completa).

![image](https://user-images.githubusercontent.com/60576547/202885375-8bfc6cfe-7512-4938-96c8-73ac50673eec.png)

# Alphabot2 -  ¿Donde Comenzar? 

Resulta útil contar con un conocimiento previo de programación básico de python, microcontroladores y conocimiento básico de electricidad y electrónica.
La plataforma Alphabot, como se mencionó anteriormente es un robot ensamblado de origen chino que puede utilizar Raspberry Pi o Arduino para funcionar dependiendo del modelo adquirido. En este repositorio se discutirá el funcionamiento y se brindarán descripciones y apoyo para la version que monta compatibilidad para modelos Raspberry Pi 3 en adelante. Así mismo, se brindará apoyo utilizando Python como lenguaje de programación y sus librerias asociadas 

# Alphabot2 -  Robótica de Enjambre

La robótica de enjambre estudia las diferentes estrategias de coordinación de un gran numero de robots simples. Se inspira en el comportamiento observado en insectos sociales, los cuales ejemplifican como un gran numero de individuos pueden interactuar entre sí para crear sistemas complejos e inteligentes. Cabe destacar que en este tipo de sistemas, el comportamiento colectivo surge de forma auto-organizada a partir de las acciones entre individuos y su entorno. Por tanto la inteligencia de enjambre es una característica que emerge como resultado de las interacciones de las masas.

En este tipo de sistemas, el enjambre se caracteriza por ser un conjunto de individuos capaces de agregar nuevos miembros (sistema con capacidad de cambio en numero de elementos), tener movimiento coordinado y capacidad de dispersarse. Organizados como enjambre, los robots son capaces de realizar tareas colectivas mucho más complejas y demandantes las cuales serían incapaces de realizar si trabajaran de manera individual. Además, a nivel de implementación siempre resulta mucho mas conveniente el diseño y construcción de sistemas roboticos de menor complejidad

# Alphabot2 -  Programación Multi hilos

En el ámbito de la programación, se habla de hilos de ejecución, también conocidos como procesos ligeros, a una estrategia de implementación de software que tiene como objetivo evitar el desperdicio de recursos en el sistema. Una de las principales razones por la que los sistemas computacionales se vuelven lentos en la ejecución de tareas es por la continua interacción entre procesador y memoria y la asignación de espacio de memoria cada uno de los procesos agendados. Los hilos son rutinas independientes  de un proceso macro que puede tener uno o muchos hilos ejecutándose. Esto permite desarrollar tareas simultaneamente en un mismo programa en lugar de ser desarrolladas de manera secuencial. La implementación de hilos permite la perspectiva al hilo de ejecución de tener exclusividad en sus recursos asignados. \cite{hilos}

Si bien la implementación de hilos en un proceso permite agilizar el uso de recursos y optimizar el rendimiento, n siempre resulta conveniente utilizarlos. Casos en donde las tareas dependan de un resultado anterior o del resultado de otras tareas resultan incompatibles para el uso de hilos. El uso de hilos de ejecución resulta conveniente cuando hablamos de tareas con objetivos diferentes entre sí. 

## Alphabot2 -  Ordenadores Raspberry Pi

Raspberry Pi es el nombre de una serie de mini ordenadores diseñados por la Fundación Raspberry Pi, una organización de origen inglés dedicada a difusión de educación en temas de computación. Esta serie de computadoras fue lanzada al mercado en 2012 y desde entonces ha desarrollado diferentes iteraciones mejorando las capacidades de hardware\cite{whatisRPi}.

El modelo original de Raspberry tuvo un procesador de un único núcleo con 700MHz de velocidad e incorporaba 256 MB de memoria RAM. Los computadores de este tipo se han caracterizado por tratar de hacer asequible la adquisición de los mismos lo que se refleja en los precios de compra directos con la Fundación Raspberry Pi. Concretamente estos ordenadores han costado en promedio 35 dólares americanos (USD) y poseen modelos tan económicos como 5 dólares \cite{whatisRPi}.

Desde su lanzamiento, la plataforma Raspberry Pi ha tenido una aceptación notable al rededor del mundo ya que muchas personas la utilizan para aprender y desarrollar proyectos de programación y electrónica. Gracias a que estas tarjetas electrónicas incorporan pines físicos es posible realizar tareas en las que el procesador interactúe con elementos y circuitería externa. Esto ha dotado de multitud de posibilidades a la tarjeta electrónica lo cual se ve reflejado en su popularidad en la comunidad de desarrolladores, estudiantes y entusiastas.