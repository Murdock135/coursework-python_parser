grammar minipython;

// ==============================================================================
// Parser rules (rules that define the structure of the language)
// ==============================================================================

tokens {INDENT, DEDENT}

prog: block EOF;

block: NEWLINE* (statement NEWLINE+ )* statement? NEWLINE* ; // catches multiple statements separated by newlines, allowing optional newlines at the start and end.

statement:
	| assignment
	| compound_assignment
	| if_stmt
	| expr
	;

assignment:
	ID '=' expr
	;

compound_assignment:
	ID COMPOUND_OP expr
	;

// *************************************************************************************************
// QUESTION FOR EKIN: Why can't we use 'if' expr ':' NEWLINE INDENT block DEDENT ... directly here?
// *************************************************************************************************
if_stmt:
	IF expr ':' NEWLINE INDENT block DEDENT
	(ELIF expr ':' NEWLINE INDENT block DEDENT)*
	(ELSE ':' NEWLINE INDENT block DEDENT)?
	;

expr:
	| expr OP_1 expr // multiplicative
	| expr OP_2 expr // additive
	| expr OP_3 expr // comparison
	| '(' expr ')' // parenthesized expr
	| '(' expr ',' expr (',' expr)* ')' // tuple (2+ elements)
	| '(' expr ',' ')' // single-element tuple
    | '[' expr (',' expr)* ']' // list
    | '{' expr ':' ( expr (',' expr ':' expr)* )? '}' // dict
	| atom;

atom: NUMBER | ID | STRING | BOOL;

// TODO:
// -----------------------------------------------------------------------------
// 1. if statements
// 2. for loops
// 3. while loops

// ==============================================================================
// Lexer rules (tokens)
// ==============================================================================

// These need to be defined before ID to avoid conflicts
IF: 'if';
ELIF: 'elif';
ELSE: 'else';

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
COMPOUND_OP: (OP_1 | OP_2) '='; // Compound assignment operators

COMMENT: '#' ~[\r\n]* -> skip; // Skip comments
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines