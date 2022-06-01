day(0).
sun(0).

pf(rain(0), 0.4).
pf(wind(0), 0.8).

run(X) :- sun(X), not wind(X), not walk(X).
walk(X) :- sun(X), not rain(X), not run(X).

music(rock).
music(classical).

modeh(listen(+day, #music)).
modeb(walk(+day), [(max, 1)]).
%modeb(wind(+day), [(max, 1)]).
%modeb(rain(+day), [(max, 1)]).
modeb(not listen(+day, #music), [(max, 1)]).
modeb(run(+day), [(max, 1)]).

example(listen(0, classical), 0.28).
example(listen(0, rock), 0.28).

% listen (rock) :− walk , not listen ( classical ). listen ( classical ) :− walk , not listen (rock ).
