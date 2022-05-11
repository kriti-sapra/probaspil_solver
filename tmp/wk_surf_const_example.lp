var1(d1).


temp(mild).
temp(cold).


surf(A,B):-
	var1(A),
	temp(B),
	rule(r((idsuBGC,c(B),l)),1).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuBGC,c(B),l),(idwibvB,c,l(1))),2).
surf(A,B):-
	var1(A),
	temp(B),
	A=C,
	var1(C),
	temp(D),
	sunshine(C,D),
	rule(r((idsuBGC,c(B),l),(idsu0sB,c(D),l(1))),2).
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
	rule(r((idsuBGC,c(B),l),(idsu0sB,c(D),l(1)),(idwibvB,c,l(1))),3).
