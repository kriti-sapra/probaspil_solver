
person(ann).
person(bob).
person(carl).

modeh(smoke(+person)).
modeb(stress(+person), [(max, 1)]).
modeb(influences(-person, +person), [(max, 1)]).
modeb(smoke(+person), [(max, 1)]).

pf(stress(ann), 0.8).
pf(influences(ann, bob), 0.6).
pf(influences(bob, carl), 0.2).

example(smoke(ann), 0.8, 0.8).
example(smoke(bob), 0.48, 0.48).
example(smoke(carl), 0.096, 0.096).