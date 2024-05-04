#Gabdiel Gersom Jair Adame Alquicira  
#Jose Alberto Alvarado Rosales
#Biblioteca para leer el archivo de texto
import re

# Definir tokens
token_patterns = [
    (r'\b(var|while|if|else|do|main|prints|println|reads?)\b', 'KEYWORD'),
    (r'\b(add|get|set|inc|dec|reverse|size)\b', 'FUNCTION'),
    (r'\b(num|option|start|finish|temp|result|remainder)\b', 'VARIABLE'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'\b(\d+)\b', 'INTEGER_CONSTANT'),
    (r'[+\-*/%=]', 'OPERATOR'),
    (r'==|!=|>=|<=|\=\>', 'COMPARISON_OPERATOR'),
    (r'\(', 'OPEN_PARENTHESIS'),
    (r'\)', 'CLOSE_PARENTHESIS'),
    (r'\[', 'OPEN_BRACKET'),
    (r'\]', 'CLOSE_BRACKET'),
    (r'{', 'OPEN_BRACE'),
    (r'}', 'CLOSE_BRACE'),
    (r'\.', 'DOT_OPERATOR'),
    (r'".*?"', 'STRING_LITERAL'),
    (r'<#[\s\S]*?#>', 'COMMENT'),
    (r';', 'SEMICOLON'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER')
]
"""def read_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()"""

#modificado para que lea el texto por lineas
def read_text_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        lines = text.split('\n')
    return text, lines

# Identifica los tokens en el texto
def tokenize(text):
    tokens = []
    tokenReal = []
    lines = text.split('\n')
    current_line = 1
    # Itera sobre cada línea del texto dividido en líneas.
    # Esto permite procesar cada línea del texto por separado.
    for line in lines:
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            #Búsqueda de todas las coincidencias de un patrón regex
            #en este caso el token dentro de una línea de texto (line)
            matches = regex.finditer(line)
            for match in matches:
                token = match.group()
                #start_index = match.start()
                #end_index = match.end()
                tokens.append((token_type, match.group(), current_line))
                tokenReal.append((token_type))
                #print(tokenReal)
        current_line += 1
    return tokens
    #return tokenReal

def process_file():
    filename = input("Por favor, ingrese el nombre del archivo: ")
    try:
        texto, _ = read_text_from_file(filename)
        #Divide el texto en tokens
        tokens = tokenize(texto)
        for token in tokens:
            print(f"Token: {token[1]} (Tipo: {token[0]}) - Linea: {token[2]}")
            
    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encontró.")
    return tokens

def main():
    process_file()

if __name__ == "__main__":
    main()
