% Background

mother(katleen,stijn).
mother(katleen,pieter).
mother(lieve,soetkin).
mother(esther,lieve).
mother(esther,katleen).
mother(yvonne,willem).
mother(yvonne,lucy).
mother(alice,rose).
mother(rose,luc).
mother(rose,an).
mother(laura,esther).

person(pieter).
person(alice).
person(stijn).
person(katleen).
person(lieve).
person(willem).
person(bart).
person(esther).
person(laura).
person(lucy).
person(luc).
person(leon).
person(etienne).
person(yvonne).
person(prudent).
person(rose).
person(soetkin).
person(rene).
person(an).

female(alice).
female(an).
female(esther).
female(katleen).
female(laura).
female(lieve).
female(lucy).
female(rose).
female(soetkin).
female(yvonne).

male(bart).
male(etienne).
male(leon).
male(luc).
male(pieter).
male(prudent).
male(rene).
male(stijn).
male(willem).

male_ancestor(bart,stijn).
male_ancestor(bart,pieter).
male_ancestor(luc,soetkin).
male_ancestor(willem,lieve).
male_ancestor(willem,katleen).
male_ancestor(rene,willem).
male_ancestor(rene,lucy).
male_ancestor(leon,rose).
male_ancestor(etienne,luc).
male_ancestor(etienne,an).
male_ancestor(prudent,esther).
male_ancestor(rene,lieve).
male_ancestor(rene,katleen).
male_ancestor(rene,soetkin).
male_ancestor(rene,stijn).
male_ancestor(rene,pieter).
male_ancestor(etienne,soetkin).
male_ancestor(willem,soetkin).
male_ancestor(willem,stijn).
male_ancestor(willem,pieter).
male_ancestor(leon,luc).
male_ancestor(leon,an).
male_ancestor(leon,soetkin).
male_ancestor(prudent,lieve).
male_ancestor(prudent,katleen).
male_ancestor(prudent,soetkin).
male_ancestor(prudent,stijn).
male_ancestor(prudent,pieter).

female_ancestor(katleen,stijn).
female_ancestor(katleen,pieter).
female_ancestor(lieve,soetkin).
female_ancestor(esther,lieve).
female_ancestor(esther,katleen).
female_ancestor(yvonne,willem).
female_ancestor(yvonne,lucy).
female_ancestor(alice,rose).
female_ancestor(rose,luc).
female_ancestor(rose,an).
female_ancestor(laura,esther).
female_ancestor(yvonne,lieve).
female_ancestor(yvonne,katleen).
female_ancestor(yvonne,soetkin).
female_ancestor(yvonne,stijn).
female_ancestor(yvonne,pieter).
female_ancestor(rose,soetkin).
female_ancestor(esther,soetkin).
female_ancestor(esther,stijn).
female_ancestor(esther,pieter).
female_ancestor(alice,luc).
female_ancestor(alice,an).
female_ancestor(alice,soetkin).
female_ancestor(laura,lieve).
female_ancestor(laura,katleen).
female_ancestor(laura,soetkin).
female_ancestor(laura,stijn).
female_ancestor(laura,pieter).

grandmother(esther,soetkin).
grandmother(esther,stijn).
grandmother(esther,pieter).
grandmother(yvonne,lieve).
grandmother(yvonne,katleen).
grandmother(alice,luc).
grandmother(alice,an).
grandmother(rose,soetkin).
grandmother(laura,lieve).
grandmother(laura,katleen).

% Probabilistic facts

pf(father(bart,stijn), 0.7). 
%pf(father(bart,pieter), 0.9). 
%pf(father(luc,soetkin), 0.6). 
%pf(father(willem,lieve), 0.7). 
%pf(father(willem,katleen), 0.8). 
%pf(father(rene,willem), 0.9). 
%pf(father(rene,lucy), 0.7). 
%pf(father(leon,rose), 0.8). 
%pf(father(etienne,luc), 0.8). 
%pf(father(etienne,an), 0.9). 
%pf(father(prudent,esther), 0.7).

% Mode Bias
modeh(parent(+person, +person)).
modeb(father(+person, +person), [(max, 1)]).
modeb(mother(+person, +person), [(max, 1)]).

% Examples

example(parent(bart,stijn), 0.7).
%example(parent(bart,pieter), 0.9).
%example(parent(luc,soetkin), 0.6).
%example(parent(willem,lieve), 0.7).
%example(parent(willem,katleen), 0.8).
%example(parent(rene,willem), 0.9).
%example(parent(rene,lucy), 0.7).
%example(parent(leon,rose), 0.8).
%example(parent(etienne,luc), 0.8).
%example(parent(etienne,an), 0.9).
%example(parent(prudent,esther), 0.7).

example(parent(katleen,stijn), 1).
example(parent(katleen,pieter), 1).
example(parent(lieve,soetkin), 1).
example(parent(esther,lieve), 1).
example(parent(esther,katleen), 1).
example(parent(yvonne,willem), 1).
example(parent(yvonne,lucy), 1).
example(parent(alice,rose), 1).
example(parent(rose,luc), 1).
example(parent(rose,an), 1).
example(parent(laura,esther), 1).
