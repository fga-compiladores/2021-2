#!/bin/env python
import sys

good_chars = "<>+-.,[]"
template = """
#include<stdio.h>

void main() {
<body>
}
"""

def compiler(src):
    lines = [
        "char array[30000] = {0};",
        "char *ptr = array;",
    ]

    for c in src:
        if c == ">": 
            lines.append("++ptr;")
        elif c == "<": 
            lines.append("--ptr;")
        elif c == "+": 
            lines.append("++*ptr;")
        elif c == "-": 
            lines.append("--*ptr;")
        elif c == ".": 
            lines.append("putchar(*ptr);")
        elif c == ",": 
            lines.append("*ptr = getchar();")
        elif c == "[": 
            lines.append("while (*ptr) {")
        elif c == "]": 
            lines.append("}")
        else:
            continue

    body = '\n'.join('    ' + line for line in lines)
    return template.replace('<body>', body)


def main():
    filename = sys.argv[-1]
    with open(filename, "r") as fd:
        src = fd.read()
    dest = compiler(src)
    print(dest)


main()
