def get_fondo(inv,tim):    

    if inv >= 100 and (tim >= 1 and tim < 12):
        print("""Los fondos recomendados para ti son los Banorte Cete o Banorte Digital 
              
              Fondo Banorte Cete (NTECT):
              Se trata de un fondo 100% de deuda con un horizonte de inversion a corto plazo, 
              este tipo de fondo te permitira obtener un rendimiento adicional a tus ahorros,
              sin permanencia minima y con la liquidez inmediata que necesitas, el riesgo 
              de este fondo es extremadamente bajo y va dirigido a inversionistas que buscan 
              hacer crecer sus ahorros. Ideal para el perfil de Preservacion de Captial que 
              mantiene estable su capital sin correr riesgos.
              
              Fondo Banorte Digital (NTEDIG):
              Se trata de un fondo 100% de deuda con un horizonte de inversion a corto plazo, 
              este tipo de fondo opera completamente en linea y por sus comisiones preferenciales
              te permitira obtener un rendimiento adicional a tus ahorros, sin permanencia minima
              y con la liquidez inmediata que necesitas, el riesgo de este fondo es extremadamente bajo 
              y va dirigido a inversionistas que buscan hacer crecer sus ahorros de una forma totalmente
              digital. Ideal para el perfil de Preservacion de Captial que mantiene estable su capital 
              sin correr riesgos.""")

    elif inv >= 50000 and (tim >= 3 and tim < 12): 
        print("""El fondo recomendado para ti es el Banorte Plazo, se trata de un fondo 100% de deuda 
              con un horizonte de inversion a corto plazo, este tipo de fondo te permitira proteger 
              tu capital y conocer tu rendimiento desde el inicio de la inversion, con una permanencia 
              minima de 91 dias y con una inversion minima de $50,000, el riesgo de este fondo es extremadamente 
              bajo y va diriigo a inversionistas que buscan obtener un premio adicional por su permanencia.""")

    elif inv >= 100 and (tim >= 12 and tim < 24): 
        print("""El fondo recomendado para ti es el Banorte Dolares (NTEDLS), se trata de un fondo conformado 
              principalmente por activos de deuda con la mejor calidad crediticia (AAA) denominados, 
              indizados y/o referenciados al dolar, este fondo te permitira respaldar el valor de tu
              dinero ante las fluctuaciones del tipo de cambio peso-dolar, el riesgo de este fondo es 
              bajo. Dirigido a inversionistas que buscan estabilidad y un mejor resguardo del valor del peso
              respecto al dolar (USD). Ideal para el perfil de Preservacion de Capital que mantiene estable
              su capital sin correr riesgos.""")

    elif inv >= 100 and (tim >= 24 and tim < 36): 
        print("""El fondo recomendado para ti es el Banorte Dolares+ (NTEDLS+), se trata de un fondo conformado
              principalmente por activos denominados en dolares, este fondo es de tipo de Renta Variable en Dolares
              por lo que te permitira acceder a una estrategia de cobertura cambiaria (peso-dolar) con un
              rendimiento adicional, el riesgo del fondo es moderado. Dirigido a inversionistas que buscan una 
              inversion internacional. Ideal para el perfil Conservador que busca hacer crecer su capital de manera
              establ, con cierto riesgo y volatilidad acotada.""")

    elif inv >= 100 and (tim >= 36 and tim < 60): 
        print("""El fondo recomendado para ti es el Fondo Estrategia (NTED-NTE1-NTE2-NTE3)
              
              Fondo Estrategia (NTED):
              Es un fondo 100% de deuda con horizonte de inversion a mediano plazo, el tipo es de Deuda por lo que 
              cuenta con una estrategia relativamente conservadora de seleccion de activos que te permite preservar y
              mejorar tu patrimonio, el riesgo es moderado. Dirigido a inversionistas que buscan un rendimiento 
              superior a la deuda gubernamental. Idel para el perfil Conservador que busca hacer crecer su capital de
              manera estable, con cierto riesgo y volatilidad acotada. 
              
              Fondo Estrategia (NTE1):
              Es un fondo que invierte alrededor del 80% de los activos de su cartera en instrumentos de Deuda, y el 20%
              en instrumentos de Renta Variable. Los valores podran estar invertidos en mercados locales e internacionales.
              Obtendras mayores rendimientos con un horizonte de Inversion a largo plazo. La exposicion por tipo de activo 
              del Fondo puede llegar a variar. El fondo es de tipo Estrategia Discrecional, cuenta con una menor exposicion
              a la Renta Variable como las acciones y los ETF's (Exchange Traded Funds), y una mayor exposicion a Deuda, el 
              riesto es moderado a alto. Dirigido a inversionistas con una limitada tolerancia al riesgo, que buscan 
              diversificar y hacer crecer sus inversiones.
              
              Fondo Estrategia (NTE2):
              Es un fondo que invierte alrededor del 60% de los activos de su carter en instrumentos de Deuda, y el 40% en 
              instrumentos de Renta Variable. Los valores podran estar invertidos en mercados locales e internacionales. 
              Obtendras mayores rendimientos con un horizonte de inversion a largo plazo. El fondo es de tipo estrategia 
              discrecional, cuenta con un balance dentro de la composicion de su cartera, manteniendo mayor exposicion en 
              valores Deuda y menor en Renta Variable como las acciones y los ETF's (Exchange Traded Funds), es de riesgo alto. 
              Dirigida a inversionistas con una tolerancia moderada al riesgo que buscan diversificar y hacer crecer sus 
              inversiones. Ideal para el perfil Moderado que busca un crecimiento constante de capital con cierta estabilidad.
              Dispuesto a aceptar riesgo y volatilidad moderadas.

              Fondo Estrategia (NTE3):
              Es un fondo que invierte alrededor del 40% de los activos de su cartera en instrumentos de Deuda, y el 60%
              en instrumentos de Renta Variable. Los valores podran estar invertidos en mercados locales e internacionales. 
              Obtendras mayores rendimientos con un horizonte de inversion a largo plazo. Este fondo es de tipo Estrategia
              Discrecional, invertira los valores con una mayor exposicion en instrumentos de Renta Variable como las acciones
              y los ETF's (Exchange Traded Funds), y en menor proporcion en instrumentos de Deuda, el nivel de riesgo es alto.
              Dirigido a inversionistas con alta tolerancia al riesgo que buscan diversificar sus inversiones para obtener mayores
              rendimientos. Ideal para el perfil Balanceado que busca un crecimiento importante de capital en el largo plazo.
              """)

    elif inv >= 100 and tim >= 60: 
        print("""El fondo recomendado para ti es el Banorte IPC+ (NTEIPC+), este fondo invierte al menos 90% de su
              cartera en acciones de empresas enlistadas en las Bolsas de Valores y en menor proporcion
              en instrumentos de Deuda Nacional e Internacional, permitiendo asi obtener mayores rendimientos con
              un horizonte de inversion a largo plazo. Este tipo de fondo es de Renta Variable, referenciado al 
              Indice de Precios y Cotizaciones (IPC) de la Bolsa Mexicana de Valores, cuenta con un riesgo muy alto.
              Dirigido a clientes que buscan invertir en la Bolsa Mexicana de Valores con una seleccion mas agresiva
              en sus inversiones. Ideal para el perfil de Crecimiento cuyo objetivo es forjar un patrimonio a largo 
              plazo, aceptando un riesgo considerable y minusvalias sustanciales.""")
        
get_fondo(100,2)