person(a). person(b).
person(c). person(d).

subject(logic).
subject(biology).
subject(sport).
subject(physics).
subject(music).

%interested(a, logic).
interested(d, logic).
%interested(b, biology).
interested(c, biology).
interested(a, sport).
interested(b, sport).
interested(c, sport).
interested(a, physics).
interested(c, music).
interested(d, music).

%Ab
1 { pair(P, a); pair(P, b); pair(P, c); pair(P, d) } 1 :- person(P).

%IC
:- pair(P, P).

pair(P1, P2) :- pair(P2, P1).
shared_interest(P1, P2, I) :- interested(P1, I), interested(P2, I),pair(P1, P2).

#show shared_interest/3.

