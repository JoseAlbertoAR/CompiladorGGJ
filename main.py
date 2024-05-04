from CompiladorGGJ import process_file
from sintactico import main

tokens = process_file()
parsilntactico = main()
parsilntactico(tokens)

