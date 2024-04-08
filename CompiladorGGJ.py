#Gabdiel Gersom Jair Adame Alquicira  
#Jose Alberto Alvarado Rosales
#Biblioteca para leer el archivo de texto
import sys

def obtener_parrafos(archivo):
    #Leer el archivo y obtener los párrafos
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
            #Obtener el texto en parrafos
            parrafos = texto.split('\n\n')
            return parrafos
    except FileNotFoundError:
        print("El archivo especificado no se encontró:", archivo)
        sys.exit(1)

def obtener_palabras(parrafo):
    # Quitar los caracteres especiales y dividir por espacios para obtener palabras
    palabras = parrafo.replace('\n', ' ').replace('\r', ' ').split()
    return palabras

def quitar_acentos(palabra):
    #Quitar los acentos
    letras_con_acento = ['á', 'é', 'í', 'ó', 'ú', 'ü', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']
    letras_sin_acento = ['a', 'e', 'i', 'o', 'u', 'u', 'A', 'E', 'I', 'O', 'U', 'U']

    #Colocar las palabras sin acento
    for i in range(len(letras_con_acento)):
        palabra = palabra.replace(letras_con_acento[i], letras_sin_acento[i])

    return palabra

def contar_palabras(parrafo):
    #Contar la cantidad de palabras en el párrafo
    palabras = obtener_palabras(parrafo)
    return len(palabras)

def main():
    #Validar si es un archivo
    if len(sys.argv) != 2:
        print("Uso: python programa.py archivo.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    parrafos = obtener_parrafos(archivo)

    total_palabras = 0
    palabras_por_parrafo = []  #Se crea lista para guardar la cantidad de palabras por párrafo

    print("Listado de palabras obtenidas por párrafos:")
    #Se obtienen las palabras de cada párrafo y se imprimen
    for i, parrafo in enumerate(parrafos, start=1):
        print(f"\nParrafo {i}:")
        palabras = obtener_palabras(parrafo)
        #Se imprimen las palabras sin acentos
        for palabra in palabras:
            palabra_sin_acento = quitar_acentos(palabra)
            print(palabra_sin_acento)
        num_palabras = contar_palabras(parrafo)
        palabras_por_parrafo.append(num_palabras)  #Se agregan la cantidad de palabras por párrafo a la lista
        total_palabras += num_palabras




    #Se imprimen la cantidad de palabras por párrafo
    for i, num_palabras in enumerate(palabras_por_parrafo, start=1):
        print(f"Cantidad de palabras en el párrafo {i}: {num_palabras}")
    #Se impreme la cantidad total de palabras en todos los párrafos
    print("Cantidad total de palabras en todos los párrafos:", total_palabras)

if __name__ == "__main__":
    main()
