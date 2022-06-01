day(d1).
% Probabilistic Facts (PF)
pf(sunshine(d1), 0.4).

% Mode Bias (M)
modeh(1, surf(+day)).
modeb(1, sunshine(+day), [(max, 1)]).

example(surf(d1), 0.4).