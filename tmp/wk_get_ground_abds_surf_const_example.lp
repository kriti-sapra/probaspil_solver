var1(d1).


temp(mild).
temp(cold).


rule(r((idsubW,c(B),l)),1) :-temp(B). 
rule(r((idsubW,c(B),l),(idwidU,c,l(1))),2) :-temp(B). 
rule(r((idsubW,c(B),l),(idsuz3,c(D),l(1))),2) :-temp(B), temp(D). 
rule(r((idsubW,c(B),l),(idsuz3,c(D),l(1)),(idwidU,c,l(1))),3) :-temp(B), temp(D). 
