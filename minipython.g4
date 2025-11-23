grammar minipython;

// ==============================================================================
// Parser rules (rules that define the structure of the language)
// ==============================================================================

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

atom: NUMBER | ID | STRING | BOOL;

// TODO:
// -----------------------------------------------------------------------------
// 1. Conditionals
// 2. Loops
// 3. Function definitions and calls

// ==============================================================================
// Lexer rules (tokens)
// ==============================================================================

ID:
	[a-zA-Z_][a-zA-Z0-9_]*; // Identifiers start with letters or underscore
NUMBER: INT | FLOAT;
FLOAT: '-'? [0-9]+ '.' [0-9]+; // Floating point literals
INT: '-'? [0-9]+; // Integer literals
BOOL: 'True' | 'False'; // Boolean literals
STRING:
	'"' ('\\' . | ~["\\\r\n])* '"' // Double-quoted strings: Backslash escapes followed by any character OR any character except backslash, double-quote, carriage return, or newline
	| '\'' ( '\\' . | ~['\\\r\n])* '\''; // Single-quoted strings: Backslash escapes followed by any character OR any character except backslash, single-quote, carriage return, or newline

// Operators
OP_1: '*' | '/' | '%'; // Multiplicative operators
OP_2: '+' | '-'; // Additive operators
OP_3:
	'=='
	| '!='
	| '<'
	| '<='
	| '>'
	| '>='; // Comparison operators

COMMENT: '#' ~[\r\n]* -> skip; // Skip comments
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines