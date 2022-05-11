var1(d1).


temp(mild).
temp(cold).


surf(A,B):-
	var1(A),
	temp(B),
	rule(r((idsu6XC,c(B),l)),1).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsu6XC,c(B),l),(idwi6e,c,l(1))),2).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	temp(D),
	sunshine(C,D),
	rule(r((idsu6XC,c(B),l),(idsujpB,c(D),l(1))),2).
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
	rule(r((idsu6XC,c(B),l),(idsujpB,c(D),l(1)),(idwi6e,c,l(1))),3).
