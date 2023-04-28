#task 1
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

#task 2 
class User():
	def __init__(self, login, password):
		self.login = login
		self.password = password

	def is_strong_password(self):
		if len(self.password).__gt__(8) and len(self.login).__ne__(len(self.password)):
			return True
		else:
			return False

short_pswd = User('user', 'qwerty')
simple_pwsd = User('super_user', 'super_user')
strong_pswd = User('admin', 'Qwerty12345')
print(short_pswd.is_strong_password())
print(simple_pwsd.is_strong_password())
print(strong_pswd.is_strong_password())


#task 3
class NobelWinner():
	winner = ''
	year = 0
	category = ''

	def __init__(self, winner, year, category):
		self.winner = winner
		self.year = year
		self.category = category

	def __str__(self):
		return f"{self.winner} выиграл наболевскую премию по {self.category} в {self.year}"

winner = NobelWinner('Роджер Пенроуз', 2020, 'физика')
print(winner)


#task 4
def sort_case_insensitive(lst):
	b = sorted(lst, key=str.lower)
	print(b)

a = ['context', 'Visible', 'center', 'acquisition', 'Football', 'testify','Responsible','cause']
print(sort_case_insensitive(a))


#task 5
class Person(object):
	def __init__(self, firstname, lastname, surname):
		self.firstname = firstname
		self.lastname = lastname
		self.surname = surname

	def __str__(self):
		return f'{self.lastname} {self.firstname} {self.surname}'

class Student(Person):
	def go_to_class(self, subject):
		self.subject = subject
		print(f'Школьник {Person(self.firstname, self.lastname, self.surname)} идет на {self.subject}')
class Teacher(Person):
	def teach_class(self, subject):
		self.subject = subject
		print(f'Учитель {Person(self.firstname, self.lastname, self.surname)} преподает {self.subject}')

student = Student('Иван', 'Иванов', 'Иванович')
teacher = Teacher('Петр', 'Петров', 'Эдуардович')
student.go_to_class('математику')
teacher.teach_class('информатику')