Início
	real: a;
	real: b;
	real: c;

	leia(a, b, c);

	se ((a+b)>c E (a+c)>b E (b+c)>a ) então
		se ((a=b) E (b=c)) então
			escreva("equilátero\n");
		senão 
			se ((a=b) OU (b=c) OU (a=c)) então
				escreva("isósceles\n");
			senão
				escreva("escaleno\n");
			fimse;
		fimse;
	senão
		escreva("não é triângulo\n");
	fimse;
Fim.
