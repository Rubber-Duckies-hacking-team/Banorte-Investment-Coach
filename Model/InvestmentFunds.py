# Asking about the amount of money in investment
inv = int(input("How much amount of money are you gonna invest?: "))
# Asking the time fram
tim = int(input("In how much time do you want to do the investment? (months): "))

if inv >= 100 and (tim >= 1 and tim < 3):
    print("Los fondos recomendados para ti son los Banorte Cete o Banorte Digital")

elif inv >= 100 and (tim > 1 and tim < 12): 
    print("El fondo recomendado para ti es el Banorte Plazo")

elif inv >= 100 and (tim >= 12 and tim < 24): 
    print("El fondo recomendado para ti es el Banorte Dolares")

elif inv >= 100 and (tim >= 24 and tim < 36): 
    print("El fondo recomendado para ti es el Banorte Dolares+")

elif inv >= 100 and (tim >= 36 and tim < 60): 
    print("El fondo recomendado para ti es el Fondo Estrategia")

elif inv >= 100 and tim >= 60: 
    print("El fondo recomendado para ti es el Banorte IPC")