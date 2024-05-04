#Archivo de reglas para el anilizador sintactico
reglas = {
    "0": {
      "lhs": "PROGRAM'",
      "len": 1,
      "result": [
        "PROGRAM"
      ]
    },
    "1": {
      "lhs": "PROGRAM",
      "len": 1,
      "result": [
        "DEF-LIST"
      ]
    },
    "2": {
      "lhs": "DEF-LIST",
      "len": 2,
      "result": [
        "DEF-LIST",
        "DEF"
      ]
    },
    "3": {
      "lhs": "DEF-LIST",
      "len": 0,
      "result": []
    },
    "4": {
      "lhs": "DEF",
      "len": 1,
      "result": [
        "VAR-DEF"
      ]
    },
    "5": {
      "lhs": "DEF",
      "len": 1,
      "result": [
        "FUN-DEF"
      ]
    },
    "6": {
      "lhs": "VAR-DEF",
      "len": 3,
      "result": [
        "var",
        "VAR-LIST",
        ";"
      ]
    },
    "7": {
      "lhs": "VAR-LIST",
      "len": 1,
      "result": [
        "ID-LIST"
      ]
    },
    "8": {
      "lhs": "ID-LIST",
      "len": 2,
      "result": [
        "ID",
        "ID-LIST-CONT"
      ]
    },
    "9": {
      "lhs": "ID-LIST-CONT",
      "len": 3,
      "result": [
        ",",
        "ID",
        "ID-LIST-CONT"
      ]
    },
    "10": {
      "lhs": "ID-LIST-CONT",
      "len": 0,
      "result": []
    },
    "11": {
      "lhs": "FUN-DEF",
      "len": 8,
      "result": [
        "ID",
        "(",
        "PARAM-LIST",
        ")",
        "{",
        "VAR-DEF-LIST",
        "STMT-LIST",
        "}"
      ]
    },
    "12": {
      "lhs": "PARAM-LIST",
      "len": 1,
      "result": [
        "ID-LIST"
      ]
    },
    "13": {
      "lhs": "PARAM-LIST",
      "len": 0,
      "result": []
    },
    "14": {
      "lhs": "VAR-DEF-LIST",
      "len": 2,
      "result": [
        "VAR-DEF-LIST",
        "VAR-DEF"
      ]
    },
    "15": {
      "lhs": "VAR-DEF-LIST",
      "len": 0,
      "result": []
    },
    "16": {
      "lhs": "STMT-LIST",
      "len": 2,
      "result": [
        "STMT-LIST",
        "STMT"
      ]
    },
    "17": {
      "lhs": "STMT-LIST",
      "len": 0,
      "result": []
    },
    "18": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-ASSIGN"
      ]
    },
    "19": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-INCR"
      ]
    },
    "20": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-DECR"
      ]
    },
    "21": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-FUN-CALL"
      ]
    },
    "22": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-IF"
      ]
    },
    "23": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-WHILE"
      ]
    },
    "24": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-DO-WHILE"
      ]
    },
    "25": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-BREAK"
      ]
    },
    "26": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-RETURN"
      ]
    },
    "27": {
      "lhs": "STMT",
      "len": 1,
      "result": [
        "STMT-EMPTY"
      ]
    },
    "28": {
      "lhs": "STMT-ASSIGN",
      "len": 4,
      "result": [
        "ID",
        "=",
        "EXPR",
        ";"
      ]
    },
    "29": {
      "lhs": "STMT-INCR",
      "len": 3,
      "result": [
        "inc",
        "ID",
        ";"
      ]
    },
    "30": {
      "lhs": "STMT-DECR",
      "len": 3,
      "result": [
        "dec",
        "ID",
        ";"
      ]
    },
    "31": {
      "lhs": "STMT-FUN-CALL",
      "len": 2,
      "result": [
        "FUN-CALL",
        ";"
      ]
    },
    "32": {
      "lhs": "FUN-CALL",
      "len": 4,
      "result": [
        "ID",
        "(",
        "EXPR-LIST",
        ")"
      ]
    },
    "33": {
      "lhs": "EXPR-LIST",
      "len": 2,
      "result": [
        "EXPR",
        "EXPR-LIST-CONT"
      ]
    },
    "34": {
      "lhs": "EXPR-LIST",
      "len": 0,
      "result": []
    },
    "35": {
      "lhs": "EXPR-LIST-CONT",
      "len": 3,
      "result": [
        ",",
        "EXPR",
        "EXPR-LIST-CONT"
      ]
    },
    "36": {
      "lhs": "EXPR-LIST-CONT",
      "len": 0,
      "result": []
    },
    "37": {
      "lhs": "STMT-IF",
      "len": 9,
      "result": [
        "if",
        "(",
        "EXPR",
        ")",
        "{",
        "STMT-LIST",
        "}",
        "ELSE-IF-LIST",
        "ELSE"
      ]
    },
    "38": {
      "lhs": "ELSE-IF-LIST",
      "len": 8,
      "result": [
        "ELSE-IF-LIST",
        "elseif",
        "(",
        "EXPR",
        ")",
        "{",
        "STMT-LIST",
        "}"
      ]
    },
    "39": {
      "lhs": "ELSE-IF-LIST",
      "len": 0,
      "result": []
    },
    "40": {
      "lhs": "ELSE",
      "len": 4,
      "result": [
        "else",
        "{",
        "STMT-LIST",
        "}"
      ]
    },
    "41": {
      "lhs": "ELSE",
      "len": 0,
      "result": []
    },
    "42": {
      "lhs": "STMT-WHILE",
      "len": 7,
      "result": [
        "while",
        "(",
        "EXPR",
        ")",
        "{",
        "STMT-LIST",
        "}"
      ]
    },
    "43": {
      "lhs": "STMT-DO-WHILE",
      "len": 9,
      "result": [
        "do",
        "{",
        "STMT-LIST",
        "}",
        "while",
        "(",
        "EXPR",
        ")",
        ";"
      ]
    },
    "44": {
      "lhs": "STMT-BREAK",
      "len": 2,
      "result": [
        "break",
        ";"
      ]
    },
    "45": {
      "lhs": "STMT-RETURN",
      "len": 3,
      "result": [
        "return",
        "EXPR",
        ";"
      ]
    },
    "46": {
      "lhs": "STMT-EMPTY",
      "len": 1,
      "result": [
        ";"
      ]
    },
    "47": {
      "lhs": "EXPR",
      "len": 1,
      "result": [
        "EXPR-OR"
      ]
    },
    "48": {
      "lhs": "EXPR-OR",
      "len": 3,
      "result": [
        "EXPR-AND",
        "OP-OR",
        "EXPR-AND"
      ]
    },
    "49": {
      "lhs": "OP-OR",
      "len": 1,
      "result": [
        "||"
      ]
    },
    "50": {
      "lhs": "OP-OR",
      "len": 1,
      "result": [
        "^"
      ]
    },
    "51": {
      "lhs": "EXPR-OR",
      "len": 1,
      "result": [
        "EXPR-AND"
      ]
    },
    "52": {
      "lhs": "EXPR-AND",
      "len": 3,
      "result": [
        "EXPR-AND",
        "&&",
        "EXPR-COMP"
      ]
    },
    "53": {
      "lhs": "EXPR-AND",
      "len": 1,
      "result": [
        "EXPR-COMP"
      ]
    },
    "54": {
      "lhs": "EXPR-COMP",
      "len": 3,
      "result": [
        "EXPR-COMP",
        "OP-COMP",
        "EXPR-REL"
      ]
    },
    "55": {
      "lhs": "EXPR-COMP",
      "len": 1,
      "result": [
        "EXPR-REL"
      ]
    },
    "56": {
      "lhs": "OP-COMP",
      "len": 1,
      "result": [
        "=="
      ]
    },
    "57": {
      "lhs": "OP-COMP",
      "len": 1,
      "result": [
        "!="
      ]
    },
    "58": {
      "lhs": "EXPR-REL",
      "len": 3,
      "result": [
        "EXPR-REL",
        "OP-REL",
        "EXPR-ADD"
      ]
    },
    "59": {
      "lhs": "EXPR-REL",
      "len": 1,
      "result": [
        "EXPR-ADD"
      ]
    },
    "60": {
      "lhs": "OP-REL",
      "len": 1,
      "result": [
        "<"
      ]
    },
    "61": {
      "lhs": "OP-REL",
      "len": 1,
      "result": [
        "<="
      ]
    },
    "62": {
      "lhs": "OP-REL",
      "len": 1,
      "result": [
        ">"
      ]
    },
    "63": {
      "lhs": "OP-REL",
      "len": 1,
      "result": [
        ">="
      ]
    },
    "64": {
      "lhs": "EXPR-ADD",
      "len": 3,
      "result": [
        "EXPR-ADD",
        "OP-ADD",
        "EXPR-MUL"
      ]
    },
    "65": {
      "lhs": "EXPR-ADD",
      "len": 1,
      "result": [
        "EXPR-MUL"
      ]
    },
    "66": {
      "lhs": "OP-ADD",
      "len": 1,
      "result": [
        "+"
      ]
    },
    "67": {
      "lhs": "OP-ADD",
      "len": 1,
      "result": [
        "-"
      ]
    },
    "68": {
      "lhs": "EXPR-MUL",
      "len": 3,
      "result": [
        "EXPR-MUL",
        "OP-MUL",
        "EXPR-UNARY"
      ]
    },
    "69": {
      "lhs": "EXPR-MUL",
      "len": 1,
      "result": [
        "EXPR-UNARY"
      ]
    },
    "70": {
      "lhs": "OP-MUL",
      "len": 1,
      "result": [
        "*"
      ]
    },
    "71": {
      "lhs": "OP-MUL",
      "len": 1,
      "result": [
        "/"
      ]
    },
    "72": {
      "lhs": "OP-MUL",
      "len": 1,
      "result": [
        "%"
      ]
    },
    "73": {
      "lhs": "EXPR-UNARY",
      "len": 2,
      "result": [
        "OP-UNARY",
        "EXPR-UNARY"
      ]
    },
    "74": {
      "lhs": "EXPR-UNARY",
      "len": 1,
      "result": [
        "EXPR-PRIMARY"
      ]
    },
    "75": {
      "lhs": "OP-UNARY",
      "len": 1,
      "result": [
        "+"
      ]
    },
    "76": {
      "lhs": "OP-UNARY",
      "len": 1,
      "result": [
        "-"
      ]
    },
    "77": {
      "lhs": "OP-UNARY",
      "len": 1,
      "result": [
        "!"
      ]
    },
    "78": {
      "lhs": "EXPR-PRIMARY",
      "len": 1,
      "result": [
        "ID"
      ]
    },
    "79": {
      "lhs": "EXPR-PRIMARY",
      "len": 1,
      "result": [
        "FUN-CALL"
      ]
    },
    "80": {
      "lhs": "EXPR-PRIMARY",
      "len": 1,
      "result": [
        "ARRAY"
      ]
    },
    "81": {
      "lhs": "EXPR-PRIMARY",
      "len": 1,
      "result": [
        "LIT"
      ]
    },
    "82": {
      "lhs": "EXPR-PRIMARY",
      "len": 3,
      "result": [
        "(",
        "EXPR",
        ")"
      ]
    },
    "83": {
      "lhs": "ARRAY",
      "len": 3,
      "result": [
        "[",
        "EXPR-LIST",
        "]"
      ]
    },
    "84": {
      "lhs": "LIT",
      "len": 1,
      "result": [
        "LIT-BOOL"
      ]
    },
    "85": {
      "lhs": "LIT",
      "len": 1,
      "result": [
        "LIT-INT"
      ]
    },
    "86": {
      "lhs": "LIT",
      "len": 1,
      "result": [
        "LIT-CHAR"
      ]
    },
    "87": {
      "lhs": "LIT",
      "len": 1,
      "result": [
        "LIT-STR"
      ]
    }
}