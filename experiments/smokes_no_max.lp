person(ann).
person(bob).
person(carl).

modeh(smoke(+person)).
modeb(stress(+person)).
modeb(influences(-person, +person)).
modeb(smoke(+person)).

pf(stress(ann), 0.8).
pf(influences(ann, bob), 0.6).
pf(influences(bob, carl), 0.2).

example(smoke(ann), 0.8).
example(smoke(bob), 0.48).
example(smoke(carl), 0.096).