#Gabdiel Gersom Jair Adame Alquicira  
#Jose Alberto Alvarado Rosales
#Biblioteca para leer el archivo de texto
import re

# Definir tokens
"""token_patterns = [
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
]"""
token_patterns = [
    (r'<#[\s\S]*?#>', 'CMT_ML'),
    (r'#.*', 'CMT_SL'),
    (r'break\b', 'break'),
    (r'dec\b', 'dec'),
    (r'do\b', 'do'),
    (r'else\b', 'else'),
    (r'elseif\b', 'elseif'),
    (r'if\b', 'if'),
    (r'inc\b', 'inc'),
    (r'return\b', 'return'),
    (r'var\b', 'var'),
    (r'while\b', 'while'),
    (r'[-]?[0-9]+', 'LIT-INT'),
    (r'(true|false)\b', 'LIT-BOOL'),
    (r"'(\\n|\\r|\\t|\\\'|\\\"|\\u[0-9a-fA-F]{6}|[\'\n\r])*'", 'LIT-CHAR'),
    (r'"(\\n|\\r|\\t|\\"|\\\'|\\u[0-9a-fA-F]{6}|["\n\r])*"', 'LIT-STR'),
    (r'\(', '('),
    (r'\)', ')'),
    (r'\[', '['),
    (r'\]', ']'),
    (r'\{', '{'),
    (r'\}', '}'),
    (r'\|\|', '||'),
    (r'&&', '&&'),
    (r'!=', '!='),
    (r'!', '!'),
    (r'\+', '+'),
    (r'-', '-'),
    (r'\*', '*'),
    (r'/', '/'),
    (r'<=', '<='),
    (r'>=', '>='),
    (r'==', '=='),
    (r'=', '='),
    (r'<', '<'),
    (r'>', '>'),
    (r'%', '%'),
    (r'\^', '^'),
    (r';', ';'),
    (r',', ','),
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'ID')
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
"""
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
                tokens.append((match.group(), token_type, current_line))
                #tokens.append((match.group(), token_type,))
                #tokenReal.append((match.group(),token_type))
                #print(tokenReal)
        current_line += 1
    return tokens
    #return tokenReal
    """
def tokenize(text):
    tokens = []
    lines = text.split('\n')
    current_line = 1

    for line in lines:
        position = 0
        while position < len(line):
            matches = []
            for pattern, token_type in token_patterns:
                regex = re.compile(pattern)
                match = regex.match(line, position)
                if match is not None:
                    matches.append((token_type, match.group(), match.start(), match.end()))
                    tokens.append((match.group(), token_type, match.start(), match.end()))

            if matches:
                # Elige el token que comienza en la posición más baja, y en caso de empate, el que tenga la longitud más larga.
                token_type, token, start, end = max(matches, key=lambda x: (x[2], x[3]-x[2]))
                tokens.append((token, token_type, current_line))
                position = end
            else:
                position += 1
        current_line += 1
    return tokens

def process_file():
    filename = input("Por favor, ingrese el nombre del archivo: ")
    try:
        texto, _ = read_text_from_file(filename)
        #Divide el texto en tokens
        tokens = tokenize(texto)
        for token in tokens:
            print(f"Token: {token[0]} (Tipo: {token[1]}) - Linea: {token[2]}")
            
    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encontró.")
    return tokens

def main():
    process_file()

if __name__ == "__main__":
    main()
