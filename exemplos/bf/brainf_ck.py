#!/bin/env python
import sys

good_chars = "<>+-.,[]"
template = """
#include<stdio.h>

void main() {
<body>
}
"""
commands_c = {
    ">": "++i;",
    "<": "--i;",
    "+": "++array[i];",
    "-": "--array[i];",
    ".": "putchar(array[i]);",
    ",": "array[i] = getchar();",
    "[": "while (array[i]) {",
    "]": "}",
}

def compiler(src):
    lines = [
        "char array[30000] = {0};",
        "int i = 0;",
    ]

    for c in src:
        if (c_src := commands_c.get(c)):
            lines.append(c_src)

    body = "\n".join("    " + line for line in lines)
    return template.replace("<body>", body)


def main():
    filename = sys.argv[-1]
    with open(filename, "r") as fd:
        src = fd.read()
    dest = compiler(src)
    print(dest)

if __name__ == "__main__":
    main()
