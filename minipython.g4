grammar minipython;
prog: expr EOF;
expr:
	expr OP_1 expr
	| expr OP_2 expr
    | expr OP_3 expr
    | INT
	| '(' expr ')';

OP_1: '*' | '/' | '%'; // Multiplicative operators
OP_2: '+' | '-'; // Arithmetic operators
OP_3: '==' | '!=' | '<' | '<=' | '>' | '>='; // Comparison operators
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip; // Skip spaces, tabs and newlines