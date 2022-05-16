person(ann).
person(bob).
person(carl).

modeh(smoke(+person)).
modeb(stress(+person), [(max, 2)]).
modeb(influences(-person, +person), [(max, 2)]).
modeb(smoke(+person), [(max, 2)]).

pf(stress(ann), 0.8).
pf(influences(ann, bob), 0.6).
pf(influences(bob, carl), 0.2).

example(smoke(ann), 0.8).
example(smoke(bob), 0.48).
example(smoke(carl), 0.096).