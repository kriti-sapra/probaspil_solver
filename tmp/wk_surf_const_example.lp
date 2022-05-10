var1(d1).


temp(mild).
temp(cold).


surf(A,B):-
	var1(A),
	temp(B),
	rule(r((idsuRl,c(B),l)),1).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuRl,c(B),l),(idwiQAB,c,l(1))),2).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	temp(D),
	sunshine(C,D),
	rule(r((idsuRl,c(B),l),(idsuaH,c(D),l(1))),2).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	temp(D),
	sunshine(C,D),
	A=E,
	var1(E),
	windok(E),
	rule(r((idsuRl,c(B),l),(idsuaH,c(D),l(1)),(idwiQAB,c,l(1))),3).
