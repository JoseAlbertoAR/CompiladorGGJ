#Gabdiel Gersom Jair Adame Alquicira  
#Jose Alberto Alvarado Rosales
#Biblioteca para leer el archivo de texto
import re
from tabulate import tabulate

# Definir tokens
token_patterns = [
    (r'\b(while|if|else|do|main|brake|inc|prints|println|reads?)\b', 'KEYWORD'),
    (r'\b(add|get|set|inc|dec|reverse|size)\b', 'FUNCTION'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'\b(\d+)\b', 'INTEGER_CONSTANT'),
    (r'[+\-*/%=]', 'OPERATOR'),
    (r'==|!=|>=|<=|\=\>', 'COMPARISON_OPERATOR'),
    (r'!', 'LOGICAL_NOT'),
    (r'&&', 'LOGICAL_AND'),
    (r'\|\|', 'LOGICAL_OR'),
    (r'\^', 'LOGICAL_XOR'),
    (r'\b\w+´\b', 'SINGLE_QUOTE'),
    (r'(?<!\\)".*?(?<!\\)"', 'STRING_LITERAL'),
    (r'(?<!\\)\'', 'SINGLE_QUOTE'),
    (r'<#([\s\S]*?)#>', 'COMMENT'),
    (r'(?<!\\)\\r', 'CARRIAGE_RETURN'),
    (r';', 'SEMICOLON'), 
    (r'\bvar\s+\w+\b', 'VARIABLE'), 
    (r'[a-zA-Z_]\w*', 'IDENTIFIER')
]

def read_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def tokenize(text):
    tokens = []
    is_comment = False  
    variables = set()  
    for pattern, token_type in token_patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(text)
        for match in matches:
            token = match.group()
            if token_type == 'COMMENT':
                tokens.append((token_type, match.group(1))) 
                is_comment = True
                break 
            if not is_comment:
                if token_type == 'VARIABLE':
                    variables.add(token.split()[1])  
                tokens.append((token_type, token))
    return tokens, variables

filename = input("Por favor, ingrese el nombre del archivo: ")

try:
    texto = read_text_from_file(filename)
    tokens, variables = tokenize(texto)

    # Imprimir los tokens y emparejarlos con los que se definieron
    table_headers = ["Tipo de Token", "Token"]
    table_data = [(token_type, token) for token_type, token in tokens]
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    # Mostrar las variables encontradas
    if variables:
        print("\nVariables encontradas:")
        for var in variables:
            print(var)
    else:
        print("\nNo se encontraron variables.")

except FileNotFoundError:
    print(f"El archivo '{filename}' no se encontró.")
