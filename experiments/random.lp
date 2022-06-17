windok(d1).
day(d1).

rain(X) :- day(X), not sunshine(X).
sunshine(X) :- day(X), warm(X), not rain(X).
