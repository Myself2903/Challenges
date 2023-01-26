''' 
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/
 '''

import math

def isPrime(num):   
    for i in [2,3,5,7]:
        if num == i:
            return True
        elif num%i == 0:
            return False

    i=11
    while i < num//2:
        if num%i == 0:
            return False
        i+= 2
    return True

def fibonacci(num):
    base = 5*math.pow(num,2)
    if math.sqrt(base+4).is_integer() or math.sqrt(base-4).is_integer():
        return True
    else:
        return False

def isEven(num):
    return num%2 == 0

if __name__ == "__main__":
    value = int(input("ingrese el numero que desea analizar: "))
    try:
        prime = f'{"" if isPrime(value) else " no"} es primo'
        fibonacci = f'{"" if fibonacci(value) else " no es"} fibonacci'
        even = f'{" es par" if isEven(value) else " es impar"}'
        print(f'{value}{prime},{fibonacci} y{even}')
    except:
        print("entrada invalida")
