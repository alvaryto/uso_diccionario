import diccionario as di

#try-step

def replace_with_dictionary(texto):
    dic=di.dictionary()
    for element in dic:
        texto=texto.replace(element, dic[element])
    return texto

def main():
    try:
        #marca de contexto#
        with open('texto.txt', 'r') as file:
            texto=file.read()

    except FileNotFoundError:#es una variable global, el open la pone a uno si no encuentra el archivo
        print("El archivo no se ha encontrado.")
    except Exception as e:
        print(e)
    else:
        print("Lectura exitosa")
        texto=replace_with_dictionary(texto)
        print(texto)

main()