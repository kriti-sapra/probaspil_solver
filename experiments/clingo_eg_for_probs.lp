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
shared_interest(P1, P2, I) :- interested(P1, I), interested(P2, I),pair(P1, P2).
%shared_disinterest(P1, P2, I) :- not interested(P1, I), not interested(P2, I), pair(P1, P2), interested(P3, I).

%pf(interested(a, logic), 0.4).
interested(d, logic).
%pf(interested(b, biology), 0.5).
interested(c, biology).
interested(a, sport).
interested(b, sport).
%interested(c, sport).
interested(a, physics).
interested(c, music).
%interested(d, music).