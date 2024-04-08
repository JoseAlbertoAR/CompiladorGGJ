#Gabdiel Gersom Jair Adame Alquicira  
#Jose Alberto Alvarado Rosales
#Biblioteca para leer el archivo de texto
import re

# Definir categorías de tokens
token_patterns = [
    (r'\b(var|while|return|if|else|do|main|prints|println|reads?)\b', 'KEYWORD'),
    (r'\b(add|get|set|inc|dec|reverse|size)\b', 'FUNCTION'),
    (r'\b(num|option|start|finish|temp|result|remainder)\b', 'VARIABLE'),
    (r'\b(true|false)\b', 'BOOLEAN'),  # Identificar booleanos
    (r'\b(\d+)\b', 'INTEGER_CONSTANT'),
    (r'[+\-*/%=]', 'OPERATOR'),
    (r'==|!=|>=|<=|\=\>', 'COMPARISON_OPERATOR'),
    (r'[()\[\]{};:,]', 'PUNCTUATION'),
    (r'\.', 'DOT_OPERATOR'),
    (r'".*?"', 'STRING_LITERAL'),
    (r'<#[\s\S]*?#>', 'COMMENT'),  # Comentario en el formato <# comentario #>, puede contener saltos de línea
    (r'\s+', 'WHITESPACE'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER')
]

# Función para leer el texto desde un archivo
def read_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Función para identificar tokens
def tokenize(text):
    tokens = []
    for pattern, token_type in token_patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(text)
        for match in matches:
            tokens.append((token_type, match.group()))
    return tokens

# Solicitar al usuario el nombre del archivo
filename = input("Por favor, ingrese el nombre del archivo: ")

try:
    # Leer el texto desde el archivo
    texto = read_text_from_file(filename)

    # Tokenizar el texto
    tokens = tokenize(texto)

    # Imprimir cada token uno a uno
    for token in tokens:
        print(token)

except FileNotFoundError:
    print(f"El archivo '{filename}' no se encontró.")
