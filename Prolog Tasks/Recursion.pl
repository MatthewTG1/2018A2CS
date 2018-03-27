even(X):- 0 is mod(X,2).
odd(X):-not(even(x)).


factorial(0,1).
factorial(N,F):-
	X is N-1,
	factorial(X,Y),
	F is N*Y.

bunnyEars(0,0).
bunnyEars(A,B):-
	X is A-1,
	bunnyEars(X,Y),
	B is Y+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(2,1).
fibonacci(A,B):-
	X is A-1,
	Z is A-2,
	fibonacci(X,Y),
	fibonacci(Z,C),
	B is Y+C.

bunnyEars2(0,0).
bunnyEars2(1,2).
bunnyEars2(2,5).
bunnyEars2(A,B):-
	
	
	

	

	







