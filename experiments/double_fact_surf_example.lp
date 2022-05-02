modeh(surf(+time)).
modeb(sunshine(+time), [(max, 1)]).
modeb(windok(+time), [(max, 1)]).
windok(0).
pf(sunshine(0), 0.4).
pf(sunshine(1), 0.4).
example(surf(0), 0.4).
example(surf(1), 0).
%%%%%%%%%%%%%%%%%%%%%%
% Background Knowledge.
%%%%%%%%%%%%%%%%%%%%%%
time(0..1).
windok(0).

