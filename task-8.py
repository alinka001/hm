class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age


    def say_hello(self) :
        print(f"Привет, меня зовут {self.name}, и мне {self.age} лет.")

    def can_vote(self):
        if self.age > 18:
            return True
        else :
            return False
        
    
person = Person("Alina", 21)
person.say_hello()
print(person.can_vote())