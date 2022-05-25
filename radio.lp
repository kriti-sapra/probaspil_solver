on(1..4).
sometime(5..8).
node(X) :- on(X).
{node(X)} :- sometime(X).

0.1::link(1,2).
0.7::link(1,5).
0.2::link(2,4).
0.1::link(4,6).
0.4::link(3,6).
0.4::link(2,7).
0.8::link(5,8).
0.95::link(8,3).
0.1::link(7,6).

%:~ node(X). [-1, X]
:~ color(1,red), color(3,red). [-1]
:~ color(1,yellow), color(3,yellow). [-1]
:~ color(1,blue), color(3,blue). [-1]
1{color(V, red); color(V, yellow); color(V, blue)}1 :- node(V).
:- link(V,U), color(V,C), color(U,C).


#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.1]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.2]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.3]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.4]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.5]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.6]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.7]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.8]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=0.9]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=1]
#query(color(1,red), color(3,red);color(1,yellow), color(3,yellow);color(1,blue), color(3,blue)). [optim=2]
