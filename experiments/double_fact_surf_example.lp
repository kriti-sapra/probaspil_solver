modeh(surf(+time)).
modeb(sunshine(+time), [(max, 1)]).
modeb(windok(+time), [(max, 1)]).
windok(0).
time(0).
time(1).
pf(sunshine(0), 0.4).
pf(sunshine(1), 0.4).
example(surf(0), 0.4).
example(surf(1), 0).

