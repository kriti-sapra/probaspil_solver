node(a).
node(b).
node(c).
node(d).
node(e).

path(X,X) :- node(X).

modeh(path(+node, +node)).
modeb(edge(+node, -node), [(max, 1)]).
modeb(path(+node, +node), [(max, 1)]).

pf(edge(a,b), 0.2).
pf(edge(b,e), 0.5).
pf(edge(a,c), 0.3).
pf(edge(c,d), 0.4).
pf(edge(d,e), 0.4).

example(path(a,e), 0.22888).