% Example that does not work

person(alice).
person(bob).

modeh(epidemic).
modeb(flu(+person), [(max, 1)]).
modeb(cold, [(max, 1)]).

flu(alice).

pf(cold, 0.7).

example(epidemic, 0.7).
