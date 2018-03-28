Task 3.1
character(habib).
character_type(habib,explorer).
pet(habib,fish).
has_skill(habib,time_travel).
animal(fish).
skill(time_travel).

Task 3.2
onlyPet(C,P):-
	character(c),animal(P).

Task 3.3
character(matt).
character(daniel).
animal(dragon).
animal(mouse).
skill(fly).
skill(omnipotent).
pet(matt,dragon).
pet(daniel,mouse).
has_skill(matt, fly).
has_skill(daniel,omnipotent).

Task 3.4
True.
X = princess.
X = jim.
X = invisibility.
X = jim.

Task 3.5
1.pet(jim,X).

2.has_skill(X,fly).

3.skill(X).

4.type_pet(T,P) :-
  	character_type(C,T),pet(C,P).
  type_pet(princess,X).
