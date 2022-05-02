var1(d1).

pf(sunshine(d1), 0.6).
pf(windok(d1), 0.7).
pf(pop(d1), 0.2).

modeh(1, surf(+var1)).
modeb(1, sunshine(+var1)).
modeb(1, windok(+var1)).
modeb(1, not pop(+var1)).

example(surf(d1), 0.704).