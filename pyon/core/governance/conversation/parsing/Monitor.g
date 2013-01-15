grammar Monitor;

options {
<<<<<<< HEAD
        language= Python;
=======
        language=Java;
>>>>>>> 0be4e402ab4ffeca4dc58485921ec74f571dec7a
	output=AST;
	backtrack=true;
}

tokens {
//==================Used for AST ===================
	INTERACTION = 'interaction';
	INT = 'int';
	STRING = 'string';
	PLUS 	= '+' ;	
	MINUS	= '-' ;
	MULT	= '*' ;
	DIV	= '/' ;
	FULLSTOP = '.' ;
	RESV = 'RESV';
	SEND = 'SEND';
	TYPE = 'TYPE';
	VALUE = 'VALUE';
	BRANCH = 'BRANCH';
	UNORDERED = 'UNORDERED';
	RECLABEL = 'RECLABEL';
	PARALLEL = 'PARALLEL';
	PROTOCOL = 'PROTOCOL';
	ASSERT = 'ASSERT';
	INT = 'int';
	STRING = 'string';
	GLOBAL_ESCAPE = 'GLOBAL_ESCAPE';
	EMPTY = 'EMPTY';
	ROLES = 'ROLES';
	INTR = 'INTR';
	DO = 'DO';
	PARAMETERLIST ='PARAMS';
	ABSTRACT = 'ABSTRACT';
	FULLNAME = 'FULLNAME';
	
//==================================================
//=======KEYWORDS===================================
	PACKAGEKW = 'package';
	IMPORTKW = 'import';
	TYPEKW = 'type';
	PROTOCOLKW = 'protocol';
	GLOBALKW = 'global';
	LOCALKW = 'local';
	ROLEKW = 'role';
	SIGKW = 'sig';
	INSTANTIATESKW = 'instantiates';

	FROMKW = 'from';
	TOKW = 'to';
	CHOICEKW = 'choice';
	ATKW = 'at';
	ORKW = 'or';
	RECKW = 'rec';
	CONTINUEKW = 'continue';
	PARALLELKW = 'par';  // FIXME: should be PARKW
	ANDKW = 'and';
	INTERRUPTIBLEKW = 'interruptible';
	WITHKW = 'with';
	BYKW = 'by';  // from for interrupts is more expected, but from is not good for multiple roles (generally, the comma in interrupt message list and role list looks like "and" rather than "or")
	DOKW = 'do';
	ASKW = 'as';
	SPAWNKW = 'spawn';
	THROWSKW = 'throws';
	CATCHESKW = 'catches';
	SIGKW = 'sig';
}

/*------------------------------------------------------------------
 * PARSER RULES
*------------------------------------------------------------------*/


// Not processed for now only recognised
module: packagedecl (importdecl)* (payloadtypedecl)* (protocolDef)*;
packagedecl: PACKAGEKW packagename ';';

packagename: ID ('.' ID)*;

importdecl: IMPORTKW ID ('.' ID)* ';'	
	   | FROMKW packagename '.' ID IMPORTKW ID ';'	
	   | FROMKW packagename '.' ID IMPORTKW ID ASKW ID ';';

// FIXME: payload types, not message types
payloadtypedecl:  TYPEKW '<' ID '>' EXTID FROMKW EXTID ASKW ID ';';

description: ( ( packagedecl | importdecl | module ) )* protocolDef -> protocolDef;

parameterList: '<' SIGKW ID (',' SIGKW ID)* '>' -> ^(PARAMETERLIST (ID)+);

protocolDef: 'local' 'protocol' protocolName ( 'at' roleName )  ( parameterList )? roleList '{' ( protocolBlockDef ) '}'
	     -> ^(PROTOCOL roleName parameterList* roleList+ protocolBlockDef*);

roleList: '(' roleparameDef ( ',' roleparameDef )* ')' -> ^(ROLES roleparameDef+);
protocolName: ID;
roleparameDef: 'role' ID -> ID;

protocolBlockDef: activityListDef -> activityListDef;	

blockDef: '{' activityListDef '}' -> ^(BRANCH activityListDef);
	 	  
assertDef : (ASSERTION)? -> ^(ASSERT ASSERTION?);

activityListDef: ( activityDef )* -> activityDef*;

primitivetype :(INT -> INT
               |STRING-> STRING);

activityDef: ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | doDef ) ';'! | 
			choiceDef | directedChoiceDef | parallelDef | repeatDef | unorderedDef |
			recBlockDef | globalEscapeDef;

introducesDef: roleDef 'introduces' roleDef ( ',' roleDef )* ;

roleDef: ID -> ID;

roleName: ID -> ID;

typeReferenceDef: ID ->ID ;

