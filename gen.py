#!/usr/bin/env python3
import re
import sys

# forgive me for this
table = [
	('(Início)(?=(?:[^"]|"[^"]*")*$)','int\nmain() {'),
	('(Fim.)(?=(?:[^"]|"[^"]*")*$)','}'),
	('(início)(?=(?:[^"]|"[^"]*")*$)','{'),
	('(fim;)(?=(?:[^"]|"[^"]*")*$)','}'),
	('(se)(?=(?:[^"]|"[^"]*")*$)(.*)( então)','if\g<2> {'),
	('(fimse;)(?=(?:[^"]|"[^"]*")*$)','}'),
	('(senão se)(?=(?:[^"]|"[^"]*")*$)(.*)','} else if\g<2> {'),
	('(senão)(?=(?:[^"]|"[^"]*")*$)','} else {'),
	('(enquanto)(?=(?:[^"]|"[^"]*")*$)(.*)( faça)','while\g<2> {'),
	('(fimenquanto;)(?=(?:[^"]|"[^"]*")*$)','}'),
	('(=)(?=(?:[^"]|"[^"]*")*$)','=='),
	('(<-)(?=(?:[^"]|"[^"]*")*$)','='),
	('(caractere:)(?=(?:[^"]|"[^"]*")*$)(.*)(==)(.*)','std::string\g<2>=\g<4>?'),
	('(inteiro:)(?=(?:[^"]|"[^"]*")*$)(.*)(==)(.*)','int\g<2>=\g<4>'),
	('(real:)(?=(?:[^"]|"[^"]*")*$)(.*)(==)(.*)','double\g<2>=\g<4>'),
	('(lógico:)(?=(?:[^"]|"[^"]*")*$)(.*)(==)(.*)','bool\g<2>=\g<4>'),
	('(caractere:)(?=(?:[^"]|"[^"]*")*$)(.*)','std::string\g<2>'),
	('(inteiro:)(?=(?:[^"]|"[^"]*")*$)(.*)','int\g<2>'),
	('(real:)(?=(?:[^"]|"[^"]*")*$)(.*)','double\g<2>'),
	('(lógico:)(?=(?:[^"]|"[^"]*")*$)(.*)','bool\g<2>'),
	('(constante)(?=(?:[^"]|"[^"]*")*$)','const'),
	('(verdadeiro)(?=(?:[^"]|"[^"]*")*$)(.*)','true;'),
	('(falso)(?=(?:[^"]|"[^"]*")*$)(.*)','false;'),
	('( E )(?=(?:[^"]|"[^"]*")*$)',' && '),
	('( OU )(?=(?:[^"]|"[^"]*")*$)',' || '),
	('(NÃO\()(?=(?:[^"]|"[^"]*")*$)(.*)(\))',' !(\g<2>) '),
	('(escreva\()(?=(?:[^"]|"[^"]*")*$)(.*)(\))','std::cout << \g<2>'),
	('(leia\()(?=(?:[^"]|"[^"]*")*$)(.*)(\))','std::cin >> \g<2>'),
]

def gen(source):
	trans = source
	for rd, c in table:
		trans = re.sub(rd, c, trans)

	lines = trans.split('\n')
	for i in range(0, len(lines)):
		if 'std::cout' in lines[i]:
			lines[i] = lines[i].replace(',', ' <<')
		if 'std::cin' in lines[i]:
			lines[i] = lines[i].replace(',', ' >>')

	trans = "#include <iostream>\n\n" + '\n'.join(lines)
	return trans

if __name__ == "__main__":
	src = str()
	for l in sys.stdin:
		src+=l
	print(gen(src))
