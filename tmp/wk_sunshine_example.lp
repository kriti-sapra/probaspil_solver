
time(0..1).
windok(0).

goal(examples).

examples:-
surf(0),not surf(1).
surf(A):-
	time(A),
	rule(r((idsuwBC,c,l)),1).
surf(A):-
	time(A),
	A=B,
	time(B),
	windok(B),
	rule(r((idsuwBC,c,l),(idwi4fC,c,l(1))),2).
surf(A):-
	time(A),
	A=B,
	time(B),
	sunshine(B),
	rule(r((idsuwBC,c,l),(idsukC,c,l(1))),2).
surf(A):-
	time(A),
	A=B,
	time(B),
	sunshine(B),
	A=C,
	time(C),
	windok(C),
	rule(r((idsuwBC,c,l),(idsukC,c,l(1)),(idwi4fC,c,l(1))),3).
