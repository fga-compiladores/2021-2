#!/bin/sh
maestro-grades grade_exam prova-cfg
maestro-grades grade_exam prova-twine
maestro-grades collect --progress --output notas.xlsx
maestro-grades collect --output notas-pontos.xlsx
maestro-grades collect --by-grade --name --progress