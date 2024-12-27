
from main import Person

Person1 = Person("Hana", 20, "Токио")
Person1.introduce()


person1 = Person("Rei", 16, "Корея")
person2 = Person("Aki", 30, "Киото")
person3 = Person("Ichiro", 18, "Нагоя")

person1.introduce()
print(person1.is_adult())
person2.introduce()
print(person2.is_adult())
person3.introduce()
print(person3.is_adult())


person4 = Person("Sora", 24, "Иокогама")
print(person4, person4.is_adult())





