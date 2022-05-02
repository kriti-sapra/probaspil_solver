var1(d1).

pf(sunshine(d1, mild), 0.6).
pf(windok(d1), 0.7).

temp(mild).
temp(cold).

modeh(1, surf(+var1, #temp)).
modeb(1, sunshine(+var1, #temp), [(max, 1)]).
modeb(1, windok(+var1)).

example(surf(d1, mild), 0.42).