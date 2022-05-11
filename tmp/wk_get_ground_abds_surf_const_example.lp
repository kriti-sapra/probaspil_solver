var1(d1).


temp(mild).
temp(cold).


rule(r((idsuKsB,c(B),l)),1) :-temp(B). 
rule(r((idsuKsB,c(B),l),(idwikT,c,l(1))),2) :-temp(B). 
rule(r((idsuKsB,c(B),l),(idsu1nB,c(D),l(1))),2) :-temp(B), temp(D). 
rule(r((idsuKsB,c(B),l),(idsu1nB,c(D),l(1)),(idwikT,c,l(1))),3) :-temp(B), temp(D). 
