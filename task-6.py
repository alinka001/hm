class Dog :
    def __init__(self, age, breed) :
        self.age = age
        self.breed = breed

    def bark(self):
        print("Гав-гав!")

    def get_human_age(self):
        age_in_months = round((self.age * 12), 1)
        if age_in_months < 24 :
            age_in_months *= 10.5
        else :
            after_24_months = age_in_months - 24
            before_24_months = age_in_months - after_24_months
            age_in_months = before_24_months * 10.5 + after_24_months * 4
            age_in_months = round((age_in_months / 12) , 2) # skopipastila iz proshloy homework)))
        return age_in_months
    

dog = Dog( 5, "Beagle")
dog.bark()
print(dog.get_human_age())