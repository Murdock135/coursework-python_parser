grammar minipython;

// ==============================================================================
// Parser rules (rules that define the structure of the language)
// ==============================================================================

tokens {INDENT, DEDENT}

prog: block EOF;

block: (statement NEWLINE+)* statement?;

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
	| expr AND expr // logical AND
	| expr OR expr // logical OR
	| NOT expr // logical NOT
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

// -------------------------------------------------------------------------------------
// The following are defined BEFORE ID
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
AND: 'and';
OR: 'or';
NOT: 'not';

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

// *************************************************************************************************************************
// QUESTION FOR EKIN: Why can't we use this? Claude mentioned that we canot reference other token names in Lexer rules
// LOGICAL_OP: AND | OR | NOT; // Logical operators
// **************************************************************************************************************************

//----------------------------------------------------------------------------------------
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers start with letters or underscore
COMMENT: '#' ~[\r\n]* -> skip; // Skip comments
NEWLINE: '\r\n' | '\n' | '\r'; // Newline characters
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines