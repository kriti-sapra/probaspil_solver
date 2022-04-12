coin(1).
heads(X) :- coin(X), not tails(X).
tails(X) :- coin(X), not heads(X).

pf(tossed(1), 1).

modeh(1, heads(+coin)).
modeh(1, tails(+coin)).
modeb(1, tossed(+coin)).


example(heads(1), 0.5).
example(tails(1), 0.5).