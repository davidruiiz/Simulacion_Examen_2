class 


def extraer_palabras_clave(string):
    #Los signos de libra por sí solos no cuentan, por ejemplo: la cadena "#" devolvería una matriz vacía.
    #Los hashtags no pueden estar en medio de una palabra (por ejemplo, "hashtag en #línea" devuelve una matriz vacía)
    #Los hashtags deben preceder a los caracteres alfabéticos (por ejemplo, "#120398" o "#?" no son válidos)

    if string == '':
        return []
    palabras_clave = []
    string = string.split()
    for i in range(len(string)):
        if string[i][0] == '#':
            if string[i][1:].isalpha():
                palabras_clave.append(string[i][1:])
       
    return palabras_clave

def palabra_precedida_por_mas_de_un_hasthag(string):
    #Si una palabra está precedida por más de un hashtag, solo cuenta el último hashtag (por ejemplo, "##alot" devolvería ["alot"])

    if string == '':
        return []
    palabras_clave = []
    string = string.split()
    for i in range(len(string)):
        if string[i][0] == '#':
            if string[i][1:].isalpha():
                palabras_clave.append(string[i][1:])

    return palabras_clave



if __name__=='__main__':
    print(extraer_palabras_clave("Esto es un #ejemplo de #extracción de #palabras clave"))
    print(extraer_palabras_clave("#"))
    print(extraer_palabras_clave("##alot"))
    print(extraer_palabras_clave("hashtag en #línea"))
    print(extraer_palabras_clave("#120398"))

