# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
# */

#gana el aprtido con 2 sets


scoreboard = {"P1": 0, "P2": 0}
def updateScoreboard(winner, sets):
    print(f"Ha ganado {winner}") 
    scoreboard[winner] = scoreboard[winner]+1
    
    for score in scoreboard.values():
        if score == 2:
            print(f"\nEnd of the Game! {winner} wins!")
            return(winner, [])
    
    return (winner, sets)

def checkSet(set):
    p1, p2 = 0,0
    points = ["love", 15, 30, 40]
    set = list(set)

    for i in range(len(set)):
        if set[i] == "P1":
            p1 += 1
        elif set[i] == "P2":
            p2 += 1
        else:
            return (-2,[])  #codigos de error: Entrada invalida


        if p1 < 3 or p2 <3:        
            if p1 > 3 and p2 < 3:         #victoria para p1
                return updateScoreboard("P1",set[i+1:])

            elif p2 > 3 and p1 < 3:       #victoria para p2
                return updateScoreboard("P2",set[i+1:])  

            else:
                print(f'{points[p1]} - {points[p2]}')

        else:       #verifica estado de deuce

            if p1 == p2:                  #deuce
                print("Deuce")  

            elif p1 == p2+1:             #ventaja para p1
                print("Ventaja P1") 

            elif p2 == p1+1:             #ventaja para p2
                print("ventaja P2") 
                
            elif p1 >= p2+2:             #victoria para p1
                return updateScoreboard("P1",set[i+1:])

            elif p2 >= p1+2:             #victoria para p2
                return updateScoreboard("P2",set[i+1:])  

    return (-1,[])  #codigos de error: set incompleto
                    
        
        


if __name__ == "__main__":
    
    #sets = input("ingresa el resultado de los juegos: ")
    sets = [
        "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1",
        "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2",
        "P1", "P1", "P1", "P2", "P1", "P1", "P1", "P1"
    ]
    
    while(len(sets) > 0): #para mas sets
        winner, sets = checkSet(sets)
        print()

    if winner == -1:    #codigos de error
        print("\nerror en la entrada del set: Set incompleto")
    elif winner == -2:  #codigos de error
        print("\nerror en la entrada del set: Entrada invalida") 

    print(f'\nScoreboard: {scoreboard["P1"]}-{scoreboard["P2"]}')
