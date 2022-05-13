# Gramáticas EBNF


Considere as gramáticas no formato EBNF abaixo onde símbolos em letras minúsculas são considerados não-terminais e os símbolos em letra maiúsculas são considerados terminais e o símbolo inicial é representado pela letra "s". Produções vazias são representadas por ε.

**G1**
```
s : A s B
  | A B
```

**G2**
```
s : A B s
  | ε
```

**G3**
```
s : r A
r : A B r
  | ε
```

**G4**
```
s : A
  | s s B
```

**G5**
```
s : r 
  | t

t : r A
  | ε

r : t B
  | ε
```

**G6**
```
s : A
  | B
  | r

r : s s
  | ε
```

**Parte I (competência: cfg 4 pts)**

Classifique as sequências de símbolos abaixo de acordo com qual gramática elas pertencem. Uma sequência pode pertencer a mais de uma gramática. Deixamos a letra (a) resolvida no formato esperado para cada resposta.

Mantenha o ε como resposta das strings que não obedecem a nenhuma gramática.

a) AB: G1, G2, G5, G6
b) B: G5, G6
b) ABA: G3, G5
c) ABBA: ε
d) ABABAB: G2
e) BABA: G5
f) AABB: G1
h) AABAB: G4, G6

**Parte II (medalha cfg, se acertar todas)**

Resuma todas as gramáticas acima com uma descrição informal que diga intuitivamente o que cada linguagem representa. Você pode atribuir significados específicos aos símbolos terminais A e B, se necessário.

A descrição deve ser concisa e utilizar apenas uma linha.

G1) Sequência de n A's seguida de n B's (n >= 1).
G2) Sequência de 1 ou mais AB's.
G3) Sequência de 1 ou mais AB's seguida de um A.
G4) Operador sufixo, A = operando e B = operador.
G5) Sequências alternadas de A's e B's.
G6) Sequência de um ou mais A's e B's.
