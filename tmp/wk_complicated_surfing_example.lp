var1(d1).



surf(A):-
	var1(A),
	rule(r((idsuQbB,c,l)),1).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	windok(B),
	rule(r((idsuQbB,c,l),(idwiXoB,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	sunshine(B),
	rule(r((idsuQbB,c,l),(idsuDb,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	sunshine(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuQbB,c,l),(idsuDb,c,l(1)),(idwiXoB,c,l(1))),3).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	rule(r((idsuQbB,c,l),(idnovUB,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuQbB,c,l),(idnovUB,c,l(1)),(idwiXoB,c,l(1))),3).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	A=C,
	var1(C),
	sunshine(C),
	rule(r((idsuQbB,c,l),(idnovUB,c,l(1)),(idsuDb,c,l(1))),3).
