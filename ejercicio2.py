# El malvado gobierno de programación ha prohibido el uso de números. Su tarea, si elige
# aceptarla, es devolver números, sin usar números.
# Problemas:
# • No puede usar literales numéricos en su código fuente.
# • No puede usar la propiedad de longitud directamente en su código.
# Meta:
# • Tienes que devolver 'Puedo escribir números como 1, 2, 3'.

from word2number import w2n

def convertir(*args):
    lista ="puedo escribir numeros como "
    for index in args:
        if index != args[-1]:
            lista+=str(w2n.word_to_num(index))+", "
        else:
            lista+=str(w2n.word_to_num(index))+"."
    return lista



if __name__ == '__main__':
    print(convertir('one','two','three'))