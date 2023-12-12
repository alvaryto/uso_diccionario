import diccionario as di
import argparse

#try-step

def replace_with_dictionary(texto):
    dic=di.dictionary()
    for element in dic:
        texto=texto.replace(element, dic[element])
    return texto

def main():
    parser = argparse.ArgumentParser(description= 'Cambia siglas por su significado')
    parser.add_argument('archivo', help='archivo a cambiar')
    parser.add_argument('-i', '--imprimir', action='store_false', help='imprimir texto')
    args=parser.parse_args()
    try:
        #marca de contexto#
        with open(args.archivo, 'r') as file:
            texto=file.read()

    except FileNotFoundError:#es una variable global, el open la pone a uno si no encuentra el archivo
        print("El archivo no se ha encontrado.")
    except Exception as e:
        print(e)
    else:
        print("Lectura exitosa")
        texto=replace_with_dictionary(texto)
        if args.imprimir:
            print(texto)

main()