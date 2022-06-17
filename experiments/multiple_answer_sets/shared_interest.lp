person(a). person(b).
person(c). person(d).

subject(logic).
subject(biology).
subject(sport).
subject(physics).
subject(music).

%Ab
1 { pair(P, a); pair(P, b); pair(P, c); pair(P, d) } 1 :- person(P).

%IC
:- pair(P, P).

pair(P1, P2) :- pair(P2, P1).

modeh(shared_interest(+person, +person, +subject)).
modeb(interested(+person, +subject), [(max, 2)]).
modeb(pair(+person, +person), [(max, 1)]).


pf(interested(a, logic), 0.3554).
interested(d, logic).
pf(interested(b, biology), 0.57797).
interested(c, biology).
interested(a, sport).
interested(b, sport).
pf(interested(c, sport), 0.6982).
interested(a, physics).
interested(c, music).
pf(interested(d, music), 0.8903).

example(shared_interest(c,d,music), 0.2968).
example(shared_interest(d,c,music), 0.2968).
example(shared_interest(d,a,logic), 0.1185).
example(shared_interest(a,d,logic), 0.1185).
example(shared_interest(b,c,sport), 0.2327).
example(shared_interest(c,b,sport), 0.2327).
example(shared_interest(b,c,biology), 0.1927).
example(shared_interest(c,b,biology), 0.1927).

% To learn:
%shared_interest(P1, P2, I) :- interested(P1, I), interested(P2, I),pair(P1, P2).