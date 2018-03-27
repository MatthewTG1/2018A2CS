len([],0).
len([_|T],L):-
	len(T,X),
	L is X+1.

mymember(I, [I|_]).
mymember(I, [_|T]):-
	mymember(I,T).