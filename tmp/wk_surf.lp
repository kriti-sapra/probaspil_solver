
day(1..40).











surf(A):-
	day(A),
	rule(r((idsuZDC,c,l)),1).
surf(A):-
	day(A),
	A=B,
	day(B),
	windok(B),
	rule(r((idsuZDC,c,l),(idwiSkC,c,l(1))),2).
surf(A):-
	day(A),
	A=B,
	day(B),
	sunshine(B),
	rule(r((idsuZDC,c,l),(idsuOwB,c,l(1))),2).
surf(A):-
	day(A),
	A=B,
	day(B),
	sunshine(B),
	A=C,
	day(C),
	windok(C),
	rule(r((idsuZDC,c,l),(idsuOwB,c,l(1)),(idwiSkC,c,l(1))),3).
surf(A):-
	day(A),
	A=B,
	day(B),
	not pop(B),
	rule(r((idsuZDC,c,l),(idnojnB,c,l(1))),2).
surf(A):-
	day(A),
	A=B,
	day(B),
	not pop(B),
	A=C,
	day(C),
	windok(C),
	rule(r((idsuZDC,c,l),(idnojnB,c,l(1)),(idwiSkC,c,l(1))),3).
surf(A):-
	day(A),
	A=B,
	day(B),
	not pop(B),
	A=C,
	day(C),
	sunshine(C),
	rule(r((idsuZDC,c,l),(idnojnB,c,l(1)),(idsuOwB,c,l(1))),3).
surf(A):-
	day(A),
	A=B,
	day(B),
	not pop(B),
	A=C,
	day(C),
	sunshine(C),
	A=D,
	day(D),
	windok(D),
	rule(r((idsuZDC,c,l),(idnojnB,c,l(1)),(idsuOwB,c,l(1)),(idwiSkC,c,l(1))),4).
