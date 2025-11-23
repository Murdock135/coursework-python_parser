grammar minipython;
prog: expr EOF;
expr:
	expr ('*' | '/') expr
	| expr ('+' | '-') expr
	| expr ('==' | '!=' | '<' | '<=' | '>' | '>=') expr
	| INT
	| '(' expr ')';

INT: [0-9]+;
NEWLINE: [\r\n]+ -> skip; // Skip newlines 
WS: [\t]+ -> skip; // Skip whitespace