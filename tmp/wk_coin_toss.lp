coin(1).
heads(X):-coin(X),not tails(X).
tails(X):-coin(X),not heads(X).




heads(A):-
	coin(A),
	rule(r((idheKm,c,l)),1).
heads(A):-
	coin(A),
	A=B,
	coin(B),
	tossed(B),
	rule(r((idheKm,c,l),(idtoagB,c,l(1))),2).
tails(A):-
	coin(A),
	rule(r((idtahSC,c,l)),1).
tails(A):-
	coin(A),
	A=B,
	coin(B),
	tossed(B),
	rule(r((idtahSC,c,l),(idtoagB,c,l(1))),2).
