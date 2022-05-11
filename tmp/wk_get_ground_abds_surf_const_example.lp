var1(d1).


temp(mild).
temp(cold).


rule(r((idsutgB,c(B),l)),1) :-temp(B). 
rule(r((idsutgB,c(B),l),(idwiVjB,c,l(1))),2) :-temp(B). 
rule(r((idsutgB,c(B),l),(idsuojB,c(D),l(1))),2) :-temp(B), temp(D). 
rule(r((idsutgB,c(B),l),(idsuojB,c(D),l(1)),(idwiVjB,c,l(1))),3) :-temp(B), temp(D). 
