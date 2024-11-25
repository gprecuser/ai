likes(john, susie). 
likes(X, susie). 
likes(john, Y). 
likes(john, Y), likes(Y, john). 
likes(john, susie); likes(john,mary). 
not(likes(john,pizza)). 
likes(john,susie) :- likes(john,mary).
friends(X,Y) :- likes(X,Y),likes(Y,X). 
hates(X,Y) :- not(likes(X,Y)).
enemies(X,Y) :- not(likes(X,Y)),not(likes(Y,X)).