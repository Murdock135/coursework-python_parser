grammar minipython;

tokens { INDENT, DEDENT }

// ==========================
// PROGRAM
// ==========================

prog: block EOF ;

block:
    statement (NEWLINE+ statement)* NEWLINE*
    ;

// ==========================
// STATEMENTS
// ==========================

statement:
      assignment
    | compound_assignment
    | if_stmt
    | while_loop
    | for_loop
    | func_call
    | expr
    ;

// ==========================
// ASSIGNMENT STATEMENTS
// ==========================

assignment:
    ID ASSIGN expr
    ;

compound_assignment:
    ID COMPOUND_OP expr
    ;

// ==========================
// CONTROL FLOW
// ==========================

if_stmt:
      IF expr COLON suite
      (NEWLINE* elif_clause)*
      (NEWLINE* else_clause)?
    ;

elif_clause:
      ELIF expr COLON suite
    ;

else_clause:
      ELSE COLON suite
    ;

// ==========================
// LOOPS
// ==========================

while_loop:
    WHILE expr COLON suite
    ;

for_loop:
    FOR ID IN (expr | func_call) COLON suite
    ;

// ==========================
// FUNCTION CALL
// ==========================

func_call:
    ID LPAREN (expr (COMMA expr)*)? RPAREN
    ;

// ==========================
// SUITES (INDENTED BLOCKS)
// ==========================

suite:
    NEWLINE INDENT block DEDENT
    ;

// ==========================
// EXPRESSIONS
// ==========================

// Precedence (highest at bottom):
// expr → or → and → comparison → additive → multiplicative → unary → primary

expr:
    logical_or_expr
    ;

logical_or_expr:
      logical_and_expr
    | logical_or_expr OR logical_and_expr
    ;

logical_and_expr:
      comparison_expr
    | logical_and_expr AND comparison_expr
    ;

comparison_expr:
      additive_expr
    | comparison_expr OP_3 additive_expr
    ;

additive_expr:
      multiplicative_expr
    | additive_expr OP_2 multiplicative_expr
    ;

multiplicative_expr:
      unary_expr
    | multiplicative_expr OP_1 unary_expr
    ;

unary_expr:
      NOT unary_expr
    | primary
    | LPAREN expr RPAREN     // <-- FIXED: allow parentheses here!
    ;

// ==========================
// PRIMARY EXPRESSIONS
// ==========================

primary:
      atom
    | func_call
    | tuple_literal
    | list_literal
    | dict_literal
    ;

// ==========================
// LITERALS
// ==========================

// Correct ordering to avoid ambiguity:
// Parenthesized expr is in unary_expr—not here.

tuple_literal:
      LPAREN expr COMMA RPAREN                    // single element
    | LPAREN expr COMMA expr (COMMA expr)* RPAREN // multi-element
    ;

list_literal:
    LBRACKET (expr (COMMA expr)*)? RBRACKET
    ;

dict_literal:
    LBRACE (expr COLON expr (COMMA expr COLON expr)*)? RBRACE
    ;

atom:
      NUMBER
    | ID
    | STRING
    | BOOL
    ;

// ==========================
// LEXER RULES
// ==========================

// RESERVED WORDS
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
AND: 'and';
OR: 'or';
NOT: 'not';
WHILE: 'while';
FOR: 'for';
IN: 'in';

// LITERALS
NUMBER: INT | FLOAT;

FLOAT: '-'? [0-9]+ '.' [0-9]+ ;
INT:   '-'? [0-9]+ ;
BOOL:  'True' | 'False' ;

// STRINGS
TRIPLE_QUOTE_COMMENT
    : ('"""' .*? '"""' | '\'\'\'' .*? '\'\'\'') -> skip
    ;

STRING:
      '"'  ('\\' . | ~["\\\r\n])* '"'
    | '\'' ('\\' . | ~['\\\r\n])* '\''
    ;

// OPERATORS
OP_1: '*' | '/' | '%';
OP_2: '+' | '-';
OP_3:
      '=='
    | '!='
    | '<'
    | '<='
    | '>'
    | '>='
    ;

COMPOUND_OP: (OP_1 | OP_2) '=';

// SYMBOLS
ASSIGN: '=';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';

// IDENTIFIERS
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// WHITESPACE / NEWLINE
COMMENT: '#' ~[\r\n]* -> skip ;
NEWLINE: '\r\n' | '\n' | '\r' ;
WS: [ \t]+ -> skip ;
