smoke(A):-  person(A), influences(B,A), person(B), smoke(B).

time(0..1).
windok(0).

surf(A):-
	time(A),
	rule(r((idsuGUB,c,l)),1).
surf(A):-
	time(A),
	A=B,
	time(B),
	windok(B),
	rule(r((idsuGUB,c,l),(idwimK,c,l(1))),2).
surf(A):-
	time(A),
	A=B,
	time(B),
	sunshine(B),
	rule(r((idsuGUB,c,l),(idsuLV,c,l(1))),2).
surf(A):-
	time(A),
	A=B,
	time(B),
	sunshine(B),
	A=C,
	time(C),
	windok(C),
	rule(r((idsuGUB,c,l),(idsuLV,c,l(1)),(idwimK,c,l(1))),3).
