# Gramáticas BNF

Considere as gramáticas EBNF abaixo escritas no formato EBNF. Remova todos os operadores extendidos, *, +, [], ?, etc e reescreva as gramáticas na notação BNF. Não é necessário modificar as gramáticas que já obedecem à notação BNF.

Considere que os símbolos não-terminais são escritos em letras minúsculas e os terminais em letras maiúsculas. Você pode criar novas regras, se necessário. Utilize ε para representar as produções vazias.


**G1**
```
s : A s B
  | A B
```

**G2**
```
s : A s
r : A r
  | ε
```

**G3**
```
s : A s
  | ε
```

**G4**
```
s : "[" r "]"
  | "[" "]"
r : A "," r
  | A
```

**G5**
```
s : "if" A "then" A
  | "if" A "then" A "else" r
r : s 
  | A
```
