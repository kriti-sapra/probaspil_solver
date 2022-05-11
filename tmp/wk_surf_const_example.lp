var1(d1).


temp(mild).
temp(cold).


surf(A,B):-
	var1(A),
	temp(B),
	rule(r((idsutgB,c(B),l)),1).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsutgB,c(B),l),(idwiVjB,c,l(1))),2).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	temp(D),
	sunshine(C,D),
	rule(r((idsutgB,c(B),l),(idsuojB,c(D),l(1))),2).
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
	rule(r((idsutgB,c(B),l),(idsuojB,c(D),l(1)),(idwiVjB,c,l(1))),3).
