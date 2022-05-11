modeh(1, surf(+day)).
modeb(1, sunshine(+day)).
modeb(1, windok(+day)).
modeb(1, not pop(+day)).

day(1..40).

pf(pop(1), 0.4987).
pf(windok(1), 0.3591).
pf(sunshine(1), 0.4534).

pf(pop(2), 0.7391).
pf(windok(2), 0.6022).
pf(sunshine(2), 0.9837).

pf(pop(3), 0.2898).
pf(windok(3), 0.7423).
pf(sunshine(3), 0.2275).

example(surf(1), 0.325686619278).
example(surf(2), 0.259208287874).
example(surf(3), 0.5688181778499999).