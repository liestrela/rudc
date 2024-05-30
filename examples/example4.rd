Início
	inteiro: n1, n2, n3;

	leia(n1, n2, n3);

	se (n1>n2) então
		n1<-n1+n2;
		n2<-n1-n2;
		n1<-n1-n2;
	fimse;

	se (n2>n3) então
		n2<-n2+n3;
		n3<-n2-n3;
		n2<-n2-n3;
		se (n1>n2) então
			n1<-n1+n2;
			n2<-n1-n2;
			n1<-n1-n2;
		fimse;
	fimse;

	escreva(n1, " ", n2, " ", n3, "\n");
Fim.
