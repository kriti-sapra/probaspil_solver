var1(d1).



surf(A):-
	var1(A),
	rule(r((idsuYm,c,l)),1).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	windok(B),
	rule(r((idsuYm,c,l),(idwiTP,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	sunshine(B),
	rule(r((idsuYm,c,l),(idsuqOB,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	sunshine(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuYm,c,l),(idsuqOB,c,l(1)),(idwiTP,c,l(1))),3).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	rule(r((idsuYm,c,l),(idnogpB,c,l(1))),2).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	A=C,
	var1(C),
	windok(C),
	rule(r((idsuYm,c,l),(idnogpB,c,l(1)),(idwiTP,c,l(1))),3).
surf(A):-
	var1(A),
	A=B,
	var1(B),
	not pop(B),
	A=C,
	var1(C),
	sunshine(C),
	rule(r((idsuYm,c,l),(idnogpB,c,l(1)),(idsuqOB,c,l(1))),3).
