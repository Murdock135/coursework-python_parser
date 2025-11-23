grammar minipython;

prog: block EOF;

block: (expr NEWLINE)*;

expr:
	| ID '=' expr // assignment as part of expr
	| expr OP_1 expr
	| expr OP_2 expr
	| expr OP_3 expr
	| '(' expr ')' // parenthesized expr
	| '(' expr ',' expr (',' expr)* ')' // tuple (2+ elements)
	| '(' expr ',' ')' // single-element tuple
    | '[' expr (',' expr)* ']' // list
    | '{' expr ':' ( expr (',' expr ':' expr)* )? '}' // dict
	| atom;

atom: NUMBER | ID | STRING;

NUMBER: INT | FLOAT;
FLOAT: '-'? [0-9]+ '.' [0-9]+; // Floating point literals
INT: '-'? [0-9]+; // Integer literals
STRING:
	'"' ('\\' . | ~["\\\r\n])* '"'
	| '\'' ( '\\' . | ~['\\\r\n])* '\'';
ID:
	[a-zA-Z_][a-zA-Z0-9_]*; // Identifiers start with letters or underscore

// Operators
OP_1: '*' | '/' | '%'; // Multiplicative operators
OP_2: '+' | '-'; // Arithmetic operators
OP_3:
	'=='
	| '!='
	| '<'
	| '<='
	| '>'
	| '>='; // Comparison operators

NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines