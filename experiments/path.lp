node(a).
node(b).
node(c).

path(X, X) :- node(X).

modeh(path(+node, +node)).
modeb(edge(+node, -node), [(max, 1)]).
modeb(path(+node, +node), [(max, 1)]).

pf(edge(a,b), 0.8).
pf(edge(b,c), 0.9).

example(path(a,c), 0.72).
example(path(b, a), 0).
example(path(c, a), 0).