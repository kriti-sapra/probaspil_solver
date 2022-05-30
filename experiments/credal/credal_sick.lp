pf(sunshine(1), 0.4).
pf(warm(1), 0.8).
pf(tired(1), 0.3).
pf(wind(1), 0.2).

day(1).

run(X) :- day(X), not walk(X), sunshine(X), not wind(X).
walk(X) :- day(X), not run(X).

modeh(sick(+day)).
modeb(run(+day), [(max, 1)]).
modeb(tired(+day), [(max, 1)]).
modeb(walk(+day), [(max, 1)]).
modeb(not warm(+day), [(max, 1)]).

example(sick(1), 0.15, 0.27).
