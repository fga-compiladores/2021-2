Start: 2022-01-17
End: 2022-05-05
Weekdays: Wed, Fri
Skip:
- 2022-02-28: *Feriado: Carnaval*
- 2022-03-01: *Feriado: Carnaval*
- 2022-03-02: *Feriado: Carnaval*
- 2022-04-15: *Feriado: Paixão de Cristo*
- 2022-04-22: *Feriado: Tiradentes*
----------------------------------------------------------
Início das aulas – Apresentação do curso  (síncrono)

* Linguagens e tecnologias adotadas.
* Métodos de avaliação.
* Materiais suplementares.
----------------------------------------------------------
Introdução ao Python I (síncrono)

* Variaveis e tipos básicos.
* Comandos básicos (if/for/while/def).
* Strings
* Compilador de Brainf*ck.
----------------------------------------------------------
Introdução ao Python II (síncrono)

* Ambientes do tipo notebook e interpretador.
* Estruturas de dados: dicionários, listas e tuplas
* Manipulação de strings
* Lidando com erros
----------------------------------------------------------
Laboratório de Python: Leitor de JSON

* Especificação do formato.
* Listas, dicionários e tipos atômicos.
* Descida recursiva.
* Testes automatizados.

Vídeo: https://www.youtube.com/watch?v=ub5nrnWyWvk
----------------------------------------------------------
Programação orientada a objetos

* Encapsulando estado.
* Métodos de uma classe.
* O parâmetro "self".
* Métodos especiais.

Vídeo: https://www.youtube.com/watch?v=mr0MqOZEvaI
----------------------------------------------------------
Combinadores de parsers I

* Representação de um parser como função.
* Operações atômicas de leitura.
* Operações de segunda ordem: mapa, sequência e alternativa.
* Lendo objetos atômicos.

Vídeo: https://www.youtube.com/watch?v=mJnVTIU7Bdg
----------------------------------------------------------
Combinadores de parsers II

* Outras operações de segunda ordem. 
* Operações recursivas e estruturas de dados.
* Parser de JSON.
* Opcional: DSL com sobrecarga de operadores.

Vídeo: https://www.youtube.com/watch?v=0MGpJAqr3N0
----------------------------------------------------------
Gramáticas gerativas

* Linguagens naturais vs formais.
* Léxico, sintaxe e semântica.
* Símbolos terminais e não-terminais.
* Gramática e representação BNF.
* Enumeração de expressões da linguagem.
* Árvores sintáticas concretas e abstratas.
* Gerador de lero-lero.

Vídeo: **em elaboração**
----------------------------------------------------------
Gramáticas livres de contexto

* Regras de produção.
* Declarando regras da gramática utilizando o Lark.
* Operadores estendidos.
* Leitor de JSON.

Vídeo: https://www.youtube.com/watch?v=mr0MqOZEvaI
----------------------------------------------------------
Derivações

* Análise léxica e símbolos terminais.
* Derivações intuitivas.
* Estratégias Top-down vs bottom-up.
* Redução à esquerda ou à direita.
* Gramáticas ambíguas vs não-ambíguas.

Vídeo: **em elaboração**
----------------------------------------------------------
Operadores

* Operações matemáticas básicas.
* Ordem infixa, sufixa e prefixa.
* Precedência e associatividade de operadores.
* Árvore sintática e avaliação de expressões.
* Operadores como funções.

Vídeo: https://www.youtube.com/watch?v=OpRkhkqS6tg
----------------------------------------------------------
Interpretador simples 

* Operações lógicas e hierarquia de operadores.
* Chamada de funções.
* Variáveis e ambiente de execução.
* Execução condicional.
* Listas de expressões. 

Vídeo: https://www.youtube.com/watch?v=0G0axJCX-J4
----------------------------------------------------------
Estudo dirigido: Linguagem Twine (assíncrono)

* Definições da linguagem.
* Interpretação de funções.

Vídeo: **em elaboração**
----------------------------------------------------------
Avaliação

* Gramáticas livre de contexto e linguagens formais.
* Interpretadores.
* Etapas de análise sintática e compilação
----------------------------------------------------------
Expressões regulares

* Linguagens regulares vs gramáticas livres de contexto.
* Expressões regulares.
* Ortografia e léxico de uma linguagem.
* Utilizando expressões regulares no Lark.
* Estensões comuns para expressões regulares.

Vídeo: https://www.youtube.com/watch?v=qV8pvyWDo0I
----------------------------------------------------------
Linguagens regulares

* Ortografia e léxico de uma linguagem.
* Linguagens regulares.
* Expressões regulares.
* Operadores não-regulares comuns.

Vídeo: https://www.youtube.com/watch?v=5K7-lFdz_2s
----------------------------------------------------------
Laboratório de regex (síncrono)

* Detecção de padrões.
* Expressões regulares em ferramentas de código.
* Regex101 e teste de padrões.
* Palavras cruzadas.
----------------------------------------------------------
Análise léxica

* Tokens.
* Implementando um analizador léxico com regex.
* Analizador léxico no Lark.

Vídeo: https://www.youtube.com/watch?v=qfE9-723Lh0
----------------------------------------------------------
Estudo dirigido: Compilador de Twine (assíncrono)

* Usando expressões regulares no analizador léxico.
* Representação interna.
* Emissão de código C.

Vídeo: **em elaboração**
----------------------------------------------------------
Autômatos

* Introdução a autômatos.
* Símbolos, estados e regras de transição.
* Autômato determinístico finito (DFA).
* Implementação de um DFA.
* Autômato não-determinístico.

Vídeo: https://www.youtube.com/watch?v=xSufZUBt2iM
----------------------------------------------------------
Autômatos não-determinísticos

* Modelos de execução e representação de um NFA.
* Implementando um NFA.
* Regras epsilon.
* Construção de Thompson.
* Problemas com construções intuitivas para regex.

Vídeo: https://www.youtube.com/watch?v=P9wbMGj8hpA
----------------------------------------------------------
Simplificando NFAs

* Eliminação de transições epsilon.
* Propagação de estados iniciais e de aceite.
* Eliminação de estados desnecessários.
* Conversão de um NFA para um DFA.
* Tabela de conversão.
* Exercícios.

Vídeos: 
    * https://www.youtube.com/watch?v=hlGr8shsymw
    * https://www.youtube.com/watch?v=Ukm1kSgBBNg
----------------------------------------------------------
Descida recursiva e o LL(1)

* Tipos atômicos (numerais, strings, etc).
* Símbolos.
* Operadores e delimitadores.
* Descida como uma tabela de transição.
* Implementação da tabela de transição.

Vídeo: **em elaboração**
----------------------------------------------------------
Parser LL(1)

* Construções FIRST e FOLLOW.
* Construção da tabela de transição.
* Gramáticas sem epsilon.
* Gramaticas com epsilon.
* Conflitos na construção.

Vídeo: **em elaboração**
----------------------------------------------------------
Linguagens de programação

* História das linguagens de programação.
* Paradigmas de programação.
* Famílias de sintaxe.
* Ambiente de execução e semântica de uma linguagem.

Vídeo: **em elaboração**
----------------------------------------------------------
Entrega de trabalhos e exercícios
----------------------------------------------------------
Revisão de notas