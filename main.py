#Создать класс Person
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.age} лет, я живу в {self.city}")

"""""
Person1 = Person("Hana", 20, "Токио")
Person1.introduce()
"""""

#Методы класса
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.age} лет, я живу в {self.city} ")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

"""""
person1 = Person("Rei", 16, "Корея")
person2 = Person("Aki", 30, "Киото")
person3 = Person("Ichiro", 18, "Нагоя")

person1.introduce()
print(person1.is_adult())
person2.introduce()
print(person2.is_adult())
person3.introduce()
print(person3.is_adult())
"""""

#Модификация и использование __str__ и __init__
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.age} лет, я живу в {self.city}")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def __str__(self):
        return f"Имя: {self.name}. Возраст: {self.age}. Город: {self.city}."

"""""
person4 = Person("Sora", 24, "Иокогама")

print(person4, person4.is_adult())
"""""






