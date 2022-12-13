



def luck_check(lista):
    
    suma = 0

    for i in range(len(lista)):

        if lista[i] == 7:

            suma += 14

        else:

            suma += lista[i]

    return suma

if __name__=='__main__':
    print(luck_check([5, 7, 7]))
    print(luck_check([5, 7, 1, 8]))
    
