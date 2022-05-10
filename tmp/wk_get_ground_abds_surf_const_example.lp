var1(d1).


temp(mild).
temp(cold).


rule(r((idsuRl,c(B),l)),1) :-temp(B). 
rule(r((idsuRl,c(B),l),(idwiQAB,c,l(1))),2) :-temp(B). 
rule(r((idsuRl,c(B),l),(idsuaH,c(D),l(1))),2) :-temp(B), temp(D). 
rule(r((idsuRl,c(B),l),(idsuaH,c(D),l(1)),(idwiQAB,c,l(1))),3) :-temp(B), temp(D). 
