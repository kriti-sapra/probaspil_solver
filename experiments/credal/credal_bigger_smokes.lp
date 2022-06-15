modeh(smoke(+person)).
modeb(stress(+person), [(max, 1)]).
modeb(influences(-person, +person), [(max, 1)]).
modeb(smoke(+person), [(max, 1)]).
modeb(friend(+person, -person), [(max, 1)]).

%smokes(X) :- stress(X).
%smokes(X) :- friend(X,Y), influences(Y,X), smokes(Y).

person(1).
person(2).
person(3).
person(4).

pf(stress(1), 0.3).
pf(stress(2), 0.3).
pf(stress(3), 0.3).
pf(stress(4), 0.3).

pf(influences(2, 1), 0.2).
pf(influences(1, 2), 0.2).
pf(influences(2, 4), 0.2).


friend(1,2).
friend(2,1).
friend(2,4).
friend(3,2).
friend(4,2).

example(smoke(1), 0.342, 0.342).
example(smoke(2), 0.342, 0.342).
example(smoke(3), 0.3, 0.3).
example(smoke(4), 0.34788, , 0.34788).