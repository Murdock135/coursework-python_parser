grammar minipython;

// ==============================================================================
// Parser rules (rules that define the structure of the language)
// ==============================================================================

tokens {INDENT, DEDENT}

prog: block EOF;

block: statement (NEWLINE+ statement)* NEWLINE*;

statement:
	assignment
	| compound_assignment
	| if_stmt
	| while_loop
	| for_loop
	| func_call
	| expr
	;

assignment: ID ASSIGN expr;

compound_assignment: ID COMPOUND_OP expr;

// ======================================================================================================
// CONTROL FLOW
// ======================================================================================================

// *************************************************************************************************
// QUESTION FOR EKIN: Why can't we use 'if' expr ':' NEWLINE INDENT block DEDENT ... directly here?
// *************************************************************************************************
if_stmt:
	IF expr COLON suite
	(NEWLINE* elif_clause)*
	(NEWLINE* else_clause)?
	;

elif_clause: ELIF expr COLON suite;

else_clause: ELSE COLON suite;

// ===============================================================================================
// LOOPS
// ===============================================================================================

while_loop: WHILE expr COLON suite;

for_loop: FOR ID IN (expr | func_call) COLON suite;

// ======================================================================================================
// FUNCTION CALLS
// ======================================================================================================

func_call: ID LPAREN (expr (COMMA expr)*)? RPAREN;

// ======================================================================================================
// SUITE
// ======================================================================================================

suite: NEWLINE INDENT block DEDENT;

// ======================================================================================================
// EXPRESSIONS
// ======================================================================================================

expr
	: expr OP_1 expr // multiplicative
	| expr OP_2 expr // additive
	| expr OP_3 expr // comparison
	| expr AND expr // logical AND
	| expr OR expr // logical OR
	| NOT expr // logical NOT
	| LPAREN expr RPAREN // parenthesized expr
	| LPAREN expr COMMA expr (COMMA expr)* RPAREN // tuple (2+ elements)
	| LPAREN expr COMMA RPAREN // single-element tuple
    | LBRACKET expr (COMMA expr)* RBRACKET // list
    | LBRACE expr COLON (expr (COMMA expr COLON expr)*)? RBRACE // dict
	| atom;

atom
	: NUMBER 
	| ID 
	| STRING 
	| BOOL;

// TODO:
// -----------------------------------------------------------------------------
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
WHILE: 'while';
FOR: 'for';
IN: 'in';

NUMBER: INT | FLOAT;
FLOAT: '-'? [0-9]+ '.' [0-9]+; // Floating point literals
INT: '-'? [0-9]+; // Integer literals
BOOL: 'True' | 'False'; // Boolean literals

// Triple-quoted comments defined before STRING to avoid conflicts
TRIPLE_QUOTE_COMMENT
    : ('"""' .*? '"""' | '\'\'\'' .*? '\'\'\'')
    -> skip
    ;	

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

// Single character tokens
ASSIGN: '=';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';

// *************************************************************************************************************************
// QUESTION FOR EKIN: Why can't we use this? Claude mentioned that we canot reference other token names in Lexer rules
// LOGICAL_OP: AND | OR | NOT; // Logical operators
// **************************************************************************************************************************

//----------------------------------------------------------------------------------------
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers start with letters or underscore
COMMENT: '#' ~[\r\n]* -> skip; // Skip comments
NEWLINE: '\r\n' | '\n' | '\r'; // Newline characters
WS: [ \t]+ -> skip; // Skip spaces, tabs and newlines