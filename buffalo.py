#!/usr/bin/env python3

import argparse
from FileHandler import FileHandler, LineByLineReadStrategy
from Lexer import Lexer


def main():
    parser = argparse.ArgumentParser(
        description="Buffalo: tokenizador de archivos de texto conteniendo código de Python"
    )

    parser.add_argument("-f", "--file", type=str, help="El nombre del archivo")
    parser.add_argument("-o", "--output", type=str, help="El archivo de salida")

    try:
        args = parser.parse_args()
    except SystemExit:
        parser.print_help()
        exit(0)

    if args.file:
        path = args.file.strip()
        line_by_line_handler = FileHandler(path, LineByLineReadStrategy())
        lines = line_by_line_handler.read()

        lexer = Lexer(lines=lines)
        # tokens = lexer.tokenize()
        test = lexer.tokenize_with_automat()

        # if args.output:
        #     with open(args.output, 'w') as f:
        #         for token in tokens:
        #             f.write(f"{token}\n")
        # else:
        #     for token in tokens:
        #         print(token)
    else:
        print("No se proporcionó ningún archivo.")


if __name__ == "__main__":
    main()
