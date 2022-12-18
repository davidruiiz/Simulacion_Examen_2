# En algunos países de la antigua Unión Soviética existía la creencia de los boletos de la
# suerte. Se creía que un billete de transporte de cualquier tipo traía suerte si la suma de los
# dígitos de la mitad izquierda de su número era igual a la suma de los dígitos de la mitad
# derecha. Aquí hay ejemplos de tales números:
# 003111 # 3 = 1 + 1 + 1
# 813372 # 8 + 1 + 3 = 3 + 7 + 2
# 17935 # 1 + 7 = 3 + 5 // si la longitud es impar, debes ignorar el número del medio al
# sumar las mitades.
# 56328116 # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
# Dichos boletos se comían después de usarlos o se recolectaban para fanfarronear.
# Su tarea es escribir una función luck_check(str), que devuelve true/Truesi el argumento es una
# representación decimal de cadena de un número de boleto de la suerte, o false/Falsepara
# todos los demás números. Debería arrojar errores para cadenas vacías o cadenas que no
# representan un número decimal.

def suma_cadena_num(num):
    suma = 0
    for i in range(len(num)):
        suma += int(num[i])
    return suma

def luck_check(str):
    if str == "":
        raise ValueError("No se puede ingresar una cadena vacía")
    elif not str.isdigit():
        raise ValueError("No se puede ingresar una cadena que no sea un número")
    elif len(str) % 2 == 0:
        mitad1 = str[:len(str)//2]
        mitad2 = str[len(str)//2:]
    else:
        mitad1 = str[:len(str)//2]
        mitad2 = str[len(str)//2+1:]
    suma1 = suma_cadena_num(mitad1)
    suma2 = suma_cadena_num(mitad2)
    if suma1 == suma2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(luck_check("16325"))
    print(luck_check("1237321"))