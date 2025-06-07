grammar GraphLang;

prog: defGraph EOF ;

defGraph: 'def' 'graph' '(' nodeList? ')' ;

nodeList: node (',' node)* ;

node: INT conn* ;

conn: '{' INT '}' weight? ;

weight: '[' INT ']' ;

WS: [ \t\r\n]+ -> skip ;

INT: [0-9]+ ;
