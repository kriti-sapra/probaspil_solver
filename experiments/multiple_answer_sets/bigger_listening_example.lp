day(0).
sun(0).
day(1).
sun(1).

pf(rain(0), 0.4).
pf(wind(0), 0.8).

pf(rain(1), 0.2).
pf(wind(1), 0.4).

pf(rain(2), 0.8).
pf(wind(2), 0.2).

run(X) :- sun(X), not wind(X), not walk(X).
walk(X) :- sun(X), not rain(X), not run(X).

music(rock).
music(classical).

modeh(listen(+day, #music)).
modeb(walk(+day), [(max, 1)]).
modeb(not listen(+day, #music), [(max, 1)]).

example(listen(0, classical), 0.28).
example(listen(0, rock), 0.28).

example(listen(1, classical), 0.32).
example(listen(1, rock), 0.32).

example(listen(2, classical), 0.073).
example(listen(2, rock), 0.073).


% listen (rock) :− walk , not listen ( classical ). listen ( classical ) :− walk , not listen (rock ).