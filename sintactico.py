from action_table import action_table
from GOTO_table import goto_table
from reglas import reglas

stack = [0]

def parsilntactico(ttokens):
    # Inicialización de tokens
    init_tokens = tokens[:]
    init_tokens.append((None, "$"))
    tokens = init_tokens[:]

    # Obtener la acción inicial y el estado inicial
    act, state = action(str(stack[-1]), tokens[0])
    print(stack, [act, state])

    # Loop principal del análisis
    while tokens:
        # Realizar la acción correspondiente
        if act == 'S':
            shift(tokens[0][1], state)
            tokens.pop(0)
        elif act == 'R':
            rule_len, rule = look_reduction(state)
            print(f"Regla obtenida en la reducción: {rule}")

            reduce(rule_len, rule)
        elif act == 'A':
            print("Sin errores sintácticos.")
            break
        else:
            print('ERROR: token fuera de la tabla de simbolos', tokens[0][1])
            break

        # Obtener la próxima acción y estado
        try:
            act, state = action(str(stack[-1]), tokens[0][1])
        except Exception as error:
            print('ERROR:', error)
            break

        # Mostrar la pila y la próxima acción/estado
        print(stack, [act, state])

def reduce(rule_len, t):
    print(f"Regla pasada a la función reduce: {t}")
    # Reducir la pila según la regla especificada
    if rule_len * 2 <= len(stack):
        if rule_len > 0:
            del stack[-rule_len * 2:]

    # Obtener el nuevo estado
    new_t = goto(str(stack[-1]), t)
    stack.append(t)
    print(stack, [new_t])
    stack.append(new_t)
    print('Después de la reducción:', stack)

def shift(t, s):
    # Realizar el cambio de estado y agregar el token a la pila
    stack.append(t)
    stack.append(s)

def look_reduction(state):
    # Buscar la regla de reducción para un estado dado
    if str(state) not in reglas:
        raise Exception(f"No existe una regla para el estado {state}")
    rule = reglas[str(state)]["lhs"]
    print(f"Regla obtenida en look_reduction: {rule}")
    rule_len = reglas[str(state)]["len"]
    return rule_len, rule

def action(i, a):
    print(f"Estado y acción pasados a action: {i}, {a[1]}")  # Agregar esta línea

    # Obtener la acción correspondiente desde la tabla de acciones
    return action_table[i][a[1]]

def goto(state, rule):
    print(f"Estado y regla pasados a goto: {state}, {rule}")

    # Obtener el estado al que se transita según la tabla goto
    return goto_table[str(state)][rule]


def main():
    return parsilntactico

if __name__ == "__main__":
    main()