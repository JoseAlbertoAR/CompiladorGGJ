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
def read_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Identifica los tokens en el texto
def tokenize(text):
    tokens = []
    for pattern, token_type in token_patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(text)
        for match in matches:
            tokens.append((token_type, match.group()))
    return tokens

filename = input("Por favor, ingrese el nombre del archivo: ")

try:

    texto = read_text_from_file(filename)

    # Divide el texto en los tokens
    tokens = tokenize(texto)

    # Imprimir los tokens y emparejarlos con los que se definierons
    for token in tokens:
        print(f"Token: {token[1]} (Tipo: {token[0]})")

except FileNotFoundError:
    print(f"El archivo '{filename}' no se encontró.")
