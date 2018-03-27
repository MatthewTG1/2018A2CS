Task 1.1
JSP structure diagram seek to break down problems into manageable chunks, to help people better understand the problem and to help them plan a solution.

Task 1.2
None: Sequence
Star:Repeated input, interation
Circle:Choice, selection

Task 1.3
NOT ROF("Staff.txt")
Salary > 50
Salary >= 90
Project manager
Lead developer
Manager

Task 1.4
... 
![](./JSP Diagram.png 'e')
...

Task 1.5
IF Salary >= 90 THEN Role ¡û ProjectManager ELSE IF Salary > 70 THEN Role ¡û Consultant ELSE Role ¡û LeadDeveloper ENDIF ENDIF

Task 1.6
def FindRole(salary):
	if salary >= 90:
		return "Project Manager"
	elif salary > 70:
		return "Consultant"
	elif salary >50:
		return "Lead Developer"
	else:
		return "Manager"

