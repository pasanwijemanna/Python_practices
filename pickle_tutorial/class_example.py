import pickle

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name)
        print(self.age)
        
person_obj = Person("pasan",24)

# with open("class.pickle","wb") as f:
#     pickle.dump(person_obj,f)


with open("class.pickle","rb") as f:
    person_data = pickle.load(f)
    
    
person_data.display()