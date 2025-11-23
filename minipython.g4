grammar minipython;

prog: block EOF;

block: (expr NEWLINE)* ;

expr:
    | ID '=' expr        // assignment as part of expr
    | expr OP_1 expr
    | expr OP_2 expr
    | expr OP_3 expr
    | atom
    | '(' expr ')';

atom: INT | ID;
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers start with letters or underscore


OP_1: '*' | '/' | '%'; // Multiplicative operators
OP_2: '+' | '-'; // Arithmetic operators
OP_3: '==' | '!=' | '<' | '<=' | '>' | '>='; // Comparison operators
NEWLINE: [\r\n]+;
INT: [0-9]+;
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines

// main branch

// expr:
// 	expr OP_1 expr
// 	| expr OP_2 expr
//     | expr OP_3 expr
//     | INT
// 	| '(' expr ')';