import random

tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J','Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

def crearCadenaDNI():

    listaNums = []
    for i in range(8):

        numeroDNI = random.randint(0,9)
        
        listaNums.append(str(numeroDNI))

    unionNums = "".join(listaNums)
    return unionNums

def calcLetra():

    tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J','Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

    nums = crearCadenaDNI()

    posi = int(nums) % 23 

    dni = nums + tabla[posi]

    print (dni)
if __name__ == '__main__':

    calcLetra()