#!/Users/sdaniels/.pyenv/shims/python3

class Person:
	def __init__(self):
		self.name = None
		self.sex  = None
		self.age  = None
		self.taunt = None

	def talk_shit(self):
		print(self.taunt)
	

class Nice_Person(Person):
	def talk_shit(self):
		print("Im too nice to say bad things.")
	def show_penis(self):
		print("Im so free with my body and smart")

Brian = Person()
Shaun = Person()
gaybie = Nice_Person()

Brian.name = "Brian"
Brian.age  = "44"
Brian.sex  = "Gender fluid"
Brian.taunt = "Fuck you jagoff"

Shaun.name = "Shaun"
Shaun.age = "44"
Shaun.sex = "Oh man yeah!"
Shaun.taunt = "Lick my ballz"

gaybie.name = "gaybie"
gaybie.age = "21"
gaybie.sex = "big fag"
gaybie.taunt = "Lick my ballz"

Brian.talk_shit()
Shaun.talk_shit()
gaybie.talk_shit()
gaybie.show_penis()
Brian.show_penis()