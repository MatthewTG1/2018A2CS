male(stefan).
male(ben).
male(matthew).
male(jah).
male(oscar).
male(matt).
female(sarah).
female(lucy).
female(katherine).

parent(stefan,ben). 
parent(elena,ben).
parent(stefan,matthew).
parent(sarah,matthew).
parent(stefan,lucy).
parent(sarah,lucy).
parent(katherine,oscar).
parent(katherine,matt).
parent(jah,oscar).
parent(jah,matt).
parent(dom,stefan).
parent(dom,sarah).
parent(letty,stefan).
parent(letty,elena).
parent(tom,katherine).
parent(tom,jah).
parent(letty,katherine).
parent(letty,jah).

brother(A,B) :-
	parent(P,A),parent(P,B),male(A),not(A=B).

sister(A,B) :- 
	parent(P,A),parent(P,B),female(A),not(A=B).

son(A,B) :- 
	parent(B,A),male(A).

daughter(A,B) :- 
	parent(B,A),female(A).

married(A,B) :- 
	parent(A,K),parent(B,K),not(A=B).

ancestor(A,B) :- 
	parent(A,B);
	parent(A,T),ancestor(T,B).