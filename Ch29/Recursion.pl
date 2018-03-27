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
bunnyEars2(A,B) :-
	X is A-1,even(X),bunnyEars2(X,Y),B is Y+2;
	X is A-1,odd(X),bunnyEars2(X,Y),B is Y+3.

triangle(0,0).
triangle(1,1).
triangle(A,B) :-
	X is A-1,triangle(X,Y),B is Y+X+1.

sumDigits(0,0).
sumDigits(A,B) :-
	X is div(A,10),
	sumDigits(X,Y),
	B is Y+mod(A,10).

isSeven(7).
countSeven(0, 0).
countSeven(A,B) :-
	D is mod(A,10),X is div(A,10),countSeven(X,Y),
	((isSeven(D), B is Y+1 );(not(isSeven(D)), B is Y)).
	
	
	

	

	







