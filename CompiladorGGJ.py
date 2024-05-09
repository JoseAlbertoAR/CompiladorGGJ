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
        (r'\(', 'OPEN_PARENTHESIS'),
    (r'\)', 'CLOSE_PARENTHESIS'),
    (r'\[', 'OPEN_BRACKET'),
    (r'\]', 'CLOSE_BRACKET'),
    (r'{', 'OPEN_BRACE'),
    (r'}', 'CLOSE_BRACE'),
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

"""def tokenize(text):
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
    return tokens, variables"""

def tokenize(text):
    tokens = []
    is_comment = False
    comment_buffer = ""
    variables = set()
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
                if token_type == 'COMMENT':
                    if not is_comment:
                        is_comment = True
                        comment_buffer = ""  # Limpiar buffer de comentarios
                    comment_buffer += token + "\n"  # Agregar línea de comentario al buffer
                    break
                if not is_comment:
                    if token_type == 'VARIABLE':
                        variables.add(token.split()[1])
                    tokens.append((token_type, match.group(), current_line))
        current_line += 1
        if is_comment and not line.strip().endswith("#>"):
            continue  # Si todavía estamos en un comentario, saltar al siguiente ciclo
        elif is_comment:  # Si hemos alcanzado el final del comentario
            tokens.append(('COMMENT', comment_buffer.strip(), current_line - len(comment_buffer.split('\n')) + 1))
            is_comment = False
            comment_buffer = ""         
    return tokens, variables

filename = input("Por favor, ingrese el nombre del archivo: ")

try:
    texto = read_text_from_file(filename)
    tokens, variables = tokenize(texto)

    # Imprimir los tokens y emparejarlos con los que se definieron
    table_headers = ["Tipo de Token", "Token","Línea"]
    table_data = [(token_type, token, line) for token_type, token, line in tokens]
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
