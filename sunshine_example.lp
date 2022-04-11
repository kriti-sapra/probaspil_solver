modeh(surf(+time), [name(hu)]).
modeb(sunshine(+time), [(max, 1)]).
modeb(windok(+time), [(max, 1)]).

pf(sunshine(0), 0.4).
example(surf(0), 0.4).
%%%%%%%%%%%%%%%%%%%%%%
% Background Knowledge.
%%%%%%%%%%%%%%%%%%%%%%
time(0..1).
windok(0).

%%%%%%%%%%%%%%%%%%%%%
%examples
%%%%%%%%%%%%%%%%%%%%%
goal(examples).

examples :-
surf(0), not surf(1).