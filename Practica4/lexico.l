D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include <stdio.h>

%}

%%

"auto"			{ printf("<Especificador de almacenamiento>"); }
"break"			{ printf("<Sentencia de control>"); }
"case"			{ printf("<Palabra reservada>"); }
"char"			{ printf("<Tipo de dato>"); }
"const"			{ printf("<Modificador>"); }
"continue"		{ printf("<Sentencia de control>"); }
"default"		{ printf("<Palabra reservada>"); }
"do"			{ printf("<Ciclo>"); }
"double"		{ printf("<Tipo de dato>"); }
"else"			{ printf("<Directiva>"); }
"enum"			{ printf("<Tipo de dato>"); }
"extern"		{ printf("<Especificador de almacenamiento>"); }
"float"			{ printf("<Tipo de dato>"); }
"for"			{ printf("<Ciclo>"); }
"goto"			{ printf("<Palabra reservada>"); }
"if"			{ printf("<Directiva>"); }
"int"			{ printf("<Tipo de dato>"); }
"long"			{ printf("<Tipo de dato>"); }
"register"		{ printf("<Especificador de almacenamiento>"); }
"return"		{ printf("<Palabra reservada>"); }
"short"			{ printf("<Tipo de dato>"); }
"signed"		{ printf("<Tipo de dato>"); }
"sizeof"		{ printf("<Operador>"); }
"static"		{ printf("<Modificador de almacenamiento>"); }
"struct"		{ printf("<Palabra reservada>"); }
"switch"		{ printf("<Sentencia de control>"); }
"typedef"		{ printf("<Palabra reservada>"); }
"union"			{ printf("<Palabra reservada>"); }
"unsigned"		{ printf("<Tipo de dato>"); }
"void"			{ printf("<Tipo de dato>"); }
"volatile"		{ printf("<Modificador de acceso>"); }
"while"			{ printf("<Ciclo>"); }

{L}({L}|{D})*		{ printf("<ID>"); }

0[xX]{H}+{IS}?		{ printf("<Constante Hexadecimal>"); }
0{D}+{IS}?		{ printf("<Constante Octal>"); }
{D}+{IS}?		{ printf("<Constante>"); }
L?'(\\.|[^\\'])+'	{ printf("<Cadena>"); }

{D}+{E}{FS}?		{ printf("<Constante>"); }
{D}*"."{D}+({E})?{FS}?	{ printf("<Contante Double>"); }
{D}+"."{D}*({E})?{FS}?	{ printf("<Constante Long Double>"); }

L?\"(\\.|[^\\"])*\"	{ printf("<Cadena>"); }

"..."			{ printf("<operador ternario>"); }
">>="			{ printf("<Operador a nivel de bit>"); }
"<<="			{ printf("<Operador a nivel de bit>"); }
"+="			{ printf("<Asignacion>"); }
"-="			{ printf("<Asignacion>"); }
"*="			{ printf("<Asignacion>"); }
"/="			{ printf("<Asignacion>"); }
"%="			{ printf("<Asignacion>"); }
"&="			{ printf("<Asignacion>"); }
"^="			{ printf("<Asignacion>"); }
"|="			{ printf("<Asignacion>"); }
">>"			{ printf("<Operador a nivel de bit>"); }
"<<"			{ printf("<Operador a nivel de bit>"); }
"++"			{ printf("<Pre Incremento>"); }
"--"			{ printf("<Pre Decremento>"); }
"->"			{ printf("<Miembro de puntero>"); }
"&&"			{ printf("<Operador de comparacion>"); }
"||"			{ printf("<Operador de comparacion>"); }
"<="			{ printf("<Operador de comparacion>"); }
">="			{ printf("<Operador de comparacion>"); }
"=="			{ printf("<Operador de comparacion>"); }
"!="			{ printf("<Operador de comparacion>"); }
";"			{ printf("<Punto y coma>"); }
("{"|"<%")		{ printf("<Llave de apertura>"); }
("}"|"%>")		{ printf("<Llave de termino>"); }
","			{ printf("<Separador>"); }
":"			{ printf("<Operador ternario>"); }
"="			{ printf("<Asignacion>"); }
"("			{ printf("<Parentesis de apertura>"); }
")"			{ printf("<Parentesis de termino>"); }
("["|"<:")		{ printf("<Corchete de apertura>"); }
("]"|":>")		{ printf("<Corchete de termino>"); }
"."			{ printf("<Miembro>"); }
"&"			{ printf("<Operador bit a bit>"); }
"!"			{ printf("<Operador Not>"); }
"~"			{ printf("<Operador bit a bit>"); }
"-"			{ printf("<Operador aritmetico>"); }
"+"			{ printf("<Operador aritmetico>"); }
"*"			{ printf("<Operador aritmetico>"); }
"/"			{ printf("<Operador aritmetico>"); }
"%"			{ printf("<Operador aritmetico>"); }
"<"			{ printf("<Operador de comparacion>"); }
">"			{ printf("<Operador de comparacion>"); }
"^"			{ printf("<Operador bit a bit>"); }
"|"			{ printf("<>Operador bit a bit"); }
"?"			{printf("<Operador ternario>"); }

[\t\v\n\f]		{printf("<Salto de linea>\n");}
.			{ /* ignore bad characters */ }

%%
