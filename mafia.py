import random

# Función para preguntar al usuario el número de civiles y de mafia
def preguntar_roles():
    while True:
        civiles = int(input("Ingrese el número de civiles: "))
        mafia = int(input("Ingrese el número de mafia: "))
        if civiles == mafia:
            print("El número de civiles y mafia debe ser diferente.")
        elif civiles < mafia:
            print("El número de civiles debe ser mayor  al número de mafia.")
        else:
            return civiles, mafia

# Función para eliminar un jugador
def eliminar_jugador(jugadores, civiles_total, mafia_total):
    while True:
        nombre = input("Ingrese el nombre del jugador a eliminar: ").lower()
        if nombre in jugadores.keys():
            rol = jugadores[nombre]
            del jugadores[nombre]
            if rol == "civil":
                civiles_total -= 1
            else:
                mafia_total -= 1
            print(f"{nombre} ({rol}) ha sido eliminado.")
            return civiles_total, mafia_total
        print("El jugador ingresado no existe.")
        
# Preguntar al usuario el número de civiles y de mafia
civiles, mafia = preguntar_roles()

# Preguntar los nombres de los jugadores y asignar roles aleatorios
jugadores = {}
roles = ["civil"] * civiles + ["mafia"] * mafia
random.shuffle(roles)

""" for i in range(civiles + mafia):
    nombre = input("Ingrese el nombre del jugador: ")
    jugadores[nombre] = roles[i]
    print(f"{nombre} tiene el rol de {roles[i]}") """

for i in range(civiles + mafia):
    nombre = input("Ingrese el nombre del jugador: ")
    jugadores[nombre] = roles[i]
    print(f"{nombre} tiene el rol de {roles[i]}")
    while True:
        continuar = input("Presione 'h' para continuar: ")
        if continuar == 'h':
            break

civiles_total = civiles
mafia_total = mafia

    
#print(jugadores)

# Eliminar jugadores hasta que se cumplan las reglas del juego
while True:
   
   if civiles_total == mafia_total:
        print("El número de civiles y mafia es igual. Los mafiosos ganan.")
        break
        if civiles_total == 0:
            print("Ganan los mafiosos.")
            break
   elif civiles_total < mafia_total:
        print("El número de civiles es menor que el número de mafia. Los mafiosos ganan.")
        print("Ganan los mafiosos.")
        break
   elif mafia_total == 0:
        print("Ganan los civiles.")
        break
   else:
        civiles_total, mafia_total = eliminar_jugador(jugadores, civiles_total, mafia_total)
        #print(f"El juego tiene {civiles_total} civiles y {mafia_total} mafia.")