interactionSignatureDef: ((typeReferenceDef -> ^(ABSTRACT typeReferenceDef))
			 | (typeReferenceDef '(' (valueDecl (',' valueDecl)* )? ')' -> typeReferenceDef ^(VALUE valueDecl*))
			 | (('(' valueDecl (',' valueDecl)* ')') -> ^(VALUE valueDecl*)));

valueDecl : ID (':'! primitivetype)?;	 
firstValueDecl	: valueDecl;

// TODO: add the to roleNames
interactionDef: 
	     interactionSignatureDef (
		'from' role= roleName  (assertDef)-> ^(RESV interactionSignatureDef $role assertDef)
	      | 'to' roleName  (assertDef) -> ^(SEND interactionSignatureDef roleName assertDef));

choiceDef: 'choice' 'at' roleName blockDef ( 'or' blockDef )* -> ^('choice' blockDef+);

directedChoiceDef: ( 'from' roleName )? ( 'to' roleName ( ','! roleName )* )? '{' ( onMessageDef )+ '}';

onMessageDef: interactionSignatureDef ':' activityList ; 

activityList: ( activityDef )*;

repeatDef: 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef  -> ^('repeat' blockDef);

recBlockDef: 'rec' labelName blockDef -> ^('rec' labelName blockDef);

labelName: ID -> ID ;

recursionDef: 'continue' labelName -> ^(RECLABEL labelName);

// TODO: check end
endDef: 'end'^ ;

// TODO: run
runDef: 'run'^ protocolRefDef ( '('! parameter ( ','! parameter )* ')'! )? 'from' roleName ;

protocolRefDef: ID ( 'at' roleName )? ;

declarationName: ID ;

parameter: declarationName ;

// TODO: inline
inlineDef: 'inline'^ protocolRefDef ( '('! parameter ( ','! parameter )* ')'! )? ;

parallelDef: 'par' blockDef ( 'and' blockDef )* -> ^(PARALLEL blockDef+);

globalEscapeDef: 'interruptible' blockDef interruptDef -> ^(INTR blockDef interruptDef);

//interruptDef: ^ blockDef;
interruptDef : 'with' (
		     'throw' interactionSignatureDef (',' interactionSignatureDef)* 'by' roleName (',' roleName)*  ';'-> ^('throw' interactionSignatureDef+ ^('by' roleName+))
                     |'catch' interactionSignatureDef (',' interactionSignatureDef)* 'by' roleName (',' roleName)*  ';'-> ^('catch' interactionSignatureDef+ ^('by' roleName+)));

unorderedDef: 'unordered' '{' ( activityDef )* '}' -> ^(PARALLEL ^(BRANCH activityDef)+);

aliasDef: roleName 'as' ID -> ^('as' roleName ID) ;	 


doDef: 'do' EXTID ('<' interactionSignatureDef (',' interactionSignatureDef)* '>')? '(' aliasDef (',' aliasDef)* ')' -> ^(DO EXTID ^(PARAMETERLIST interactionSignatureDef*) ^(ROLES aliasDef+));	 

	 

/*-----------------------------------------------
TO DO:
Declaration (variables) possibly - but that may need
lookahead to avoid conflict with interactions.
-------------------------------------------------*/

expr	: term ( ( PLUS | MINUS )  term )* ;

term	: factor ( ( MULT | DIV ) factor )* ;

factor	: NUMBER ;


/*------------------------------------------------------------------
 * LEXER RULES
 *------------------------------------------------------------------*/
	 

NUMBER	: (DIGIT)+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ 	{ $channel = HIDDEN; } ;


ASSERTION : '@{' (options {greedy=false;} : .)* '}' ;


ML_COMMENT
    :   '/*' (options {greedy=false;} : .)* '*/' {$channel=HIDDEN;}
    ;

LINE_COMMENT : '//' (options {greedy=false;} : .)* '\n' {$channel=HIDDEN;} ;

StringLiteral: '"' ( ~('\\'|'"') )* '"' ;


ID:
	(LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*
;

/*MESSAGEOPERATOR:  // rule "subsumed" by identifier, lexer doesn't like it (also because it is a potentially empty token)
	(LETTER | DIGIT | UNDERSCORE)*
;*/

EXTID:
	'\"' (LETTER | UNDERSCORE) (LETTER | DIGIT | SYMBOL)* '\"'
;

fragment SYMBOL:
	'{' | '}' | '(' | ')' | '[' | ']' | ':' | '/' | '\\' | '.' | '\#' | '&' | '?' | '!'	| UNDERSCORE
;

fragment LETTER:
	'a'..'z' | 'A'..'Z'
;

fragment DIGIT:
	'0'..'9'
;

fragment UNDERSCORE:
	'_'
;

