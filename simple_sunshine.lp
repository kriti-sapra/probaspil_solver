day(0).
sun(0).


run(X) :- sun(X), not wind(X), not walk(X).
walk(X) :- sun(X), not rain(X), not run(X).


music(rock).
music(classical).


listen(X, rock) :- day(X), walk(X), not listen(X, classical).
listen(X, classical) :- day(X), walk(X), not listen(X, rock).