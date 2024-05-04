from action_table import action_table
from GOTO_table import goto_table
from reglas import reglas

stack = [0]

def parsilntactico(tokens):
    # Inicialización de tokens
    init_tokens = tokens[:]
    init_tokens.append((None, "$"))
    tokens = init_tokens[:]

    # Obtener la acción inicial y el estado inicial
    act, state = action(stack[-1], tokens[0])
    print(stack, [act, state])

    # Loop principal del análisis
    while tokens:
        # Realizar la acción correspondiente
        if act == 'S':
            shift(tokens[0][1], state)
            tokens.pop(0)
        elif act == 'R':
            len, rule = look_reduction(state)
            reduce(len, rule)
        elif act == 'A':
            print("SUCCESS!")
            break
        else:
            print('ERROR: token not expected', tokens[0])
            break

        # Obtener la próxima acción y estado
        try:
            act, state = action(stack[-1], tokens[0])
        except Exception as error:
            print('ERROR:', error)
            break

        # Mostrar la pila y la próxima acción/estado
        print(stack, [act, state])

def reduce(len, t):
    # Reducir la pila según la regla especificada
    if len * 2 <= len(stack):
        if len > 0:
            del stack[-len * 2:]

    # Obtener el nuevo estado
    new_t = goto(stack[-1], t)
    stack.append(t)
    print(stack, [new_t])
    stack.append(new_t)

def shift(t, s):
    # Realizar el cambio de estado y agregar el token a la pila
    stack.append(t)
    stack.append(s)

def look_reduction(state):
    # Buscar la regla de reducción para un estado dado
    rule = reglas[state]["lhs"]
    len = reglas[state]["len"]
    return len, rule

def action(i, a):
    # Obtener la acción correspondiente desde la tabla de acciones
    return action_table[i][a]

def goto(state, rule):
    # Obtener el estado al que se transita según la tabla goto
    return goto_table[state][rule]


def main():
    return parsilntactico

if __name__ == "__main__":
    main()