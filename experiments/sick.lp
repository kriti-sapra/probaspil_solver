day(1).
run(X) :- day(X), not walk(X), sunshine(X).
walk(X) :- day(X), not run(X).

sick(A):-  day(A), run(A), tired(A).
sick(A):-  day(A), not warm(A), walk(A).
warm(1).
tired(1).
wind(1).
sunshine(1).
