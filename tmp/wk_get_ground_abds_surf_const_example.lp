var1(d1).


temp(mild).
temp(cold).


rule(r((idsuMY,c(B),l)),1) :-temp(B). 
rule(r((idsuMY,c(B),l),(idwi43B,c,l(1))),2) :-temp(B). 
rule(r((idsuMY,c(B),l),(idsuqLC,c(D),l(1))),2) :-temp(B), temp(D). 
rule(r((idsuMY,c(B),l),(idsuqLC,c(D),l(1)),(idwi43B,c,l(1))),3) :-temp(B), temp(D). 
